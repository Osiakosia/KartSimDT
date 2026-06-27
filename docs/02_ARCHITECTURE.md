# KartSimDT

**Document:** ARCHITECTURE

**Version:** v0.1

**Last Updated:** 2026-06-27

---

# System Architecture

KartSimDT is designed as a modular research platform for creating high-fidelity digital twins of kart racing tracks.

The architecture follows a layered design where each module has a single responsibility and communicates through well-defined interfaces.

The system is intended to grow gradually while maintaining backward compatibility and clear module separation.

---

# Core Design Principles

The architecture is based on the following principles:

- Modular design
- Separation of concerns
- High cohesion
- Low coupling
- Extensibility
- Testability
- Reproducible research
- Independent modules

---
# Architecture Goals

The primary goals of the architecture are:

• Scalability
• Maintainability
• Scientific reproducibility
• Modularity
• Extensibility
• Interoperability

---

# Reference Datasets

KartSimDT is validated using real-world karting data.

Current reference datasets:

• Rotena Kart Track
• Anykščiai Kart Track

Each dataset may contain:

• AIM telemetry
• Google Earth KML
• Orthophotos
• Metadata
• Validation measurements

---

# High-Level Architecture

```
                     Digital Twin
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
     Telemetry        Geometry          Vehicle
        │                 │                 │
        └──────────────┬──┴─────────────────┘
                       │
                     Core
                       │
                Simulation Engine
                       │
                 Optimization
                       │
                   Export Layer
```

---



# Project Structure

```
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

---

# Module Responsibilities

## Core

The project kernel.

Responsible for:

- Digital Twin
- Shared models
- Configuration
- Units
- Interfaces
- Exceptions

The Core must never depend on external adapters.

---

## IO

Responsible for importing and exporting external data.

Supported formats:

- AIM telemetry
- CSV
- KML
- PNG
- Future data formats

---

## Telemetry

Responsible for:

- Telemetry sessions
- Lap management
- Channel processing
- Filtering
- Analysis

---

## Geometry

Responsible for:

- Coordinate systems
- Geometry calculations
- Interpolation
- Elevation
- Spatial algorithms

---

## Track

Responsible for:

- Track model
- Centerline
- Track width
- Kerbs
- Boundaries
- Surface description

---

## Terrain

Responsible for:

- Terrain mesh
- Elevation model
- Ground surface
- Environment data

---

## Vehicle

Responsible for:

- Kart models
- Vehicle parameters
- Tires
- Engine
- Chassis
- Driver model

---

## Simulation

Responsible for:

- Physics engine
- Dynamic simulation
- Time integration
- Vehicle motion

---

## Optimization

Responsible for:

- Racing line optimization
- Parameter optimization
- Lap comparison
- Performance analysis

---

## Adapters

Responsible for communication with external software.

Examples:

- Blender
- Unity
- Google Earth
- Future simulators

---

## Utils

General helper utilities shared across the project.

Examples:

- Logging
- File utilities
- Mathematical helpers
- Validation

---

# Data Flow

```
Reference Data

AIM CSV
Google Earth KML
Orthophoto

        │
        ▼

Import Layer

        │
        ▼

Telemetry Processing

        │
        ▼

Track Reconstruction

        │
        ▼

Digital Twin

        │
        ▼

Simulation

        │
        ▼

Optimization

        │
        ▼

Visualization / Export

```

---

# Dependency Rules

The dependency direction must always point toward the Core.

```
Adapters
      │
IO
      │
Telemetry
      │
Geometry
      │
Core
```

Core must never import higher-level modules.

---

# Development Philosophy

KartSimDT evolves incrementally.

Each release should:

• remain functional
• remain documented
• remain testable
• preserve backward compatibility whenever practical

---

# Future Expansion

The architecture is designed to support future modules including:

- AI-assisted racing line optimization
- Machine learning
- Tire models
- Suspension models
- Weather simulation
- Multi-vehicle simulation
- Virtual coaching
- Digital twin synchronization

---

 # Architecture Evolution

Version 0.1 establishes the core architecture.

Future versions will extend the platform without changing the fundamental module hierarchy.
 ---

# Architecture Status

Current version:

**v0.1**

This document defines the initial architecture of KartSimDT and will evolve together with the project.