# 🛰️ Track Survey Foundation

> **Engineering the Physical World into the Digital Twin**

---

# Purpose

Track Survey Foundation defines the engineering methodology used to measure, document, validate and reconstruct real kart racing circuits.

Unlike Telemetry Foundation, which captures vehicle behaviour during a driving session, Track Survey Foundation captures the physical characteristics of the racing circuit.

The primary output of this milestone is the `TrackSurveySession` platform object.

---

# Vision

Every Digital Twin begins with the real world.

The objective of Track Survey Foundation is to transform field measurements into reproducible engineering data.

All subsequent platform modules depend on the quality of these measurements.

```
Real Track
      │
      ▼
Track Survey
      │
      ▼
TrackSurveySession
      │
      ▼
Track Geometry
      │
      ▼
Track Model
      │
      ▼
Digital Twin
```

---

# Objectives

Track Survey Foundation shall provide:

- reproducible engineering field measurements
- validated GPS trajectories
- validated track centerline
- engineering reference points
- georeferenced photographs
- survey metadata
- engineering documentation

---

# Platform Position

Track Survey Foundation is the second engineering milestone of KartSimDT.

```
Telemetry Foundation
        │
        ▼
Track Survey Foundation
        │
        ▼
Track Reconstruction
        │
        ▼
Digital Twin
```

Telemetry describes **how the vehicle moved**.

Track Survey describes **where the vehicle moved**.

Together they become the foundation of the Digital Twin.

---

# Platform Object

## TrackSurveySession

The TrackSurveySession represents one complete engineering survey of a racing circuit.

```
TrackSurveySession

├── metadata
├── gps_track
├── centerline
├── critical_points
├── photos
├── notes
├── attachments
└── validation
```

---

# Survey Data Model

The Track Survey Foundation introduces the following engineering objects.

```
SurveyMetadata

SurveyPoint

CriticalPoint

PhotoReference

GpsTrack

Centerline

TrackSurveySession
```

Each object should be independently testable and reusable.

---

# Field Survey Methodology

All measurements shall follow a reproducible engineering workflow.

```
Preparation
      │
      ▼
GPS Logger
      │
      ▼
Centerline Recording
      │
      ▼
Critical Point Survey
      │
      ▼
GPS Photographs
      │
      ▼
Survey Notes
      │
      ▼
Validation
      │
      ▼
TrackSurveySession
```

Every completed survey must be reproducible by another engineer.

---

# Survey Equipment

Current equipment:

- Android smartphone
- GPS Logger
- GPS Mapper
- GPS Camera
- Critical Point Checklist
- Portable Power Bank

Future equipment:

- RTK GPS
- Drone
- LiDAR
- Laser Distance Meter
- 360 Camera
- Photogrammetry

The survey methodology shall remain compatible with future equipment upgrades.

---

# Survey Data Sources

TrackSurveySession may contain data collected from multiple sources.

Supported sources include:

- GPX tracks
- KML files
- GPS photographs
- Critical point measurements
- Centerline recordings
- Google Earth
- Orthophotos
- Survey notes

Future sources:

- Drone imagery
- LiDAR
- RTK measurements
- Satellite imagery

---

# Development Roadmap

## Phase 1

Domain Model

- SurveyMetadata
- SurveyPoint
- CriticalPoint
- PhotoReference
- TrackSurveySession

---

## Phase 2

Survey Readers

- GPX Reader
- KML Reader
- GPS Photo Reader

---

## Phase 3

Validation

- Coordinate validation
- GPS validation
- Critical point validation
- Photo validation

---

## Phase 4

Centerline

- Import
- Cleaning
- Simplification
- Validation

---

## Phase 5

Engineering Tools

- inspect_track_survey.py
- acceptance_track_foundation.py

---

## Phase 6

Integration

TrackSurveySession becomes the reference geometry for:

- Track Reconstruction
- Terrain Reconstruction
- Replay
- Ghost Kart
- Drone Coach
- SimCoach
- Digital Twin

---

# Engineering Workflow

Every platform object follows the same engineering lifecycle.

```
Domain Model
      │
      ▼
Readers
      │
      ▼
Validation
      │
      ▼
Platform Object
      │
      ▼
Engineering Inspector
      │
      ▼
Engineering Acceptance Report
      │
      ▼
Documentation
      │
      ▼
Milestone Complete
```

This workflow was established during Telemetry Foundation and shall be applied throughout the KartSimDT platform.

---

# Engineering Tools

Development tools for this milestone:

```
inspect_track_survey.py

acceptance_track_foundation.py
```

These tools provide engineering diagnostics and milestone acceptance validation.

---

# Future Research

Future investigations include:

- AI-assisted centerline generation
- Automatic critical point detection
- RTK GPS integration
- Drone-assisted surveying
- Photogrammetry
- LiDAR reconstruction
- Surface modelling
- Elevation reconstruction
- Terrain generation

---

# Milestone Acceptance

Track Survey Foundation is considered complete when:

- TrackSurveySession implemented
- Survey readers implemented
- Validation complete
- Centerline validation complete
- Engineering Inspector complete
- Engineering Acceptance Report complete
- Documentation complete
- Quality gates passed

---

# Expected Outcome

The completed Track Survey Foundation provides a validated engineering representation of a real racing circuit.

It becomes the primary geometric reference for every subsequent KartSimDT platform module and establishes the physical foundation required for accurate Digital Twin reconstruction.

---------------------------------------------------------------------------
---------------------------------------------------------------------------

# Part II — Technical Specification

This section defines the implementation architecture of the Track Survey Foundation.

It describes the software modules, development phases, engineering validation and milestone progress.

---

# Module Structure

```text
survey/
└── track_survey/
    ├── __init__.py
    ├── parser.py
    ├── reader.py
    ├── validator.py
    ├── mapper.py
    ├── metadata.py
    ├── gps_track.py
    ├── centerline.py
    ├── critical_points.py
    ├── photos.py
    ├── notes.py
    ├── session.py
    ├── constants.py
    └── exceptions.py
```

---

# Module Responsibilities

## parser.py

Coordinates the complete Track Survey pipeline.

---

## reader.py

Reads GPX, KML and future survey sources.

---

## validator.py

Validates:

- GPS data
- Coordinates
- Centerline
- Critical points
- Metadata

---

## mapper.py

Maps survey data into:

- TrackSurveySession
- SurveyMetadata
- GpsTrack
- Centerline
- CriticalPointCollection
- PhotoCollection

---

## session.py

Defines the TrackSurveySession platform object.

---

# Track Survey Pipeline

```text
Field Survey
      │
      ▼
Reader
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
```

---

# Development Tasks

## Sprint 3.1 — Module Foundation

Tasks:

- [+] Create `reader.py`
- [+] Create `validator.py`
- [+] Create `mapper.py`
- [+] Create `metadata.py`
- [ ] Create `gps_track.py` (pending)
- [+] Create `centerline.py`
- [ ] Create `critical_points.py`( pending)
- [ ] Create `photos.py` (pending)
- [ ] Create `notes.py`  (pending)
- [ ] Create `session.py` 
- [+] Create `constants.py`
- [+] Create `exceptions.py`
- [ ] Create `parser.py`

---

## Sprint 3.2 — Survey Readers

Tasks:

- [ ] GPX Reader
- [ ] KML Reader
- [ ] GPS Photo Reader
- [ ] TrackSurveyRawData
- [ ] Unit tests

---

## Sprint 3.3 — Validation

Tasks:

- [ ] GPS validation
- [ ] Coordinate validation
- [ ] Centerline validation
- [ ] Critical point validation
- [ ] Metadata validation
- [ ] Unit tests

---

## Sprint 3.4 — Mapping

Tasks:

- [ ] Build TrackSurveySession
- [ ] Map GPS tracks
- [ ] Map centerline
- [ ] Map critical points
- [ ] Map photos
- [ ] Integration tests

---

## Sprint 3.5 — Engineering

Tasks:

- [ ] Create `inspect_track_survey.py`
- [ ] Create engineering report
- [ ] Create acceptance report
- [ ] Validate reference datasets

---

## Sprint 3.6 — End-to-End Integration

Tasks:

- [ ] Complete Track Survey pipeline
- [ ] Acceptance tests
- [ ] Platform integration


---

# Progress

| Sprint | Description | Status |
|---------|-------------|:------:|
| 3.1 | Module Foundation | ⚪ |
| 3.2 | Survey Readers | ⚪ |
| 3.3 | Validation | ⚪ |
| 3.4 | Mapping | ⚪ |
| 3.5 | Engineering Tools | ⚪ |
| 3.6 | End-to-End Integration | ⚪ |

---

# Definition of Done

```text
Field Survey
      │
      ▼
Reader
      │
      ▼
TrackSurveyRawData
      │
      ▼
Validator
      │
      ▼
Mapper
      ├── Metadata        ✓
      ├── GPS Track       ✓
      ├── Centerline      ✓
      ├── Critical Points ✓
      ├── Photos          ✓
      └── Notes           ✓
      │
      ▼
TrackSurveySession
```

Track Survey Foundation v1.0 completed.

---

# Summary

The Track Survey subsystem provides the engineering foundation for reconstructing real kart racing circuits.

Its responsibility is to transform field measurements into the common `TrackSurveySession` domain model while remaining independent from later geometry reconstruction, replay and Digital Twin modules.

-------------------------------------------------------------------
-------------------------------------------------------------------
# Visualization Layer

## Goal

Transform the Track Survey domain model into engineering-grade visual
representations.

The first visualization backend is **Blender**.

Future visualization targets include:

- Blender
- Unreal Engine
- Assetto Corsa
- Other simulation platforms

---

## Architecture

```text
TrackSurveySession
        │
        ▼
Visualization Layer
        │
        ├── Coordinate Transform
        ├── Curve Generation
        ├── Mesh Generation
        ├── Terrain Generation
        └── Scene Export
```

---

## Input

```text
TrackSurveySession
```

Contains:

- Survey metadata
- Track centerline
- GPS coordinates

---

## Output

Visualization scene.

Example:

```text
Blender Scene

├── Curve
├── Road Mesh
├── Terrain
├── Materials
└── Scene Objects
```

---

## Responsibilities

The Visualization layer is responsible for:

- coordinate transformation
- local coordinate system
- curve generation
- road mesh generation
- terrain generation
- scene export

The Visualization layer does **not**:

- read KML files
- validate survey data
- map survey objects
- reconstruct telemetry

Those responsibilities belong to the Track Survey module.

---

## Package Structure

```text
kartsimdt/

    visualization/

        blender/

            __init__.py

            constants.py
            exceptions.py

            coordinate_transform.py

            curve.py
            mesh.py
            terrain.py

            exporter.py
```

---

## Pipeline

```text
Google Earth KML
        │
        ▼
TrackSurveyParser
        │
        ▼
TrackSurveySession
        │
        ▼
Visualization
        │
        ▼
Blender Scene
```

---

## Future Extensions

The Visualization layer is designed to support multiple export targets.

```text
Visualization
        │
        ├── Blender
        ├── Unreal Engine
        ├── Assetto Corsa
        └── Other Platforms
```

The domain model remains independent from the visualization backend.

---

## Development Roadmap

| Sprint | Description |
|---------|-------------|
| 4.1 | Visualization Foundation |
| 4.2 | Curve Generation |
| 4.3 | Road Mesh |
| 4.4 | Terrain |
| 4.5 | Blender Export |
| 4.6 | Engineering Tools |
| 4.7 | End-to-End Integration |

## Sprint 4.1 — Visualization Foundation

Tasks:

- [+] Create Visualization package
- [+] Create Blender package
- [+] Create module structure
- [ ] Create constants
- [ ] Create exceptions
- [ ] Create coordinate transformation utilities

---

## Sprint 4.2 — Curve Generation

Tasks:

- [ ] Create curve model
- [ ] Convert GPS coordinates
- [ ] Generate curve geometry
- [ ] Validate point order
- [ ] Unit tests

---

## Sprint 4.3 — Road Mesh

Tasks:

- [ ] Create road mesh
- [ ] Generate vertices
- [ ] Generate faces
- [ ] Support configurable track width
- [ ] Unit tests

---

## Sprint 4.4 — Terrain

Tasks:

- [ ] Create terrain model
- [ ] Generate terrain plane
- [ ] Orthophoto support
- [ ] Elevation preparation
- [ ] Unit tests

---

## Sprint 4.5 — Blender Export

Tasks:

- [ ] Create Blender exporter
- [ ] Export curve
- [ ] Export road mesh
- [ ] Export terrain
- [ ] Export Blender scene

---

## Sprint 4.6 — Engineering Tools

Tasks:

- [ ] Create Blender inspector
- [ ] Create engineering report
- [ ] Create acceptance report
- [ ] Validate exported scene

---

## Sprint 4.7 — End-to-End Integration

Tasks:

- [ ] Complete visualization pipeline
- [ ] Acceptance tests
- [ ] Platform integration

---

# Progress

| Sprint | Description | Status |
|---------|-------------|:------:|
| 4.1 | Visualization Foundation | ⚪ |
| 4.2 | Curve Generation | ⚪ |
| 4.3 | Road Mesh | ⚪ |
| 4.4 | Terrain | ⚪ |
| 4.5 | Blender Export | ⚪ |
| 4.6 | Engineering Tools | ⚪ |
| 4.7 | End-to-End Integration | ⚪ |

---

