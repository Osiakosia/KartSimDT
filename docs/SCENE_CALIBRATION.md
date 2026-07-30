# Engineering Calibration

## Purpose

Engineering Calibration establishes the spatial relationship between real-world survey data and the engineering scene used by KartSimDT.

Calibration is performed once for each track and becomes the reference for all subsequent geometry generation.

---

# Philosophy

KartSimDT does not generate geometry directly from Blender.

Blender is used only as an engineering calibration environment.

Its responsibility is to align independent data sources into a common engineering reference frame.

After calibration, Blender exports only the transformation parameters required by the platform.

---

# Calibration Pipeline

```text
Google Earth KML
        │
        ▼
TrackSurveySession
        │
        ▼
CenterlineGeometry
        │
        ▼
centerline.json
        │
        ▼
Blender Engineering Scene
        │
        ▼
Engineering Calibration
        │
        ▼
calibration.json
```

---

# Calibration Objects

The engineering scene currently contains three independent objects.

## Orthophoto

Reference aerial imagery.

Purpose:

- visual reference
- scale validation

---

## Reference Track Survey

Centerline reconstructed from Google Earth.

Purpose:

- reference geometry
- engineering baseline

---

## Walkthrough Track Survey

Centerline collected during on-site walkthrough.

Purpose:

- local geometric correction
- validation of real measurements

---

# Calibration Output

The result of calibration is not a Blender scene.

The result is a platform calibration file.

```text
calibration.json
```

The file stores engineering transforms required by the platform.

Example:

```json
{
    "orthophoto": {
        "scale": 0.9987
    },

    "track_surveys": {
        "reference": {
            "scale": 1.000,
            "rotation_deg": -1.25,
            "offset_x": 124.36,
            "offset_y": -41.82,
            "offset_z": 0.0
        },

        "walkthrough": {
            "scale": 0.999,
            "rotation_deg": -1.08,
            "offset_x": 124.18,
            "offset_y": -41.67,
            "offset_z": 0.0
        }
    }
}
```

---

# Platform Rule

Calibration data belongs to the KartSimDT platform.

Blender is only responsible for producing calibration parameters.

Geometry generators never read Blender scenes.

They use:

- TrackSurveySession
- calibration.json

---

# Future Pipeline

Once calibration is complete, all geometry generators operate from the same engineering reference.

```text
TrackSurveySession
        │
        ├──────────────┐
        │              │
        ▼              ▼
Terrain        Kerbs
        │              │
        └──────┬───────┘
               ▼
         Track Mesh
               │
               ▼
         Digital Twin
```

---

# Engineering Principle

Calibration is performed once.

All subsequent geometry generation must reuse the exported calibration.

No generator should require manual alignment inside Blender.

# Philosophy 

Blender is an engineering calibration tool, 
not the source of truth. The source of truth 
is the KartSimDT platform (TrackSurveySession and future 
domain sessions).