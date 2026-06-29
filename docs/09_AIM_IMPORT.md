# 📥 KartSimDT AIM Import Specification

## Document Information

| Property     | Value             |
| ------------ | ----------------- |
| Document     | AIM IMPORT        |
| Version      | v0.1              |
| Status       | 🟡 In Development |
| Last Updated | 2026-06-29        |

---

# Purpose

This document defines the AIM telemetry import subsystem.

Its purpose is to transform external AIM telemetry files into the internal KartSimDT telemetry domain model.

The AIM module acts only as an adapter between external telemetry data and the common telemetry domain.

---

# Scope

The AIM import subsystem is responsible for:

* Reading AIM CSV files
* Validating file structure
* Mapping AIM channels
* Extracting session metadata
* Detecting laps and sectors
* Building TelemetrySession objects

The subsystem is **not** responsible for telemetry analysis or simulation.

---

# Architecture Principle

The AIM module never defines its own telemetry objects.

All imported data is transformed into the common telemetry model.

```
AIM CSV
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
TelemetrySession
```

---

# Module Structure

```
io/
└── aim/
    ├── __init__.py
    ├── parser.py
    ├── reader.py
    ├── validator.py
    ├── mapper.py
    ├── channels.py
    ├── metadata.py
    ├── laps.py
    ├── beacons.py
    ├── constants.py
    └── exceptions.py
```

---

# Module Responsibilities

## parser.py

Coordinates the complete import process.

---

## reader.py

Loads AIM CSV files into memory.

---

## validator.py

Validates:

* CSV structure
* Required columns
* Missing data
* Supported versions

---

## mapper.py

Transforms AIM data into:

* TelemetrySession
* SessionMetadata
* TelemetryChannel
* LapCollection

---

## channels.py

Maps AIM channel names to the KartSimDT channel registry.

---

## metadata.py

Extracts:

* Driver
* Vehicle
* Track
* Session date
* Logger information

---

## laps.py

Creates Lap objects.

Responsible for:

* Lap detection
* Lap numbering
* Sector detection

---

## beacons.py

Processes beacon information.

Supports future virtual beacons.

---

## constants.py

Stores AIM-specific constants.

---

## exceptions.py

Defines AIM-specific exceptions.

---

# Import Pipeline

```
AIM CSV
    │
    ▼
reader.py
    │
    ▼
validator.py
    │
    ▼
channels.py
    │
    ▼
metadata.py
    │
    ▼
laps.py
    │
    ▼
mapper.py
    │
    ▼
parser.py
    │
    ▼
TelemetrySession
```

---

# Domain Mapping

The AIM module does not create proprietary telemetry classes.

It produces:

* TelemetrySession
* SessionMetadata
* TelemetryChannel
* Lap
* LapCollection

---

# Validation

Each imported file is validated for:

* CSV integrity
* Required channels
* Missing samples
* Timestamp consistency
* AIM compatibility

---

# Error Handling

The parser should generate descriptive exceptions for:

* Invalid files
* Unsupported versions
* Missing channels
* Corrupted data
* Mapping failures

---

# Future Extensions

The same architecture can support:

* MyChron
* MoTeC
* RaceBox
* VBOX
* Custom telemetry loggers

---

# Development Tasks

## Sprint 2.1 — Module Foundation

Tasks:

* [+] Create `reader.py`
* [+] Create `validator.py`
* [+] Create `mapper.py`
* [+] Create `channels.py`
* [+] Create `metadata.py`
* [+] Create `constants.py`
* [+] Create `exceptions.py`
* [+] Create `parser.py`

---

## Sprint 2.2 — CSV Reader

Tasks:

* [ ] Read AIM CSV file
* [ ] Detect delimiter
* [ ] Parse header
* [ ] Load DataFrame
* [ ] Unit tests

---

## Sprint 2.3 — Validator

Tasks:

* [ ] Validate CSV structure
* [ ] Validate required channels
* [ ] Validate timestamps
* [ ] Validate missing values
* [ ] Validate AIM version
* [ ] Unit tests

---

## Sprint 2.4 — Channel Mapping

Tasks:

* [ ] Create AIM channel registry
* [ ] Map AIM channel names
* [ ] Normalize channel units
* [ ] Create TelemetryChannel objects
* [ ] Unit tests

---

## Sprint 2.5 — Metadata Extraction

Tasks:

* [ ] Parse session metadata
* [ ] Create SessionMetadata
* [ ] Parse logger information
* [ ] Unit tests

---

## Sprint 2.6 — Lap Detection

Tasks:

* [ ] Analyze real AIM telemetry datasets
* [ ] Identify beacon information
* [ ] Identify lap timing information
* [ ] Design lap detection algorithm
* [ ] Implement `beacons.py`
* [ ] Implement `laps.py`
* [ ] Detect laps
* [ ] Detect sectors
* [ ] Build `LapCollection`
* [ ] Unit tests


---

## Sprint 2.7 — Parser Integration

Tasks:

* [ ] Build complete parser pipeline
* [ ] Create TelemetrySession
* [ ] Import complete AIM session
* [ ] Integration tests

---

## Sprint 2.8 — Validation

Tasks:

* [ ] Test Rotena dataset
* [ ] Test Anykščiai dataset
* [ ] Verify lap count
* [ ] Verify lap times
* [ ] Verify channel mapping
* [ ] Benchmark import performance

---

# Progress

| Sprint              | Status |
| ------------------- | :----: |
| Module Foundation   |    ⚪   |
| CSV Reader          |    ⚪   |
| Validator           |    ⚪   |
| Channel Mapping     |    ⚪   |
| Metadata Extraction |    ⚪   |
| Lap Detection       |    ⚪   |
| Parser Integration  |    ⚪   |
| Validation          |    ⚪   |

---

# Summary

The AIM import subsystem provides the entry point for external telemetry data.

Its responsibility is to transform AIM telemetry files into the common KartSimDT telemetry domain while keeping the internal architecture independent from external file formats.
