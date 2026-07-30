# 📘 KartSimDT

> **Engineering the Digital Future of Kart Racing**

Telemetry → Track → Vehicle → Physics → Digital Twin → Optimization

**Kart Simulation Digital Twin Toolkit**

An open engineering and research platform for transforming real-world kart racing telemetry into validated Digital Twins for simulation, analysis, optimization, and scientific research.

---

# 🎯 Project Vision

KartSimDT is an engineering platform designed to reconstruct real kart racing circuits using telemetry, geospatial data, and physics-based simulation.

The project combines software engineering, telemetry analysis, computational geometry, and vehicle dynamics into a unified Digital Twin platform.

The long-term objective is to create reproducible and validated digital representations of kart tracks that support engineering research, simulation, and performance optimization.

---

# 🏗 Platform Architecture

```
                    KartSimDT

              Engineering Platform

                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   Import Layer    Core Domain    Applications
        │               │               │
        ▼               ▼               ▼
 Telemetry       Digital Twin      Blender
 GIS             Physics           Assetto Corsa
 Images          Simulation        Research
```

---

# ✨ Main Features

## 📡 Telemetry

- AIM Sports telemetry import
- Automatic lap detection
- Channel validation
- Session analysis
- Multi-session comparison

---

## 🗺 Track Reconstruction

- Google Earth KML import
- Orthophoto import
- Centerline reconstruction
- Elevation reconstruction
- 3D track generation

---

## 🚗 Digital Twin

- Complete digital track model
- Modular architecture
- Vehicle models
- Physics-based simulation

---

## 📈 Optimization

- Racing line optimization
- Driver comparison
- Corner analysis
- AI-assisted research

---

## 📂 Reference Data

- AIM telemetry
- Google Earth KML
- Orthophotos
- Validation datasets
- Reference tracks

---

## 📤 Export

- Blender
- Unity
- CSV
- KML
- Future simulation formats

---

# 📊 Current Development Status

| Module | Status |
|----------|:------:|
| Documentation | 🟢 |
| Project Architecture | 🟢 |
| AIM CSV Reader | 🟢 |
| AIM Validator | 🟢 |
| AIM Channel Mapper | 🟡 |
| Telemetry Domain | ⚪ |
| Track Reconstruction | ⚪ |
| Physics Engine | ⚪ |
| Digital Twin | ⚪ |

---

# 🛣 Development Roadmap

| Version | Status | Description |
|----------|:------:|-------------|
| v0.1 | 🟢 | Project foundation |
| v0.2 | 🟡 | AIM telemetry import |
| v0.3 | ⚪ | Google Earth KML |
| v0.4 | ⚪ | Track reconstruction |
| v0.5 | ⚪ | Digital Twin Core |
| v0.6 | ⚪ | Vehicle models |
| v0.7 | ⚪ | Physics engine |
| v0.8 | ⚪ | Optimization |
| v0.9 | ⚪ | Validation |
| v1.0 | ⚪ | Research Platform |

---

# ⚙ Technology Stack

## Programming

- Python 3.13+

## Scientific Computing

- NumPy
- Pandas
- SciPy
- Matplotlib

## GIS & Geometry

- Shapely
- PyProj
- lxml

## Computer Vision

- OpenCV

## Development

- black
- ruff
- mypy
- pytest
- pre-commit

---

# 📁 Repository Structure

```
KartSimDT/

docs/
data/
examples/
tests/

src/
└── kartsimdt/
    ├── core/
    ├── io/
    ├── telemetry/
    ├── geometry/
    ├── track/
    ├── terrain/
    ├── vehicle/
    ├── simulation/
    ├── optimization/
    ├── adapters/
    └── utils/
```
# Geometry Philosophy

> **Single Source of Geometric Truth**

---

## Purpose

KartSimDT is built around a single engineering principle:

> **TrackSurveySession is the single source of geometric truth within the platform.**

Every engineering subsystem shall consume the TrackSurvey domain model rather than raw external data.

This separation keeps the platform independent from file formats, visualization tools and simulation backends.

---

# Engineering Principle

External engineering data are considered **transport formats**, not platform objects.

Examples include:

- Google Earth KML
- GPX
- CSV
- Orthophotos
- Blender scenes
- JSON exchange files

These files are only used to construct the TrackSurvey domain model.

Once imported, every subsequent platform module operates exclusively on TrackSurvey.

---

# Geometry Flow

```text
External Engineering Data

    Google Earth
    GPX
    RTK GPS
    Drone
    LiDAR
    Orthophotos

            │
            ▼

          Readers

            │
            ▼

     TrackSurveySession
    (Single Source of Truth)

            │
            ▼

     Geometry Components

            │
     ┌──────┼──────────────┐
     │      │              │
     ▼      ▼              ▼

Visualization   Exporters   Generators
```

---

# Readers

Readers import engineering measurements into the platform.

Examples:

- GoogleEarthKmlReader
- WalkthroughKmlReader
- GpxReader
- LidarReader

Every reader produces the same platform object.

```text
TrackSurveySession
```

Readers never generate geometry.

Readers never depend on Blender.

Readers never perform visualization.

---

# Geometry Components

Geometry components transform TrackSurvey into reusable engineering geometry.

Examples:

- CenterlineGeometry
- TrackBoundaryGeometry
- TerrainGeometry
- SurfaceGeometry

These objects become the engineering foundation used by every downstream subsystem.

---

# Visualization

Visualization is a consumer of platform geometry.

Visualization systems include:

- Blender
- Unreal Engine
- Assetto Corsa
- Future simulation platforms

Visualization never owns the engineering model.

Its responsibilities are limited to:

- displaying geometry
- engineering inspection
- calibration
- scene export

---

# Blender

Within KartSimDT, Blender is an engineering application.

It is used for:

- visual validation
- orthophoto alignment
- engineering calibration
- scene inspection

Blender never reconstructs TrackSurvey.

Blender only visualizes existing platform geometry.

---

# Calibration

Engineering calibration is performed inside Blender.

The result is exported as calibration parameters.

Example:

```text
scene_transform.json
```

Calibration modifies visualization parameters.

It never modifies the original TrackSurveySession.

---

# Generators

Generators consume platform geometry.

Examples:

- Terrain Generator
- Kerb Generator
- Track Mesh Generator
- Racing Line Generator
- Digital Twin Generator

Generators never read KML or GPX directly.

Their only geometric input is the platform model.

---

# Platform Independence

The geometry core remains completely independent from:

- Blender
- Assetto Corsa
- Unity
- Unreal Engine
- Export formats

New visualization systems can be connected without changing the TrackSurvey domain model.

Likewise, new Readers can be added without modifying existing generators.

---

# Engineering Rule

The following rule shall guide every future architecture decision.

> **If a new subsystem needs to read KML, GPX, Orthophotos or Blender files directly, the architecture should be reconsidered.**

The correct workflow is:

```text
External Data
      │
      ▼
Reader
      │
      ▼
TrackSurveySession
      │
      ▼
Platform Geometry
      │
      ▼
Visualization / Export / Generation
```

TrackSurvey remains the only geometric source of truth throughout the KartSimDT platform.
---

# 🔄 Development Workflow

Every engineering task follows the same workflow.

```
Plan
    │
    ▼
Architecture
    │
    ▼
Implementation
    │
    ▼
black
    │
    ▼
ruff
    │
    ▼
mypy
    │
    ▼
pytest
    │
    ▼
Documentation
    │
    ▼
Git Commit
```

---

# 🌳 Branch Strategy

```
KartSimDT
      │
      ├──────────────┐
      │              │
      ▼              ▼
    Main         Applied
      │              │
      ▼              ▼
 Stable Core   Engineering Validation
                     │
                     ▼
              Assetto Corsa
```

The **Applied** branch continuously validates the Core architecture using real engineering demonstrators.

---

# 📚 Documentation

Project documentation is located in the `docs/` directory.

| Document | Description |
|----------|-------------|
| 📘 Style Guide | Engineering standards |
| 🏗 Architecture | System architecture |
| 🛣 Roadmap | Development roadmap |
| 📈 Development | Current project status |
| 📑 Design Decisions | Architecture decisions |
| 📥 AIM Import | AIM telemetry specification |

---

# 💡 Project Philosophy

KartSimDT is developed according to engineering-first principles.

- Architecture before implementation
- Validation before assumptions
- Physics before visualization
- Digital Twins built from reality

---

# 📄 License

Distributed under the MIT License.

---

# 🚧 Project Status

KartSimDT is under active development.

The current focus is building a robust engineering foundation before expanding into full Digital Twin simulation and optimization.

---

> **Engineering the Digital Future of Kart Racing**