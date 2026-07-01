# 📡 KartSimDT Telemetry Specification

## Document Information

| Property     | Value             |
| ------------ | ----------------- |
| Document     | TELEMETRY         |
| Version      | v0.1              |
| Status       | 🟡 In Development |
| Last Updated | 2026-06-27        |

---

# Purpose

This document specifies the telemetry subsystem of KartSimDT.

It defines:

* telemetry architecture
* domain model
* supported data formats
* development plan
* implementation progress

---

# Design Goals

The telemetry subsystem shall:

* remain independent from specific telemetry vendors
* support multiple telemetry formats
* provide a unified domain model
* preserve original measurements
* support engineering analysis
* support Digital Twin generation

---

# Supported Data Sources

Current:

* AIM Sports CSV

Planned:

* MyChron
* MoTeC
* Race Technology
* GPX
* Custom CSV

---

# Telemetry Architecture

```text
External Data

AIM CSV

MyChron

MoTeC

        │

        ▼

Import Layer

        │

        ▼

Telemetry Domain Model

        │

        ▼

Analysis

        │

        ▼

Digital Twin
```

---

# Domain Model

```text
TelemetrySession
│
├── SessionMetadata
├── ChannelCollection
│       └── TelemetryChannel
├── LapCollection
│       └── Lap
└── DataFrame
```

---

# Package Structure

```text
telemetry/
│
├── __init__.py
├── session.py
├── metadata.py
├── channel.py
├── channels.py
├── lap.py
├── laps.py
└── constants.py
```

---

# Responsibilities

## TelemetrySession

Stores the complete telemetry session.

---

## SessionMetadata

Stores session information.

Examples:

* track
* driver
* kart
* logger
* sampling rate

---

## TelemetryChannel

Represents one telemetry channel.

Examples:

* Speed
* RPM
* GPS Latitude
* GPS Longitude
* Throttle

---

## ChannelCollection

Container for telemetry channels.

---

## Lap

Represents one completed lap.

---

## LapCollection

Container for all laps within a session.

---

# Development Sprints

## Sprint 1 — Domain Model

Status: 🟡

Tasks:

* [+] Create `lap.py`
* [+] Create `channel.py`
* [+] Create `metadata.py`
* [+] Create `laps.py`
* [+] Create `channels.py`
* [+] Create `session.py`
* [+] Create `analysis.py`
* [+] Create `constants.py`
* [+] Create `filters.py`
* 

---

## Sprint 2 — AIM Import

Status: ⚪

Tasks:

* [ ] CSV Reader
* [ ] Header Parser
* [ ] Channel Parser
* [ ] Session Builder

---

## Sprint 3 — Validation

Status: ⚪

Tasks:

* [ ] Channel validation
* [ ] Lap validation
* [ ] Metadata validation

---

## Sprint 4 — Telemetry Analysis

Status: ⚪

Tasks:

* [ ] Fastest lap
* [ ] Lap statistics
* [ ] Channel statistics
* [ ] Signal filtering

---

## Sprint 5 — Digital Twin Integration

Status: ⚪

Tasks:

* [ ] Export TelemetrySession
* [ ] Track synchronization
* [ ] Simulation interface

---

# Current Milestone

Current objective:

Create the first complete `TelemetrySession` object from a real AIM CSV file recorded at the Aukštadvaris kart track.

---

# Validation

Telemetry implementation is validated using reference datasets.

Current reference tracks:

* Aukštadvaris
* Rotena
* Anykščiai

---

# Future Extensions

Future capabilities include:

* Real-time telemetry
* Live streaming
* Cloud synchronization
* Multi-session comparison
* AI-assisted telemetry analysis
* Physics validation

---

# Progress

| Sprint                   | Status |
| ------------------------ | :----: |
| Domain Model             |   🟡   |
| AIM Import               |    ⚪   |
| Validation               |    ⚪   |
| Analysis                 |    ⚪   |
| Digital Twin Integration |    ⚪   |

---

# Summary

The telemetry subsystem provides the foundation for importing, validating and analysing telemetry data before it is transformed into engineering-grade Digital Twin models.
