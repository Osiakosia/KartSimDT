# 🏗 KartSimDT Architecture

## 📄 Document Information

| Property | Value |
|----------|-------|
| Document | System Architecture |
| Version | v1.0 |
| Status | 🟡 In Development |
| Last Updated | 2026-07-01 |

---

# 🎯 Purpose

This document defines the software architecture of the KartSimDT platform.

Its purpose is to describe how the system is organized, how individual modules interact, and which engineering principles govern the overall design.

The architecture is intended to provide a stable foundation for long-term development while supporting future extensions, research activities, and Digital Twin applications.

This document complements the repository **README** by describing the internal engineering architecture rather than the project overview.

---

# 🌍 System Overview

KartSimDT is an engineering platform for transforming real-world kart racing data into validated Digital Twins.

The platform combines telemetry processing, computational geometry, vehicle dynamics, and physics-based simulation into a modular software architecture.

High-level engineering workflow:

```text
Telemetry
      │
      ▼
Track Reconstruction
      │
      ▼
Vehicle Modeling
      │
      ▼
Physics Simulation
      │
      ▼
Digital Twin
      │
      ▼
Optimization
```

The platform is designed around independent modules with clearly defined responsibilities.

Each module communicates through stable domain models, allowing new functionality to be added without affecting the overall architecture.

---

# 🏛 Architectural Principles

KartSimDT follows modern software engineering principles.

## Core Principles

- Modular architecture
- Separation of concerns
- High cohesion
- Low coupling
- Single responsibility
- Extensibility
- Testability
- Reproducible engineering
- Validation-first development

---

## Engineering Goals

The architecture is designed to achieve:

- Scalability
- Maintainability
- Reusability
- Scientific reproducibility
- Interoperability
- Platform independence
- Long-term evolution

---

## Design Philosophy

The architecture is based on a simple engineering principle:

> Build a stable Core that remains independent of external data formats, applications, and visualization tools.

External systems communicate with the platform exclusively through adapters, while the Core contains the shared engineering domain and business logic.

This separation enables KartSimDT to evolve without introducing unnecessary coupling between internal components and external technologies.

---

# 🧱 Layered Architecture

KartSimDT follows a layered architecture in which each layer has a clearly defined responsibility.

Higher layers depend only on stable interfaces provided by lower layers, while the Core remains independent of external systems.

```text
                 External Data Sources
                         │
                         ▼
                  Import Layer (IO)
                         │
                         ▼
                 Core Domain Layer
                         │
                         ▼
                 Simulation Layer
                         │
                         ▼
               Application Layer
                         │
                         ▼
              External Applications
```

## Layer Responsibilities

| Layer | Responsibility |
|--------|----------------|
| Import Layer | Read and validate external data formats |
| Core Domain | Shared engineering models and business logic |
| Simulation Layer | Physics simulation and Digital Twin processing |
| Application Layer | Analysis, visualization and optimization |

> [!IMPORTANT]
> The Core Domain must never depend on external file formats, user interfaces, or visualization software.

---

# 📦 Core Modules

The Core is organized into independent engineering modules.

Each module owns a single engineering domain and exposes a stable public interface.

```text
Core

├── Telemetry
├── Geometry
├── Track
├── Terrain
├── Vehicle
├── Simulation
├── Optimization
└── Utilities
```

## Module Responsibilities

| Module | Responsibility |
|----------|----------------|
| Telemetry | Telemetry sessions, laps, channels and metadata |
| Geometry | Coordinate systems and geometric algorithms |
| Track | Track model and reconstruction |
| Terrain | Terrain and elevation models |
| Vehicle | Vehicle configuration and dynamics |
| Simulation | Physics engine and Digital Twin simulation |
| Optimization | Racing line and performance optimization |
| Utilities | Shared helper components |

Each module is responsible only for its own engineering domain.

Communication between modules should occur through well-defined public interfaces.

---

# 📁 Repository Structure

The repository is organized according to the layered architecture.

```text
KartSimDT/

├── docs/
├── data/
├── examples/
├── tests/
│
└── src/
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

## Repository Organization

| Directory | Purpose |
|-----------|----------|
| docs | Engineering documentation |
| data | Reference datasets and validation data |
| examples | Usage examples |
| tests | Automated tests |
| src | Project source code |

The repository structure reflects the engineering architecture, ensuring that documentation, implementation, testing, and reference data remain clearly separated.

---

# 🔄 Data Flow

KartSimDT processes engineering data through a well-defined transformation pipeline.

Each stage has a single responsibility and produces data for the next stage.

```text
External Data
      │
      ▼
Import Adapter
      │
      ▼
Raw Data
      │
      ▼
Validation
      │
      ▼
Domain Mapping
      │
      ▼
Core Domain Objects
      │
      ▼
Simulation
      │
      ▼
Analysis & Optimization
      │
      ▼
Export / Visualization
```

## Data Processing Stages

| Stage | Responsibility |
|--------|----------------|
| Import Adapter | Read external file formats |
| Raw Data | Temporary representation of imported data |
| Validation | Verify integrity and consistency |
| Domain Mapping | Convert imported data into the common domain model |
| Core Domain | Store engineering objects |
| Simulation | Execute Digital Twin algorithms |
| Analysis | Produce engineering results |
| Export | Communicate with external applications |

Each stage performs exactly one engineering responsibility.

---

# 🧩 Domain Model Ownership

KartSimDT maintains a single engineering domain model.

Domain objects are owned exclusively by the Core.

External file formats never introduce their own business objects.

```text
External Format
       │
       ▼
 Import Adapter
       │
       ▼
   Raw Data
       │
       ▼
 Domain Mapper
       │
       ▼
 Core Domain Model
```

Examples of Core domain objects include:

- TelemetrySession
- SessionMetadata
- TelemetryChannel
- Lap
- LapCollection

Import adapters are responsible only for transforming external data into these shared objects.

This architecture provides:

- Single source of truth
- Consistent engineering workflow
- Minimal duplication
- Stable public interfaces
- Easy integration of new data formats

---

# 🔌 Adapter Architecture

External systems communicate with KartSimDT exclusively through adapters.

Adapters isolate external technologies from the engineering Core.

```text
           External Systems

 AIM CSV      KML      Orthophoto
    │          │            │
    └──────────┼────────────┘
               ▼
        Import Adapters
               │
               ▼
         KartSimDT Core
               │
               ▼
        Export Adapters
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
 Blender   Assetto Corsa  Research Tools
```

## Adapter Responsibilities

| Adapter | Responsibility |
|----------|----------------|
| Import | Read external engineering data |
| Export | Provide data to external applications |

Adapters should contain no business logic.

Their responsibility is limited to data transformation and communication.

---

# 🌳 Branch Architecture

KartSimDT development follows a dual-branch strategy.

```text
                 KartSimDT

                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
     Main Branch              Applied Branch
        │                           │
        ▼                           ▼
 Stable Engineering Core   Engineering Validation
                                    │
                                    ▼
                          Assetto Corsa
                          Blender
                          Research Projects
```

## Branch Responsibilities

| Branch | Purpose |
|----------|----------|
| Main | Stable engineering platform |
| Applied | Validation using real engineering applications |

The Main branch contains reusable platform components.

The Applied branch demonstrates and validates those components using real-world engineering scenarios.

This separation allows the Core to evolve independently while continuously validating its design through practical applications.

---

# 📈 Architecture Evolution

KartSimDT is designed to evolve incrementally while preserving the stability of its Core architecture.

New functionality should extend the platform rather than modify existing engineering principles.

The long-term evolution follows a layered progression.

```text
Telemetry
      │
      ▼
Track Reconstruction
      │
      ▼
Vehicle Modeling
      │
      ▼
Physics Simulation
      │
      ▼
Digital Twin
      │
      ▼
Optimization
      │
      ▼
Research Platform
```

Each development stage builds upon previously validated engineering components.

---

# 🚀 Future Expansion

The architecture has been intentionally designed to support future engineering modules without requiring fundamental redesign.

## Planned Extensions

| Area | Planned Capability |
|------|--------------------|
| Telemetry | Additional telemetry formats |
| GIS | Advanced geospatial processing |
| Track | Automatic track reconstruction |
| Vehicle | Multiple kart configurations |
| Physics | Advanced tire and suspension models |
| Simulation | Multi-vehicle simulation |
| Optimization | AI-assisted racing line optimization |
| Visualization | Real-time Digital Twin rendering |
| Research | Machine learning and engineering validation |

Future modules should integrate through stable interfaces while preserving Core independence.

---

# 🛡 Architecture Stability

The following principles should remain stable throughout the lifetime of the project.

## Stable Components

- Engineering Core
- Domain model
- Layered architecture
- Adapter pattern
- Module responsibilities
- Public interfaces

## Evolutionary Components

- Import adapters
- Export adapters
- Physics models
- Vehicle models
- Optimization algorithms
- External integrations

Stable architectural principles reduce technical debt and enable long-term maintainability.

---

# 📌 Summary

KartSimDT is built as a modular engineering platform centered around a stable Core domain.

The architecture separates external technologies from engineering logic through clearly defined layers and adapters, allowing the platform to evolve without compromising maintainability or extensibility.

The guiding principles of the architecture are:

- Modular engineering design
- Stable Core domain
- Layered architecture
- Adapter-based integration
- Validation-first development
- Reproducible engineering workflows

Together, these principles establish a scalable foundation for building validated Digital Twins of kart racing tracks and supporting future engineering research.

---

> **A stable architecture enables sustainable innovation.**