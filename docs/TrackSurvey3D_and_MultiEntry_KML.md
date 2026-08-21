# KartSimDT --- Track Survey 3D and Multi-Entry KML Architecture

**Status:** Architecture decision recorded\
**Scope:** Track Survey 3D auxiliary branch, KML entry-point
architecture, AIM/Google Earth comparison, MATLAB visualization\
**Primary track dataset:** `data/tracks/<TrackName>/`

------------------------------------------------------------------------

## 1. Purpose

KartSimDT is a Digital Twin platform rather than a single-track Blender
or Assetto Corsa project.

The platform must therefore separate:

1.  the **core track data pipeline**;
2.  the **auxiliary Track Survey 3D validation branch**;
3.  visualization tools such as Blender and MATLAB;
4.  track-specific data from reusable platform code.

The Track Survey 3D branch remains in the project as an engineering and
validation tool. It is not the primary runtime or track-generation
pipeline.

------------------------------------------------------------------------

# 2. Track Survey 3D --- Auxiliary Branch

## 2.1 Role

Track Survey 3D is an **auxiliary engineering branch** used to verify
and investigate track geometry.

Its purpose is to combine and compare:

-   Google Earth centerline;
-   Google Elevation data;
-   AIM GPS/telemetry;
-   derived 3D track geometry.

The branch answers the engineering question:

> Does the derived track geometry correspond to the real track and
> available telemetry?

It is therefore a validation and analysis path, not the platform's main
source of runtime behavior.

------------------------------------------------------------------------

## 2.2 Auxiliary Architecture

``` text
                    TRACK SURVEY 3D
                           |
              +------------+------------+
              |                         |
              v                         v
       Google Earth                  AIM
        Centerline                Telemetry
              |                         |
              +------------+------------+
                           |
                           v
                     Comparison
                           |
                           v
                      Validation
                           |
              +------------+------------+
              |                         |
              v                         v
        Google Elevation          3D Survey Analysis
```

The branch may generate diagnostic or derived artifacts, but these
artifacts must not become hidden replacements for the canonical platform
track data.

------------------------------------------------------------------------

# 3. Real Track Entry Point

The platform must operate on real track datasets located under:

``` text
data/tracks/
```

Each track owns its own data:

``` text
data/
└── tracks/
    ├── Aukštadvaris/
    ├── Kandava/
    ├── Mande_Kart/
    ├── Plytinė/
    └── Smalininkai/
```

The platform code must not contain a hardcoded assumption that the
active track is Aukštadvaris.

For example, this is not acceptable as a platform-level design:

``` python
track_folder = root / "data" / "tracks" / "Aukštadvaris"
```

The track name must come from the selected track context / entry point.

------------------------------------------------------------------------

# 4. KML Entry Point

## 4.1 Current Validated Entry Point

For Aukštadvaris, the validated source is:

``` text
data/tracks/Aukštadvaris/google_earth/centerline.kml
```

This KML contains:

``` text
677 centerline points
677 elevation points
0 missing elevation values
```

The KML was validated with Google Elevation data before becoming the
current track input.

Example values:

``` text
First  : 147.938919 m
Middle : 151.387283 m
Last   : 147.931839 m
```

------------------------------------------------------------------------

# 5. KML Processing Pipeline

The current processing chain is:

``` text
data/tracks/<TrackName>/google_earth/centerline.kml
                         |
                         v
                TrackSurveyKmlReader
                         |
                         v
                 TrackSurveySession
                         |
                         v
               CenterlineGeometryMapper
                         |
                         v
                 CenterlineGeometry
                     X / Y / Z
                         |
                         v
                 CenterlineJsonExporter
                         |
                         v
data/tracks/<TrackName>/centerline.json
```

The resulting `centerline.json` is a derived local engineering
representation.

Example:

``` json
{
    "format": "KartSimDT",
    "version": 1,
    "geometry": "Centerline",
    "coordinate_system": "Local",
    "point_count": 677,
    "points": [
        {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0
        },
        {
            "x": -0.06350887996568073,
            "y": 1.2625788453448195,
            "z": 0.016525000000001455
        }
    ]
}
```

The important architectural fact is that elevation is preserved during
the transformation.

------------------------------------------------------------------------

# 6. Elevation Verification

The local coordinate system uses the first centerline point as the
origin.

Therefore:

``` text
local Z = point elevation - origin elevation
```

For the validated Aukštadvaris data:

``` text
Google elevation:

Minimum : 146.499 m
Maximum : 151.931 m
Delta   : 5.432 m
```

After conversion to local coordinates and import into Blender:

``` text
Blender:

Points : 677
Z MIN  : -1.440323 m
Z MAX  :  3.991821 m
Z Δ    :  5.432144 m
```

The elevation delta is preserved.

This confirms:

``` text
Google Elevation
      |
      v
Track Survey KML
      |
      v
TrackSurveySession
      |
      v
CenterlineGeometry
      |
      v
centerline.json
      |
      v
Blender
```

does not lose the vertical component.

------------------------------------------------------------------------

# 7. Blender Role

Blender is a **visualization and scene-construction component**.

It must not become the owner of the track survey calculation.

The current importer consumes:

``` text
data/tracks/<TrackName>/centerline.json
```

and creates a Blender 3D curve.

The importer maps:

``` python
spline_point.co = (
    point["x"],
    point["y"],
    point["z"],
    1.0,
)
```

Therefore Blender receives already calculated local 3D geometry.

Its responsibility is to:

-   visualize the centerline;
-   construct the visual scene;
-   align the track with orthophoto/reference assets;
-   support later visual scene generation.

Blender does not calculate Google elevation.

------------------------------------------------------------------------

# 8. MATLAB Visualization

MATLAB is an additional engineering visualization and analysis tool.

Its role is similar to the analytical side of Track Survey 3D:

``` text
Track Survey / AIM / derived geometry
                |
                v
             MATLAB
                |
       +--------+--------+
       |        |        |
       v        v        v
     2D plot  3D plot  comparison
```

MATLAB may be used to visualize:

-   centerline geometry;
-   elevation profile;
-   3D track shape;
-   AIM GPS trajectory;
-   Google Earth centerline;
-   trajectory-to-centerline comparison;
-   elevation comparison;
-   geometric diagnostics.

MATLAB is therefore a **consumer/analysis tool**, not the source of the
track data.

The same rule applies as with Blender:

> Visualization tools consume KartSimDT data; they do not define the
> canonical track geometry.

------------------------------------------------------------------------

# 9. Google Earth ↔ AIM Visual Comparison

The auxiliary Track Survey 3D branch supports visual comparison between:

``` text
Google Earth Centerline
            +
AIM GPS trajectory
            +
Elevation
```

The comparison can be performed in:

-   Google Earth / map imagery;
-   Blender;
-   MATLAB;
-   future KartSimDT visualization tools.

The purpose is to establish confidence in:

-   centerline placement;
-   track shape;
-   coordinate transformation;
-   track length;
-   elevation profile;
-   correspondence between surveyed geometry and actual driving.

This comparison is particularly important before using the track for
downstream Digital Twin components.

------------------------------------------------------------------------

# 10. Source vs Derived Data

The architecture must distinguish source data from derived artifacts.

## Source

``` text
data/tracks/<TrackName>/google_earth/centerline.kml
```

The KML is an input to Track Survey processing.

## Derived

``` text
data/tracks/<TrackName>/centerline.json
```

The JSON is a local engineering representation generated by KartSimDT.

## Visualization

``` text
data/tracks/<TrackName>/blender/
```

contains Blender scene artifacts.

## Telemetry

``` text
data/tracks/<TrackName>/aim/
```

contains AIM data.

This separation must remain explicit.

------------------------------------------------------------------------

# 11. Transition: Fixed Test KML → Multi-Entry KML

The platform was initially developed using fixed test data such as:

``` text
tests/data/aukstadvaris/survey/centerline.kml
```

and:

``` text
tests/data/aukstadvaris/survey/centerline_google_elevation.kml
```

This was useful during platform development because individual modules
could be tested against stable fixtures.

However, this is not the final platform architecture.

The production-oriented path is:

``` text
OLD

tests/data/aukstadvaris/...
        |
        v
hardcoded runner
        |
        v
single test KML
```

becoming:

``` text
NEW

data/tracks/
    |
    +-- <TrackName>/
            |
            +-- google_earth/
            |      |
            |      +-- centerline.kml
            |
            +-- aim/
            |
            +-- blender/
            |
            +-- final/
            |
            +-- walkthrough/
            |
            +-- centerline.json
            |
            +-- metadata.yaml
```

The platform must process the selected track through a common entry
point.

------------------------------------------------------------------------

# 12. Multi-Entry KML Principle

The KML reader itself should remain generic.

It should not know:

``` text
Aukštadvaris
Kandava
Plytinė
Smalininkai
```

The reader only knows:

> I was given a KML file; read its track survey data.

Track selection belongs above the reader.

Conceptually:

``` text
Track Context
     |
     v
Track Directory
     |
     v
KML Entry Point
     |
     v
TrackSurveyKmlReader
```

This allows the same processing pipeline to be reused for every track.

------------------------------------------------------------------------

# 13. Target Multi-Track Architecture

The intended architecture is:

``` text
                         KartSimDT
                             |
                       Track Context
                             |
             +---------------+---------------+
             |               |               |
             v               v               v
        Aukštadvaris      Šiauliai       Kandava
             |               |               |
             v               v               v
       google_earth      google_earth    google_earth
        centerline.kml   centerline.kml  centerline.kml
             |               |               |
             +---------------+---------------+
                             |
                             v
                    TrackSurvey Pipeline
                             |
                             v
                    CenterlineGeometry
                             |
                +------------+------------+
                |            |            |
                v            v            v
             Blender      MATLAB       AIM tools
```

The processing code is shared.

Only the track context and its data directory change.

------------------------------------------------------------------------

# 14. Migration Rule

The migration from fixed test KML to multi-entry KML should be
incremental.

## Phase 1 --- Completed

Validate the complete pipeline using stable test data.

``` text
tests/data/aukstadvaris/
```

Purpose:

-   unit testing;
-   integration testing;
-   module development;
-   regression testing.

## Phase 2 --- Current

Move the actual Aukštadvaris dataset into:

``` text
data/tracks/Aukštadvaris/
```

and make the real track dataset the operational input.

This phase is now validated for the centerline + Google elevation chain.

## Phase 3 --- Next

Remove hardcoded track assumptions from runners and visualization
importers.

Introduce a reusable track context / track entry-point mechanism.

## Phase 4

Run the same pipeline against:

``` text
data/tracks/Kandava/
data/tracks/Mande_Kart/
data/tracks/Plytinė/
data/tracks/Smalininkai/
```

without changing platform source code.

------------------------------------------------------------------------

# 15. Architectural Decision

The following decisions are recorded:

### Decision A

**Track Survey 3D remains an auxiliary validation branch.**

### Decision B

**Blender is visualization/scene construction, not track survey
calculation.**

### Decision C

**MATLAB is visualization/engineering analysis, not the source of track
geometry.**

### Decision D

**Real operational track data lives under `data/tracks/<TrackName>/`.**

### Decision E

**`tests/data` remains for tests and regression fixtures, not
operational track input.**

### Decision F

**KML processing must evolve from a fixed test KML to a multi-track
entry-point architecture.**

### Decision G

**Track selection must be external to `TrackSurveyKmlReader`.**

### Decision H

**The canonical derived centerline for downstream consumers is the local
3D `CenterlineGeometry` representation exported as `centerline.json`.**

------------------------------------------------------------------------

# 16. Current Status

For Aukštadvaris:

``` text
Google Earth centerline       PASS
Google Elevation injection    PASS
TrackSurvey KML reading       PASS
Elevation completeness        PASS
CenterlineGeometry mapping    PASS
3D centerline JSON             PASS
Blender 3D Z import            PASS
```

The validated chain is:

``` text
data/tracks/Aukštadvaris/google_earth/centerline.kml
                         |
                         v
                  Track Survey
                         |
                         v
              CenterlineGeometry
                         |
                         v
data/tracks/Aukštadvaris/centerline.json
                         |
                         v
                     Blender
```

The Track Survey 3D / AIM / Google Earth comparison branch remains
available for engineering validation.

------------------------------------------------------------------------

# 17. Next Architectural Step

The next task is **not** to add more elevation processing.

The next task is:

> Define the reusable multi-track entry-point mechanism and remove
> track-specific hardcoding from the runners and Blender importer.

The desired result is:

``` text
KartSimDT
   |
   +-- select track
          |
          +-- resolve data/tracks/<TrackName>
          |
          +-- resolve KML entry point
          |
          +-- run Track Survey
          |
          +-- produce canonical 3D centerline
          |
          +-- expose geometry to visualization consumers
```

Only after this foundation is clean should downstream Digital Twin
components such as Assetto Corsa integration and Digital Coach be
connected.
