# KartSimDT — PROJECT CHARTER

Version: Part Two
Status: Active Development

---

# Mission

Create an engineering-grade open karting Digital Twin platform capable of:

- Telemetry analysis
- Track Digital Twin generation
- Kart simulation
- Vehicle setup optimization
- Engineering research
- Multi-platform visualization

---

# Vision

One Core.

Many Data Sources.

Many Applications.

One Digital Twin.

---

# Engineering Principles

Architecture before implementation.

Domain before visualization.

Physics before graphics.

Test before integration.

Digital Twin before rendering.

Every important engineering decision is documented.

---

# Current Architecture

Telemetry Import Layer

AIM CSV
    │
    ▼
AimCsvReader
    │
    ▼
AimRawData
    │
    ▼
AimValidator
    │
    ▼
AimMapper
    │
    ▼
TelemetrySession
    │
    ▼
AimTelemetryParser

Status

PART ONE

Nearly complete.

Remaining tasks

- Validate missing values
- Validate AIM version
- AimMapper
- TelemetrySession
- AimTelemetryParser

Goal

Finish Import Layer.

---

# PART TWO

Digital Twin Core

Core Domain

TelemetrySession

Track

Kart

Driver

Lap

Environment

SimulationState

Core Services

Import

Physics

Track Builder

Analysis

Optimization

Applications

Blender

Assetto Corsa

Unity

Python API

Future Interfaces

LiDAR

Photogrammetry

RTK GPS

Video

Helmet Sensors

---

# Parallel Development

Main Branch

KartSimDT Core

Engineering architecture

Applied Branch

Aukštadvaris Digital Twin

Assetto Corsa implementation

Technology validation

Future

Indoor Digital Twin

LiDAR integration

---

# Long-Term Objective

Create the most accurate open karting Digital Twin platform possible.

---

# Immediate Development Goal

Complete PART ONE.

Deliver a fully operational telemetry import pipeline producing TelemetrySession.

After completion begin Track domain development.

---

# Success Criteria

Every module must strengthen KartSimDT Core.

Every engineering decision must support the Digital Twin vision.

The architecture must remain independent from any single visualization platform.

Blender is the first application.

It is not the Core.