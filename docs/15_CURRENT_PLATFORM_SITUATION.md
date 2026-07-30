# KartSimDT Platform

## Current Platform Architecture (Interim)

---

# Purpose

KartSimDT is a geometry platform whose purpose is to transform various raw track survey sources into a single, unified track model.

The platform is independent of Blender, Unreal Engine, Unity, or any other visualization system.

Visualization systems are consumers of the platform, not the owners of the geometry.

---

# Core Architecture Rule

> **TrackSurvey is the single source of geometric truth within the platform.**

Every subsystem operates on the TrackSurvey model.

No subsystem should directly depend on:

- KML
- GPX
- Blender
- Google Earth
- JSON exports

These formats are only transport mechanisms.

---

# Platform Pipeline

```text
                 Readers
        ┌─────────┼──────────┐
        │         │          │
      KML       GPX        CSV
        │         │          │
        └─────────┴──────────┘
                  │
                  ▼
          TrackSurveyRawData
                  │
                  ▼
             Validator
                  │
                  ▼
               Mapper
                  │
                  ▼
         TrackSurveySession
                  │
                  ▼
          Geometry Mapper
                  │
                  ▼
        Centerline Geometry
                  │
      ┌───────────┼─────────────┐
      │           │             │
      ▼           ▼             ▼
   Blender     Exporters    Generators
```

---

# Readers

Readers are responsible only for reading external data sources.

Examples:

- KmlReader
- GpxReader
- CsvReader

Readers never generate geometry.

Their only responsibility is creating:

```text
TrackSurveyRawData
```

---

# Validator

The validator verifies that raw survey data is valid.

Examples:

- coordinates exist
- minimum point count
- valid geometry
- valid metadata

---

# Mapper

The mapper converts validated survey data into the platform domain model.

```text
TrackSurveyRawData
        │
        ▼
TrackSurveySession
```

TrackSurveySession is the canonical representation of a surveyed track.

---

# Geometry Mapper

The Geometry Mapper converts TrackSurveySession into geometric objects.

```text
TrackSurveySession
        │
        ▼
CenterlineGeometry
```

From this point onward the platform operates on geometry instead of raw GPS coordinates.

---

# Blender

Blender is **not** a geometry source.

Blender is a

- visualization tool
- calibration tool

Its responsibilities are:

- display imported geometry
- compare multiple datasets
- allow manual alignment
- export calibration transforms

Blender never owns the data.

---

# Blender Operators

Operators export user adjustments.

For example:

```text
scene_transform.json
```

Operators never generate TrackSurvey data.

---

# Exporters

Exporters serialize platform objects into external formats.

Examples:

- JSON
- Blender
- CSV
- Future formats

Exporters do not modify geometry.

---

# Generators

Generators operate on platform geometry.

Examples:

- Terrain Generator
- Kerb Generator
- Track Mesh Generator
- Racing Line Generator
- AI Generator

Generators never read KML or GPX directly.

They always consume platform geometry.

---

# First Complete Platform Pipeline

The first complete working pipeline of KartSimDT is:

```text
KML
 │
 ▼
Reader
 │
 ▼
Validator
 │
 ▼
Mapper
 │
 ▼
TrackSurveySession
 │
 ▼
Geometry Mapper
 │
 ▼
Centerline Geometry
 │
 ▼
Blender Import
 │
 ▼
Scene Calibration
 │
 ▼
scene_transform.json
```

This is the first end-to-end workflow of the platform.

---

# Future Expansion

Once the first pipeline is complete, additional readers can be connected without changing the platform core.

Examples:

- GPX Reader
- RTK GPS Reader
- LiDAR Reader
- Drone Survey Reader

All of them will produce the same TrackSurvey model.

Likewise, new generators can be added independently:

- Terrain Generator
- Kerb Generator
- Track Mesh Generator
- Boundary Generator
- Racing Line Generator
- AI Generator

None of these components should depend on the original survey format.

---

# Platform Philosophy

Raw data enters the platform through Readers.

The platform converts raw data into a unified TrackSurvey model.

Everything else in the ecosystem operates exclusively on TrackSurvey and its derived geometry.

This separation ensures that the geometry core remains independent of file formats, visualization tools, and future simulation systems.