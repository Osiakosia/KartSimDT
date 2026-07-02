# 🗺 KartSimDT Development Roadmap

## 📄 Document Information

| Property | Value |
|----------|-------|
| Document | Development Roadmap |
| Version | v1.0 |
| Status | 🟡 In Development |
| Last Updated | 2026-07-01 |

---

# 🎯 Purpose

This document defines the long-term development roadmap of the KartSimDT platform.

Its purpose is to describe the planned engineering phases, major project milestones, and the overall implementation strategy.

The roadmap provides a high-level view of the project while detailed implementation plans are maintained within individual module specifications.

---

# 🧭 Development Strategy

KartSimDT is developed incrementally through a series of well-defined engineering phases.

Each phase delivers a complete and validated set of functionality before the next phase begins.

This approach ensures:

- Stable architectural evolution
- Incremental delivery of features
- Continuous validation
- Reduced technical debt
- Clear engineering milestones

Development follows the principle:

```text
Foundation
      │
      ▼
Implementation
      │
      ▼
Validation
      │
      ▼
Integration
      │
      ▼
Release
```

Every completed phase establishes a stable foundation for the next stage of development.

---

# 🗺 Development Phases

The project is divided into major engineering phases.

Each phase represents a significant milestone in the evolution of the platform.

```text
Phase 1
Foundation
      │
      ▼
Phase 2
Telemetry
      │
      ▼
Phase 3
Track Reconstruction
      │
      ▼
Phase 4
Digital Twin Core
      │
      ▼
Phase 5
Physics
      │
      ▼
Phase 6
Optimization
      │
      ▼
Phase 7
Research Platform
```

Detailed implementation plans, sprint definitions, and engineering tasks are maintained within the corresponding module specification documents.

The roadmap intentionally remains technology-independent and focuses on long-term engineering objectives rather than implementation details.

---

# 📋 Phase Overview

The KartSimDT roadmap is organized into engineering phases.

Each phase delivers a complete and validated capability that becomes the foundation for subsequent development.

---

## 🟢 Phase 1 — Foundation

### Goal

Establish the engineering foundation of the KartSimDT platform.

### Major Deliverables

- Repository structure
- Engineering documentation
- Development standards
- Core architecture
- Development workflow

### Status

🟢 Complete

---

## 🟡 Phase 2 — Telemetry

### Goal

Develop a unified telemetry import framework and establish the common telemetry domain.

### Major Deliverables

- AIM telemetry import
- Telemetry domain model
- Channel registry
- Session metadata
- Lap detection
- Import validation

### Specifications

- AIM Import Specification

### Status

🟡 In Progress

---

## ⚪ Phase 3 — Track Reconstruction

### Goal

Reconstruct accurate track geometry from real-world geospatial data.

### Major Deliverables

- Google Earth KML import
- Orthophoto processing
- Track centerline reconstruction
- Elevation model
- Surface representation

### Status

⚪ Planned

---

## ⚪ Phase 4 — Digital Twin Core

### Goal

Build the engineering representation of the racing environment.

### Major Deliverables

- Digital track model
- Vehicle model integration
- Environment model
- Simulation configuration

### Status

⚪ Planned

---

## ⚪ Phase 5 — Physics

### Goal

Develop validated vehicle dynamics models for realistic simulation.

### Major Deliverables

- Tire models
- Chassis dynamics
- Powertrain simulation
- Vehicle dynamics validation

### Status

⚪ Planned

---

## ⚪ Phase 6 — Optimization

### Goal

Provide engineering tools for performance analysis and optimization.

### Major Deliverables

- Racing line optimization
- Driver comparison
- Performance metrics
- AI-assisted analysis

### Status

⚪ Planned

---

## ⚪ Phase 7 — Research Platform

### Goal

Transform KartSimDT into a complete engineering and research platform.

### Major Deliverables

- Scientific validation
- Benchmark datasets
- Research publications
- Public platform release

### Status

⚪ Planned

---

# 🎯 Active Development

At any given time, only one engineering specification should be considered the primary implementation target.

The active development workflow is tracked at three levels.

| Level | Current Focus |
|--------|---------------|
| Phase | Current engineering phase |
| Specification | Active module specification |
| Sprint | Current implementation sprint |

Current development should always follow this hierarchy:

```text
Roadmap
    │
    ▼
Current Phase
    │
    ▼
Active Specification
    │
    ▼
Current Sprint
    │
    ▼
Implementation
    │
    ▼
Validation
```

This approach keeps long-term planning, module development, and implementation clearly separated.

---

# 🔮 Long-Term Vision

KartSimDT is designed to evolve from a telemetry processing toolkit into a complete Digital Twin engineering platform.

The planned engineering evolution is illustrated below.

```text
Telemetry
      │
      ▼
Track Reconstruction
      │
      ▼
Digital Twin
      │
      ▼
Vehicle Modeling
      │
      ▼
Physics Engine
      │
      ▼
Simulation
      │
      ▼
Optimization
      │
      ▼
Research Platform
```

Each completed phase provides the validated foundation required for the next stage of development.

---

# 📌 Summary

The KartSimDT development roadmap defines the long-term engineering strategy of the project.

Its responsibilities are limited to:

- defining engineering phases;
- tracking overall project progress;
- identifying the active engineering specification;
- describing release milestones;
- guiding the long-term evolution of the platform.

Detailed implementation planning is intentionally delegated to dedicated specification documents.

This separation ensures that:

- the roadmap remains concise and stable;
- specifications can evolve independently;
- sprint planning remains module-specific;
- implementation details do not clutter long-term project planning.

Together, the roadmap and module specifications provide a structured framework for managing the continued evolution of KartSimDT.

---

> **Plan the platform. Build one specification at a time.**