# 💻 KartSimDT Development Guide

## Document Information

| Property     | Value       |
| ------------ | ----------- |
| Document     | DEVELOPMENT |
| Version      | v0.1        |
| Status       | 🟢 Active   |
| Last Updated | 2026-06-27  |

---

# Purpose

This document defines the development workflow, coding standards, testing strategy and engineering practices used throughout the KartSimDT project.

The objective is to ensure that every component of the platform is developed consistently, tested using real-world data and documented according to the project standards.

---

# Development Philosophy

KartSimDT is developed as an engineering platform rather than a collection of independent scripts.

Every new feature should be:

* Modular
* Documented
* Tested
* Validated
* Reproducible

Development follows an incremental approach where every milestone produces a functional improvement to the platform.

---

# Development Workflow

Every new feature follows the same workflow:

```text
Research
    │
    ▼
Architecture
    │
    ▼
Implementation
    │
    ▼
Unit Tests
    │
    ▼
Reference Dataset Validation
    │
    ▼
Documentation
    │
    ▼
Git Commit
```

---

# Coding Standards

Development requirements:

* Python 3.13+
* Type hints for public interfaces
* Ruff for linting
* Black for formatting
* mypy for static type checking
* pytest for automated testing
* pre-commit hooks before every commit

---

# Repository Workflow

Recommended Git commit prefixes:

```text
feat:      New functionality
fix:       Bug fix
refactor:  Internal improvements
test:      Tests
docs:      Documentation
style:     Formatting
chore:     Maintenance
```

Examples:

```text
feat: implement AimTelemetryParser
feat: add TelemetrySession model
docs: update architecture
test: add parser validation tests
fix: correct lap detection
```

---

# Testing Strategy

Every module should be verified on three levels:

## Unit Tests

Validate individual functions and classes.

## Integration Tests

Verify interaction between multiple modules.

## Reference Dataset Validation

Validate the implementation using real-world reference tracks.

Current reference datasets:

* Aukštadvaris
* Mande_Kart
* Anykščiai

---

# Reference Data Policy

Whenever possible, algorithms should be tested using measured data rather than synthetic datasets.

Reference datasets may include:

* AIM telemetry
* Google Earth KML
* Orthophoto imagery
* Elevation data
* Track metadata

---

# Development Principles

The following principles apply throughout the project:

* One module — one responsibility
* Prefer composition over complexity
* Keep modules independent
* Avoid circular dependencies
* Core must remain independent
* Write readable code
* Document public interfaces
* Validate before extending functionality

---

# Documentation Policy

Documentation evolves together with the implementation.

Major architectural decisions should first be recorded in **RESEARCH.md** before becoming part of the permanent documentation.

---

# Engineering Validation

A feature is considered complete only when:

* Source code is implemented
* Unit tests pass
* Integration tests pass
* Validation with reference datasets succeeds
* Documentation is updated

---

# Current Development Target

The current engineering milestone is:

**M1 – Aukštadvaris Digital Twin**

Primary objectives:

* AIM Telemetry Parser
* Telemetry Session
* Fastest Lap Extraction
* Google Earth KML Import
* Track Reconstruction
* First Digital Twin

---

# Long-Term Development Goals

Future development includes:

* Vehicle dynamics
* Physics simulation
* Racing line optimisation
* AI-assisted analysis
* Multi-track support
* Research platform
* Blender and Unity integration

---

# Summary

KartSimDT is developed according to engineering best practices with emphasis on modular architecture, real-world validation and reproducible scientific research.

Every implemented feature should move the project one step closer to a fully validated Digital Twin of a real kart racing circuit.
