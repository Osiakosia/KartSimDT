# KartSimDT

Telemetry  →  Track  →  Vehicle  →  Physics  →  Digital Twin  →  Optimization

**Kart Simulation Digital Twin Toolkit**

**An open engineering and research platform for creating validated digital twins of kart racing tracks from real telemetry, geospatial data and physics-based simulation.**

---

# Project Vision
The platform is designed around real reference datasets and reproducible engineering workflows.

KartSimDT aims to provide a complete workflow for transforming real-world karting telemetry into accurate digital twins suitable for:

- Track analysis
- Racing line optimization
- Driver performance analysis
- Vehicle simulation
- AI research
- Physics validation
- 3D visualization
- Digital track preservation

The long-term goal is to build a modular research platform capable of reconstructing real kart circuits and simulating vehicle dynamics with high accuracy.

---

# Main Features

## Telemetry

- AIM Sports telemetry import
- Automatic lap detection
- Channel validation
- Telemetry filtering
- Session analysis
- Multi-session comparison

## Track Reconstruction

- Google Earth KML import
- Orthophoto import
- Track centerline reconstruction
- Track width estimation
- Elevation reconstruction
- 3D track generation

## Digital Twin

- Complete digital track model
- Modular architecture
- Multiple kart models
- Configurable vehicle parameters
- Physics-based simulation

## Optimization

- Racing line optimization
- Corner analysis
- Driver comparison
- Performance metrics
- AI-assisted analysis

## Reference Data

- Real AIM telemetry
- Google Earth KML
- Orthophoto imagery
- Reference Tracks
- Validation datasets

## Export

- Blender
- Unity
- CSV
- KML
- Future simulation formats

---

# Project Architecture

```
   Digital Twin

Reference Tracks
        │
        ▼
Telemetry Import
        │
        ▼
Track Reconstruction
        │
        ▼
Digital Twin Core
        │
        ▼
Simulation
        │
        ▼
Optimization
        │
        ▼
Visualization```

---

# Current Development Stage

**Current Version**

**v0.1 — Project Architecture**

The initial project structure has been established.

Current development focuses on:

- Architecture
- Documentation
- AIM Telemetry Parser
- Core Digital Twin classes

---

# Development Roadmap

| Version | Status | Description |
|----------|:------:|-------------|
| v0.1 | ✅ | Project architecture |
| v0.2 | 🔄 | AIM telemetry parser |
| v0.3 | ⏳ | Google Earth KML import |
| v0.4 | ⏳ | Track geometry |
| v0.5 | ⏳ | Digital Twin core |
| v0.6 | ⏳ | Vehicle models |
| v0.7 | ⏳ | Physics simulation |
| v0.8 | ⏳ | Racing line optimization |
| v0.9 | ⏳ | Complete Digital Twin |
| v1.0 | ⏳ | Research Platform Release |

---

# Technology Stack

## Programming Language

- Python 3.13+

## Scientific Libraries

- NumPy
- Pandas
- SciPy
- Matplotlib

## Geometry & GIS

- Shapely
- PyProj
- lxml

## Data Sources

- AIM Sports
- Google Earth
- Orthophoto imagery

## Image Processing

- OpenCV

## Development Tools

- Black
- Ruff
- mypy
- pytest
- pre-commit

---

# Repository Structure

```
KartSimDT/

docs/
data/
   experiments/
   reference/
   track/
   validation/
    vehicles/
examples/
tests/

src/
    kartsimdt/
        core/
        io/
        telemetry/
        geometry/
        track/
        terrain/
        vehicle/
        simulation/
        optimization/
        adapters/
        utils/
```

---

# Design Principles

The project follows several fundamental principles:

- Modular architecture
- Separation of concerns
- Test-driven development
- Reproducible research
- Extensible simulation models
- Clear documentation
- Open-source collaboration

---

# Project Objectives

The platform is intended to support:

- Kart track reconstruction
- Digital Twin generation
- Vehicle dynamics research
- Telemetry analysis
- Racing line optimization
- Educational projects
- Scientific research

---

# Engineering Principles

KartSimDT follows modern software engineering practices:

- Modular architecture
- Reference datasets
- Reproducible research
- Validation-first development
- Test-driven implementation
- Extensible Digital Twin models

---

# Documentation

Detailed documentation is available in the **docs/** directory.

- Architecture
- Development Guide
- API Documentation
- Telemetry Specification
- Track Model
- Research Notes
- Design Decisions
- Roadmap

---

# License

This project is distributed under the MIT License.

---

# Project Motto

> **Engineering the digital future of kart racing.**

---

# Project Status

🚧 Work in Progress

KartSimDT is currently under active development.