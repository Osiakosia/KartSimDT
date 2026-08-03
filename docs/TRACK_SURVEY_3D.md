# Track Survey 3D Specification

**Status:** Planned\
**Version:** 1.0\
**Project:** KartSimDT\
**Component:** Track Survey\
**Feature:** Third Coordinate / Elevation Implementation

## 1. Purpose

`Track Survey 3D` extends the existing Track Survey pipeline by
implementing the third spatial coordinate: **elevation**.

The existing Track Survey pipeline already provides surveyed horizontal
geometry:

``` text
longitude
latitude
elevation = None
```

The existing domain and visualization models already support elevation
and local Z coordinates.

The purpose of Track Survey 3D is therefore **not to redesign the
geometry pipeline**, but to supply the missing elevation information
using canonical KartSimDT telemetry data.

Target result:

``` text
TrackSurvey Point
longitude
latitude
elevation
```

Existing downstream pipeline:

``` text
TrackSurveySession
        ↓
CenterlineGeometryMapper
        ↓
CoordinateTransform
        ↓
LocalPoint(x, y, z)
        ↓
CenterlineGeometry
        ↓
centerline.json
        ↓
Blender
```

## 2. Current State

The existing Track Survey source is Google Earth KML:

``` text
Google Earth KML
        ↓
TrackSurveyKmlReader
        ↓
TrackSurveyRawData
        ↓
TrackSurveyMapper
        ↓
TrackSurveySession
        ↓
Centerline
```

The Track Survey domain model already supports elevation:

``` python
@dataclass(slots=True)
class Point:
    longitude: float
    latitude: float
    elevation: float | None = None
```

The current KML source does not provide usable elevation data, so the
current centerline is effectively:

``` text
longitude ✓
latitude  ✓
elevation None
```

The visualization pipeline already supports Z. `CoordinateTransform`
calculates:

``` python
z = point_elevation - origin_elevation
```

and `centerline.json` already exports `point.z`.

Therefore no redesign of the Blender or local coordinate pipeline is
required.

## 3. Elevation Source

Elevation will be obtained from the existing canonical telemetry domain.

``` text
AiM / MyChron
      ↓
io/aim
      ↓
AimMapper
      ↓
TelemetrySession
```

The existing channel registry maps GPS latitude, GPS longitude and GPS
altitude into canonical telemetry channels.

Track Survey 3D MUST consume `TelemetrySession` and MUST NOT directly
consume CSV, XRK, AiM-specific structures, or MyChron-specific
structures.

``` text
RAW source
    ↓
source adapter / parser
    ↓
canonical domain data
    ↓
processing
    ↓
derived engineering products
```

## 4. Inputs

Track Survey 3D receives two canonical inputs.

### 4.1 Track Survey

``` python
TrackSurveySession
```

providing:

``` text
centerline.points[].longitude
centerline.points[].latitude
centerline.points[].elevation
```

Normally elevation will initially be `None`.

### 4.2 Telemetry

``` python
list[TelemetrySession]
```

Each usable telemetry session must provide synchronized:

``` text
gps_latitude
gps_longitude
gps_altitude
```

The architecture must support one or multiple telemetry sessions.

## 5. Output

The output remains `TrackSurveySession`, but its centerline contains the
third coordinate:

``` text
Point
├── longitude
├── latitude
└── elevation
```

Elevation remains an **absolute measured/derived elevation** at the
Track Survey domain level. Local Z conversion remains the responsibility
of `CoordinateTransform`.

## 6. Core Constraint

Track Survey 3D MUST NOT modify the horizontal Track Survey geometry:

``` text
longitude input == longitude output
latitude input  == latitude output
```

Only `elevation` is implemented in this stage.

GPS telemetry is used as an elevation measurement source, not as a
replacement centerline. Future **True Centerline** processing remains a
separate feature.

## 7. Spatial Association

The number of Track Survey points and telemetry samples is not expected
to match. Index-based assignment is therefore prohibited:

``` python
survey.points[i].elevation = gps_altitude[i]  # INVALID
```

Elevation must be determined spatially:

``` text
Track Survey point
      lon / lat
          ↓
Telemetry GPS samples
 lat / lon / altitude
          ↓
Spatial association
          ↓
Elevation estimate
```

The exact estimation algorithm may evolve without changing the public
Track Survey 3D contract.

Possible methods include nearest sample, nearest N samples, distance
weighting, median estimation, multiple-lap aggregation, outlier
rejection and profile smoothing.

## 8. Multiple Sessions

The design must support multiple telemetry sessions from the beginning:

``` text
TelemetrySession 1 ─┐
TelemetrySession 2 ─┤
TelemetrySession 3 ─┼──► Track Survey 3D
TelemetrySession 4 ─┤
TelemetrySession 5 ─┘
                     ↓
              Elevation Profile
```

The first implementation may operate on one session, but the public API
must not prevent multi-session processing.

## 9. Proposed API

``` python
class TrackSurvey3DBuilder:
    """Build the third Track Survey coordinate from canonical telemetry."""

    def build(
        self,
        survey: TrackSurveySession,
        telemetry_sessions: list[TelemetrySession],
    ) -> TrackSurveySession:
        ...
```

The builder operates only on KartSimDT domain objects.

## 10. Validation

Minimum requirements:

-   Track Survey centerline exists and contains points.
-   `gps_latitude` exists.
-   `gps_longitude` exists.
-   `gps_altitude` exists.
-   GPS channel lengths match.
-   At least one telemetry session is supplied.

Invalid or missing data must produce an explicit domain error.

The system MUST NOT silently replace missing telemetry elevation with
zero.

## 11. Quality and Diagnostics

Track Survey 3D should eventually expose diagnostics such as:

-   telemetry sessions used
-   GPS samples considered
-   GPS samples rejected
-   distance from centerline
-   measurements per centerline point
-   elevation spread
-   missing sections
-   interpolated sections

Diagnostics should remain separate from the core `Point` geometry model.

## 12. Non-Goals

Track Survey 3D does NOT implement:

-   True Centerline generation
-   XY centerline correction
-   track width
-   road mesh
-   terrain
-   banking
-   camber
-   surface reconstruction
-   ideal racing line
-   vehicle dynamics
-   Blender calibration
-   raw AiM parsing
-   raw KML parsing

## 13. Target Architecture

``` text
 Google Earth KML                  AiM / MyChron
        │                               │
        ▼                               ▼
TrackSurveyParser                    io/aim
        │                               │
        ▼                               ▼
TrackSurveySession              TelemetrySession(s)
  lon / lat / None               lat / lon / altitude
        │                               │
        └──────────────┬────────────────┘
                       ▼
              TrackSurvey3DBuilder
                       ▼
               TrackSurveySession
                lon / lat / elev
                       ▼
            CenterlineGeometryMapper
                       ▼
              CoordinateTransform
                       ▼
                Local XYZ Geometry
                       ▼
                centerline.json
                       ▼
                    Blender
```

## 14. Implementation Sprints

### Sprint TS3D.1 --- Telemetry Contract & Validation

**Goal:** establish a reliable input boundary.

Implement:

-   `TrackSurvey3DBuilder` skeleton
-   Track Survey 3D validation
-   required telemetry channel lookup
-   channel length validation
-   domain exceptions

Tests:

-   valid survey accepted
-   empty survey rejected
-   missing `gps_latitude` rejected
-   missing `gps_longitude` rejected
-   missing `gps_altitude` rejected
-   different channel lengths rejected
-   empty telemetry session list rejected

**Deliverable:** Track Survey 3D accepts validated canonical inputs.

### Sprint TS3D.2 --- GPS Measurement Model

**Goal:** convert telemetry channels into an internal spatial
measurement representation.

Conceptual model:

``` python
GpsElevationSample(
    latitude=...,
    longitude=...,
    elevation=...,
)
```

No Track Survey modification yet.

Tests cover sample synchronization, channel conversion, invalid values,
missing values and multiple sessions.

**Deliverable:** clean GPS elevation measurement dataset.

### Sprint TS3D.3 --- Spatial Matching

**Goal:** associate Track Survey points with telemetry measurements.

``` text
Survey Point XY
      ↓
spatial search
      ↓
Telemetry GPS sample
      ↓
distance
      ↓
elevation
```

The matching algorithm must be isolated so it can later be replaced.

Tests:

-   exact coordinate match
-   nearest sample
-   multiple candidates
-   maximum allowed distance
-   no valid nearby measurement

**Deliverable:** every matchable Track Survey point can obtain an
elevation candidate.

### Sprint TS3D.4 --- Elevation Profile

**Goal:** construct the first complete Track Survey elevation profile.

``` text
spatial matches
      ↓
elevation estimates
      ↓
Point.elevation
      ↓
TrackSurveySession 3D
```

Critical invariant:

``` text
input.longitude == output.longitude
input.latitude  == output.latitude
```

Tests:

-   XY preserved exactly
-   elevation populated
-   point ordering preserved
-   metadata preserved

**Deliverable:** first complete `TrackSurveySession` with XYZ
information.

### Sprint TS3D.5 --- Multi-Session Elevation

**Goal:** use repeated telemetry measurements to create a robust
elevation profile.

Candidate aggregation methods include median, distance weighting and
outlier rejection. The final method should be selected from actual
Aukštadvaris telemetry characteristics.

Tests must include artificial GPS altitude noise and outliers.

**Deliverable:** robust multi-session elevation profile.

### Sprint TS3D.6 --- Geometry & Blender Validation

**Goal:** verify the complete existing downstream pipeline.

``` text
TrackSurveySession 3D
        ↓
CenterlineGeometryMapper
        ↓
CoordinateTransform
        ↓
LocalPoint.z
        ↓
centerline.json
        ↓
Blender TrackSurvey
```

Validate:

-   non-zero Z
-   reasonable elevation range
-   continuous profile
-   correct origin Z
-   XY unchanged
-   Blender curve follows elevation profile
-   scene calibration remains unchanged

**Deliverable:** Aukštadvaris TrackSurvey rendered as validated 3D
geometry.

## 15. Definition of Done

Track Survey 3D is complete when:

-   [ ] canonical `TelemetrySession` is the elevation source
-   [ ] no raw telemetry is parsed by Track Survey 3D
-   [ ] KML centerline XY remains unchanged
-   [ ] elevation is assigned to Track Survey points
-   [ ] multiple telemetry sessions are supported
-   [ ] missing/invalid telemetry produces explicit errors
-   [ ] `TrackSurveySession` contains XYZ survey information
-   [ ] `CoordinateTransform` generates meaningful local Z
-   [ ] `centerline.json` contains meaningful Z values
-   [ ] Blender imports the resulting 3D centerline
-   [ ] automated tests pass
-   [ ] architecture documentation is updated

## 16. Project Sequence

``` text
Track Survey 2D          ✓
Orthophoto calibration   ✓
Scene calibration        ✓
        ↓
Track Survey 3D          ← CURRENT
        ↓
True Centerline          future
        ↓
Road Mesh
        ↓
Terrain / banking
        ↓
Simulation geometry
```

Track Survey XYZ geometry should be completed before Road Mesh
generation so downstream surface geometry can be built from the final
three-dimensional centerline rather than being rebuilt later.
