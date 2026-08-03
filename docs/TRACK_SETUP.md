# KartSimDT Track Setup

## Status

**Reference track:** Aukštadvaris

### Current implementation

- Google Earth orthophoto metric calibration
- Independent X/Y metres-per-pixel calibration
- Canonical `centerline.json`
- Blender `TrackSurvey` import
- Persistent `scene_transform.json`
- KartSimDT interactive Orthophoto calibration
- Calibration Save / Reset
- Calibration restore after Blender scene load
- Reproducible Blender engineering scene build

### Planned

- Track manifest (`track.json`)
- Dynamic track selection
- Telemetry input
- LiDAR / SLAM input
- Video input
- Track surface geometry generation
- Racing-line and telemetry validation

---

# 1. Purpose

This document defines the standard KartSimDT workflow for adding,
calibrating, validating, and maintaining a track.

The goal is to provide a reproducible process for:

- adding raw track source data;
- defining official data entry points;
- calibrating reference imagery to physical metric dimensions;
- converting source geometry into canonical KartSimDT data;
- building the Blender engineering scene;
- aligning scene objects without modifying source measurements;
- preserving calibration between Blender sessions;
- validating the resulting track baseline;
- supporting future telemetry, LiDAR, SLAM, and video sources without
  changing the core architecture.

The Aukštadvaris track is the current reference implementation.

---

# 2. Core Principle

A KartSimDT track must be reproducible.

A Blender engineering scene should be rebuildable from:

```text
source data
+
source calibration
+
canonical KartSimDT geometry
+
scene transformation data
```

The `.blend` file must not become the only authoritative source of track
geometry or calibration.

Raw source data must not be manually modified merely to make it visually
fit the Blender scene.

The intended data flow is:

```text
RAW SOURCE DATA
       │
       ▼
IMPORT / CALIBRATION / NORMALIZATION
       │
       ▼
CANONICAL KARTSIMDT DATA
       │
       ▼
BLENDER ENGINEERING SCENE
       │
       ▼
SCENE ALIGNMENT
       │
       ▼
VALIDATED TRACK BASELINE
```

---

# 3. Track Data Root

All data belonging to a track must live under one track root:

```text
data/
└── tracks/
    └── <track_name>/
```

The track directory is the single data root for that track.

Current and planned structure:

```text
data/
└── tracks/
    └── <track_name>/
        │
        ├── google_earth/
        │   ├── <source_image>.png
        │   └── calibration.json
        │
        ├── survey/
        │   └── <raw survey source files>
        │
        ├── telemetry/
        │   └── <telemetry sessions>
        │
        ├── lidar/
        │   └── <LiDAR / SLAM datasets>
        │
        ├── video/
        │   └── <track video sources>
        │
        ├── centerline.json
        ├── track.json
        │
        └── blender/
            ├── scene.blend
            └── scene_transform.json
```

Not all directories are required for every track.

The following are currently reserved/planned entry points:

- `survey/`
- `telemetry/`
- `lidar/`
- `video/`
- `track.json`

They define the intended architecture but are not necessarily part of the
current runtime implementation.

---

# 4. Data Classification

KartSimDT distinguishes four major classes of track data.

## 4.1 Raw source data

Examples:

```text
Google Earth image
KML
GPS survey
MyChron session
Race Studio export
LiDAR point cloud
SLAM dataset
video
```

Raw data should be preserved as received whenever practical.

---

## 4.2 Source calibration

Calibration describes how raw measurements map to physical units.

Example:

```text
Google Earth pixels
        ↓
metres
```

This data belongs with the corresponding source.

---

## 4.3 Canonical KartSimDT data

Canonical data is normalized into a representation understood by the
KartSimDT pipeline.

Current example:

```text
centerline.json
```

Blender should consume canonical KartSimDT data rather than depend directly
on every possible source format.

---

## 4.4 Scene transformation data

Scene transformations describe how already calibrated or normalized objects
are placed in the Blender engineering coordinate system.

Current file:

```text
blender/scene_transform.json
```

Scene transformation data must remain separate from source calibration.

---

# 5. Official Track Data Entry Points

## 5.1 Orthophoto / Reference Imagery

Official entry point:

```text
data/tracks/<track_name>/google_earth/
```

Current source:

```text
Google Earth
```

Typical structure:

```text
google_earth/
├── <source_image>.png
└── calibration.json
```

The image provides spatial reference imagery.

`calibration.json` describes the metric calibration of that image.

The source image filename must be stored in calibration data so the
calibration can always be traced back to the exact image from which it was
calculated.

---

## 5.2 Survey / Centerline Source

Raw survey entry point:

```text
data/tracks/<track_name>/survey/
```

Possible source formats include:

```text
KML
GPS survey
measured track survey
external GIS data
```

Source data is converted or normalized into:

```text
data/tracks/<track_name>/centerline.json
```

Pipeline:

```text
KML / GPS / Survey
        │
        ▼
conversion / normalization
        │
        ▼
centerline.json
        │
        ▼
import_track_survey.py
        │
        ▼
TrackSurvey
```

This separation allows future source formats to be introduced without
changing the Blender importer.

For example:

```text
Google Earth KML ─┐
Survey GPS ───────┤
MyChron GPS ──────┼──→ normalization ──→ centerline.json
Other GIS ────────┘
```

---

## 5.3 Telemetry

Reserved entry point:

```text
data/tracks/<track_name>/telemetry/
```

Expected sources include:

```text
MyChron
Race Studio
GPS sessions
lap telemetry
vehicle dynamics data
```

Telemetry is not currently part of the basic Blender track construction
pipeline.

Future telemetry processing should convert source sessions into
KartSimDT-defined intermediate or canonical representations before they are
used for:

- track validation;
- racing-line analysis;
- lap-time comparison;
- vehicle model validation;
- simulator validation.

Raw telemetry must not be manually moved or distorted merely to match
Blender geometry.

---

## 5.4 LiDAR / SLAM

Reserved entry point:

```text
data/tracks/<track_name>/lidar/
```

Possible future sources:

```text
LiDAR scans
SLAM point clouds
mobile mapping
Raspberry Pi acquisition
NVIDIA Orin acquisition / processing
```

Raw point-cloud data must remain separate from Blender scene alignment.

Any coordinate registration required to combine point clouds with the
canonical track model should be explicitly defined and reproducible.

---

## 5.5 Video

Reserved entry point:

```text
data/tracks/<track_name>/video/
```

Possible future uses:

- visual track validation;
- synchronized telemetry/video analysis;
- SLAM;
- surface reconstruction;
- object/environment reconstruction.

Video remains source data and should not become implicit Blender scene
state.

---

# 6. Canonical Centerline

Current canonical centerline location:

```text
data/tracks/<track_name>/centerline.json
```

It is consumed by:

```text
blender/importers/import_track_survey.py
```

and creates the Blender object:

```text
TrackSurvey
```

The canonical centerline can contain XYZ information.

Conceptually:

```text
X = horizontal track geometry
Y = horizontal track geometry
Z = elevation
```

For the current Aukštadvaris reference dataset:

```text
Points: 677
```

The canonical centerline should not be manually modified merely to make it
visually fit the Orthophoto.

If alignment is required, that alignment belongs in the appropriate
transformation layer.

---

# 7. Orthophoto Metric Calibration

Orthophoto metric calibration establishes the physical dimensions of the
source image.

It is different from Blender scene alignment.

Calibration file:

```text
data/tracks/<track_name>/google_earth/calibration.json
```

Conceptually:

```text
image pixels
     │
     ▼
metres per pixel
     │
     ▼
physical image dimensions
```

Both image axes must be calibrated independently.

Use:

```text
metres_per_pixel_x
metres_per_pixel_y
```

Do not assume that X and Y resolution are identical.

---

# 8. Google Earth Calibration Procedure

For a new track:

1. Prepare the reference Google Earth image.
2. Preserve the exact image used for calibration.
3. Measure a known horizontal/X reference distance.
4. Measure a known vertical/Y reference distance.
5. Record the image pixel dimensions.
6. Calculate metres per pixel independently for X and Y.
7. Calculate physical image dimensions.
8. Store calibration information in `calibration.json`.
9. Verify the resulting dimensions in Blender.

Reference measurements should preferably be aligned with the image axes.

The fundamental equations are:

```text
metres_per_pixel_x =
    reference_distance_x_m / reference_distance_x_px

metres_per_pixel_y =
    reference_distance_y_m / reference_distance_y_px
```

Then:

```text
physical_width =
    image_width_px × metres_per_pixel_x

physical_height =
    image_height_px × metres_per_pixel_y
```

---

# 9. Aukštadvaris Reference Calibration

Aukštadvaris is the reference implementation for the current calibration
pipeline.

Google Earth reference measurements:

```text
X reference distance = 200.32 m
Y reference distance = 200.04 m
```

Reference image dimensions:

```text
8192 × 5125 px
```

Calculated metric resolution:

```text
X = 0.06461674 m/px
Y = 0.06448964 m/px
```

Calculated physical Orthophoto dimensions:

```text
Width  = 529.340 m
Height = 330.509 m
```

The Blender Orthophoto should therefore be created at approximately:

```text
529.340 × 330.509 m
```

with object scale:

```text
1.0, 1.0, 1.0
```

after metric construction.

These values are reference values for verifying the pipeline.

They must not be copied into another track's calibration.

---

# 10. Source Calibration vs Scene Alignment

These two operations must never be confused.

## Source calibration

Stored in:

```text
google_earth/calibration.json
```

Answers:

> What physical size does this source image represent?

Conceptually:

```text
pixels → metres
```

---

## Scene alignment

Stored in:

```text
blender/scene_transform.json
```

Answers:

> Where should this already metric object be located in the engineering
> scene?

Conceptually:

```text
metric object → Blender scene position/orientation
```

Changing scene alignment must not alter the underlying source calibration.

---

# 11. Blender Scene Transformation

Scene transformation file:

```text
data/tracks/<track_name>/blender/scene_transform.json
```

Current structure:

```json
{
    "version": 1,
    "orthophoto": {
        "scale": 1.0,
        "rotation": 0.0,
        "offset_x": 0.0,
        "offset_y": 0.0
    },
    "track_centerline": {
        "scale": 1.0,
        "rotation_deg": 0.0,
        "offset_x": 0.0,
        "offset_y": 0.0,
        "offset_z": 0.0
    }
}
```

The exact numerical offsets are track-specific.

`orthophoto` and `track_centerline` are independent sections.

Saving one section must preserve the other.

---

# 12. KartSimDT Orthophoto Calibration

The KartSimDT Blender addon currently exposes:

```text
Scale
Rotation
Offset X
Offset Y
Live Update
Save
Reset
```

The current persistence pipeline is:

```text
scene_transform.json
        │
        ▼
calibration_loader
        │
        ▼
KartSimDT calibration properties
        │
        ▼
KartSimDT UI
        │
        ▼
Live Update
        │
        ▼
Orthophoto object
        │
        ▼
Save
        │
        ▼
scene_transform.json
```

The UI properties must be initialized from the saved scene transformation.

Otherwise default UI values such as:

```text
Scale    = 1
Rotation = 0
Offset X = 0
Offset Y = 0
```

could overwrite valid saved calibration.

---

# 13. Calibration Persistence

Calibration must survive Blender restart and engineering scene rebuild.

Expected sequence:

```text
Blender starts
      │
      ▼
KartSimDT addon registers
      │
      ▼
calibration_loader registers load handler
      │
      ▼
scene.blend loads
      │
      ▼
scene_transform.json is read
      │
      ▼
KartSimDT properties are restored
      │
      ▼
UI displays saved values
```

The loader must not depend on accessing restricted Blender context during
addon registration.

Scene-dependent loading must occur only when a valid scene context and scene
file are available.

---

# 14. Calibration Rules

Use the following order when aligning a track:

```text
1. Verify source metric calibration.
2. Verify image orientation.
3. Verify centerline coordinate system.
4. Correct X/Y scene offset if required.
5. Correct rotation only if a systematic angular error exists.
6. Correct scale only if an actual metric scale error is demonstrated.
```

Do not use scale as the first method of correcting visual mismatch.

Once Orthophoto metric calibration has been verified, keep:

```text
Scale = 1.0
```

unless independent measurements prove that the metric scale is wrong.

A centerline mismatch does not automatically mean the Orthophoto scale is
incorrect.

---

# 15. Alignment Validation

Never validate alignment using only one point on the circuit.

Check multiple distant locations.

Recommended reference areas include:

```text
start / finish straight
opposite side of the circuit
major corner
far end of the circuit
another geometrically distinctive corner
```

Interpret errors systematically.

If the complete track is shifted by approximately the same amount:

```text
→ inspect X/Y offset
```

If error increases with angular direction:

```text
→ inspect rotation
```

If one location matches but distance error grows systematically with
distance:

```text
→ investigate metric scale
```

Do not change calibration parameters without identifying the type of error.

---

# 16. Blender Engineering Scene

Working scene:

```text
data/tracks/<track_name>/blender/scene.blend
```

The scene is a generated / working engineering artifact.

It must not become the authoritative source of original measurements.

The engineering scene is built using:

```text
blender/builders/build_engineering_scene.py
```

Current major inputs are:

```text
google_earth/calibration.json
centerline.json
blender/scene_transform.json
```

Conceptually:

```text
google_earth/calibration.json
            │
            ▼
       Orthophoto
            │
            ├──────────────┐
            │              │
scene_transform.json       │
                           ▼
                    Engineering Scene
                           ▲
scene_transform.json       │
            │              │
            ├──────────────┘
            │
       TrackSurvey
            ▲
            │
     centerline.json
```

---

# 17. New Track Setup Workflow

## Phase A — Create Track Root

Create:

```text
data/tracks/<track_name>/
```

Then create the required input directories.

Minimum current structure:

```text
<track_name>/
├── google_earth/
└── blender/
```

Add `survey/` when raw survey data exists.

Do not copy numerical calibration values from another track.

---

## Phase B — Add Source Imagery

```text
[ ] Add Google Earth reference image
[ ] Preserve the exact source image
[ ] Record source image filename
[ ] Establish X reference measurement
[ ] Establish Y reference measurement
[ ] Preserve calibration reference information
```

The calibration must always be traceable to its source image.

---

## Phase C — Metric Orthophoto Calibration

```text
[ ] Determine image width in pixels
[ ] Determine image height in pixels
[ ] Calculate metres/pixel X
[ ] Calculate metres/pixel Y
[ ] Calculate physical image width
[ ] Calculate physical image height
[ ] Save google_earth/calibration.json
[ ] Import Orthophoto
[ ] Verify Blender dimensions
[ ] Verify object scale is 1.0 after metric construction
```

---

## Phase D — Add Track Survey Data

```text
[ ] Store raw KML/GPS/survey source
[ ] Preserve original source
[ ] Convert source into KartSimDT coordinates
[ ] Generate centerline.json
[ ] Verify point count
[ ] Verify XYZ data
[ ] Import TrackSurvey
```

Do not manually edit the canonical centerline simply to make it fit the
Orthophoto.

---

## Phase E — Build Engineering Scene

```text
[ ] Build/open engineering scene
[ ] Verify Orthophoto is present
[ ] Verify Orthophoto physical dimensions
[ ] Verify TrackSurvey is present
[ ] Verify expected point count
[ ] Verify basic XY correspondence
```

---

## Phase F — Scene Alignment

Start with:

```text
Orthophoto Scale = 1.0
Rotation          = 0
```

Then:

```text
[ ] Adjust Offset X if required
[ ] Adjust Offset Y if required
[ ] Check distant reference locations
[ ] Adjust Rotation only if required
[ ] Recheck complete circuit
[ ] Change Scale only if metric error is proven
[ ] Save scene calibration
```

---

## Phase G — Persistence Test

After saving calibration:

```text
[ ] Inspect scene_transform.json
[ ] Verify orthophoto section
[ ] Verify track_centerline section was preserved
[ ] Close Blender completely
[ ] Rebuild/reopen engineering scene
[ ] Verify KartSimDT UI values are restored
[ ] Verify Orthophoto position is restored
[ ] Verify TrackSurvey alignment is restored
[ ] Verify no calibration data was reset to defaults
```

A track calibration is not complete until this test passes.

---

## Phase H — Track Baseline Validation

Before accepting the track baseline:

```text
[ ] Verify multiple locations around the complete track
[ ] Verify physical dimensions
[ ] Verify canonical centerline
[ ] Verify scene persistence
[ ] Verify reproducible scene build
[ ] Run code quality checks
[ ] Run relevant tests
[ ] Commit the calibrated baseline
```

---

# 18. Project Validation

Formatting and automatic fixes:

```bash
black .
ruff check . --fix
```

Final static validation:

```bash
ruff check .
mypy src
```

Run the relevant project tests before committing.

The final validation should be performed after automatic formatting/fixes so
the committed state is the state that was actually checked.

---

# 19. Track Baseline

Once calibration and persistence have been verified, the resulting track
state becomes the calibrated baseline.

After that point:

- do not casually modify Orthophoto metric calibration;
- do not manually move canonical source geometry;
- do not compensate geometry problems with arbitrary scale changes;
- record intentional transformation changes;
- keep source data reproducible.

Further work should build on the verified baseline.

Examples:

```text
track width
track boundaries
elevation
surface
kerbs
run-off areas
barriers
racing line
telemetry comparison
vehicle simulation
```

---

# 20. Planned Track Manifest

A future track-level manifest should provide one official runtime entry
point for a track.

Proposed location:

```text
data/tracks/<track_name>/track.json
```

Example:

```json
{
    "id": "aukstadvaris",
    "name": "Aukštadvaris",
    "coordinate_system": "local_metric",
    "inputs": {
        "orthophoto": "google_earth/calibration.json",
        "centerline": "centerline.json"
    },
    "scene": {
        "transform": "blender/scene_transform.json"
    }
}
```

Status:

```text
PLANNED — not yet the authoritative runtime implementation.
```

The current implementation still contains track-specific paths.

Those paths should eventually be replaced by manifest-driven track
selection.

The intended future call chain is:

```text
track.json
    │
    ├── source/calibration paths
    ├── canonical geometry paths
    └── scene transformation path
             │
             ▼
       KartSimDT pipeline
```

This will allow a new track to be selected without modifying Python source
code.

---

# 21. Future Input Architecture

The intended long-term architecture is:

```text
                   ┌── Google Earth
                   │
                   ├── KML / survey
                   │
                   ├── MyChron / GPS
                   │
TRACK INPUTS ──────┼── LiDAR / SLAM
                   │
                   └── Video
                         │
                         ▼
                IMPORT / CALIBRATION
                   / NORMALIZATION
                         │
                         ▼
               KARTSIMDT CANONICAL DATA
                         │
              ┌──────────┴───────────┐
              │                      │
              ▼                      ▼
       BLENDER ENGINEERING      SIMULATION /
             MODEL               VALIDATION
              │                      │
              └──────────┬───────────┘
                         ▼
                DIGITAL TRACK MODEL
```

New source formats should normally add a new importer/converter rather than
change the canonical Blender pipeline.

---

# 22. New Track Data Entry Summary

For a completely new track, the intended entry path is:

```text
NEW TRACK
   │
   ▼
data/tracks/<track_name>/
   │
   ├── google_earth/
   │       ├── source image
   │       └── calibration.json
   │
   ├── survey/
   │       └── raw KML/GPS/survey
   │
   ├── telemetry/        [optional / future]
   ├── lidar/            [optional / future]
   └── video/            [optional / future]
           │
           ▼
     NORMALIZATION
           │
           ▼
     centerline.json
           │
           ▼
  ENGINEERING SCENE
           │
           ├── Orthophoto
           ├── TrackSurvey
           └── scene_transform.json
                    │
                    ▼
             VALIDATED BASELINE
```

The long-term goal is for `track.json` to become the single formal entry
point that connects all these datasets.

---

# 23. Reference Implementation

Current reference:

```text
Track:
Aukštadvaris

Orthophoto calibration:
X reference = 200.32 m
Y reference = 200.04 m

Image:
8192 × 5125 px

Metric resolution:
X = 0.06461674 m/px
Y = 0.06448964 m/px

Physical Orthophoto:
529.340 × 330.509 m

Canonical TrackSurvey:
677 points
```

Aukštadvaris should be used to verify that future changes to the import,
calibration, Blender, or persistence pipeline do not break an already
validated track.

---

# 24. Definition of Done for a New Track

A new track is considered successfully integrated when:

```text
[ ] Raw source data has defined entry points
[ ] Source imagery is preserved
[ ] Orthophoto metric calibration is reproducible
[ ] X and Y calibration are independently defined
[ ] Physical Orthophoto dimensions are verified
[ ] Canonical centerline.json exists
[ ] TrackSurvey imports correctly
[ ] Engineering scene builds successfully
[ ] Orthophoto and TrackSurvey align
[ ] Scene transformation is stored separately from source calibration
[ ] Save preserves unrelated transformation sections
[ ] Calibration survives Blender restart
[ ] Engineering scene can be rebuilt
[ ] Multiple track locations have been visually validated
[ ] Static checks pass
[ ] Relevant tests pass
[ ] Calibrated baseline is committed
```

Only after this baseline is established should work proceed to detailed
track geometry, elevation, surface construction, telemetry validation, or
simulation.