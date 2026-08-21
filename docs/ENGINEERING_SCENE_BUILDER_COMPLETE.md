# Engineering Scene Builder — COMPLETE

## Status

**Status:** COMPLETE  
**Scope:** Deterministic generation and restoration of the Blender Engineering Scene skeleton from canonical track data.

## IN — Input

The Engineering Scene Builder takes the selected track directory as its canonical input source:

```text
data/
└── tracks/
    └── <track-name>/
```

For the validated track:

```text
data/tracks/Aukštadvaris/
```

Consumed track data:

```text
data/tracks/<track-name>/
├── centerline.json
├── design/
│   └── track_design.yaml
└── blender/
    └── scene_transform.json
```

Orthophoto and other survey resources are consumed through the existing `TrackContext` and importers.

### Canonical 3D centerline

`centerline.json` is the canonical local 3D centerline source containing X, Y, Z elevation, point indices and geometry metadata.

The source elevation profile is preserved. Blender scene transforms do not overwrite the source centerline.

### Track design

`design/track_design.yaml` contains engineering parameters used by the road generator.

Current validated Aukštadvaris design includes:

- default road width: 8.0 m;
- Start/Finish width zone: indices 640–676, width 11.0 m;
- Start/Finish centerline index: 662;
- straight length: 105.36 m;
- terrain enabled;
- kerbs/runoff/objects currently empty.

### Blender scene transform

`blender/scene_transform.json` contains visualization calibration:

- orthophoto scale, rotation and XY offset;
- TrackSurvey scale, rotation and XY offset;
- TrackSurvey Z offset.

For the validated Aukštadvaris scene:

```json
"track_centerline": {
    "scale": 1.0,
    "rotation_deg": 0.0,
    "offset_x": 0.0,
    "offset_y": 0.0,
    "offset_z": 1.440323
}
```

The Z offset is a scene/reference transform and does not modify `centerline.json`.

## PROCESS

The builder performs this deterministic pipeline:

```text
TrackContext
    |
    +--> cleanup generated scene objects
    |
    +--> import orthophoto
    |
    +--> import 3D TrackSurvey
    |
    +--> load TrackDesign
    |
    +--> generate TrackRoad
    |
    +--> apply/validate scene transforms
    |
    +--> save scene
    |
    v
data/tracks/<track-name>/blender/scene.blend
```

### 1. Cleanup

Previously generated KartSimDT objects are removed while persistent Blender infrastructure such as Camera and Light is preserved.

### 2. Orthophoto

The existing orthophoto importer creates the `Orthophoto` scene object using the track calibration data.

### 3. TrackSurvey

The canonical `centerline.json` is imported as the Blender `TrackSurvey` object.

The configured scene transform is applied.

### 4. TrackDesign

`track_design.yaml` is loaded into the domain `TrackDesign` model.

Blender does not define engineering parameters; it consumes the domain data.

### 5. TrackRoad

`TrackRoadGenerator` consumes the transformed `TrackSurvey` and `TrackDesign`.

The road is generated through:

```text
RoadWidthResolver
        |
RoadGeometryGenerator
        |
BlenderRoadWriter
```

The resulting Blender object is:

```text
TrackRoad
```

### 6. Validation

For the validated Aukštadvaris track:

```text
Source centerline:
    min Z = -1.440323 m
    max Z =  3.991821 m

Engineering scene:
    min Z = 0.000000 m
    max Z = 5.432144 m
```

The elevation profile is preserved; the Blender scene reference is shifted by `+1.440323 m`.

### 7. Save

The generated scene is saved to:

```text
data/tracks/<track-name>/blender/scene.blend
```

For Aukštadvaris:

```text
data/tracks/Aukštadvaris/blender/scene.blend
```

## OUT — Output

Primary output:

```text
data/tracks/<track-name>/blender/scene.blend
```

`scene.blend` is a **generated visualization artifact**, not the canonical engineering-data store.

Canonical track data remains under:

```text
data/tracks/<track-name>/
```

Therefore the Blender scene can be deleted and rebuilt from the track data.

## Rebuild Contract

The completed stage must support:

```text
DELETE scene.blend
        |
        v
BUILD
        |
        v
SAVE
        |
        v
scene.blend
        |
        v
OPEN / RESTORE
```

The rebuilt scene must reproduce the Engineering Scene skeleton from the same track data and calibration.

This is the key platform capability established by this stage.

## Architecture Boundary

Blender is a visualization/application layer.

It is not the canonical Track data store and it is not KartSimDT Core.

Dependency direction:

```text
Track / Survey / Geometry / Design
                |
                v
      Engineering Scene Builder
                |
                v
             Blender
```

Therefore:

- canonical data lives in `data/tracks/<track-name>/`;
- engineering calculations remain in KartSimDT Core/domain modules;
- Blender consumes generated geometry and visualization data;
- `scene.blend` is reproducible output.

## Quality Gate

The following checks pass:

```text
ruff check . --fix    PASS
mypy src              PASS
pytest                PASS
```

`mypy` currently uses:

```toml
ignore_missing_imports = true
```

because Blender's `bpy` module is supplied by the Blender runtime rather than the project `.venv`.

## Completed Scope

- [x] Track data as scene input
- [x] 3D centerline import
- [x] Elevation preservation
- [x] Orthophoto import
- [x] XY calibration
- [x] Z scene calibration
- [x] TrackDesign loading
- [x] Variable road width
- [x] TrackRoad generation
- [x] Generated-object cleanup
- [x] Engineering Scene rebuild
- [x] Scene save
- [x] Scene restore
- [x] Ruff
- [x] MyPy
- [x] Pytest

## Next Scope

The next visual layers can be added incrementally:

1. Start/Finish geometry and zone
2. Kerbs
3. Terrain
4. Runoff
5. Track-side objects
6. Protective tyre barriers
7. Additional track structures

Each layer should follow:

```text
track data
    ->
domain calculation / generator
    ->
visualization adapter
    ->
scene object
    ->
saved scene
```
