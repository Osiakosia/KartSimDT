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

# AIM Import Pipeline

```text
                    AIM CSV
                       │
                       ▼
             AimTelemetryParser
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
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
 Channel Registry   Metadata      Lap Detection
 (channels.py)    (metadata.py)   (laps.py)
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
                  AimMapper
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

* [+] Analyze AIM CSV structure
* [+] Detect file encoding (verified)
* [+] Detect delimiter
* [+] Parse metadata block
* [+] Parse channel names
* [+] Parse channel units
* [+] Load telemetry samples
* [+] Build `AimRawData`
* [+] Unit tests
---

## Sprint 2.3 — Validator

### Validate CSV structure

- [x] Metadata is not empty
- [x] Channel names are not empty
- [+] Channel units are not empty
- [+] Samples are not empty
- [+] Channel names count == channel units count
- [+] Sample columns == channel names count

### Validate required channels

- [+] Required channel: Time
- [+] Required channel: GPS Speed
- [+] Required channel: GPS Latitude
- [+] Required channel: GPS Longitude

### Validate timestamps

- [+] Time channel exists
- [+] Time starts at zero
- [+] Time is monotonically increasing
- [+] No duplicated timestamps

### Validate missing values

- [+] Metadata has no missing required values
- [+] Channel names contain no empty values
- [+] Samples contain no missing values

### Validate AIM version

- [+] Format field exists
- [+] Supported AIM CSV format

### Unit tests

- [x] Empty metadata
- [x] Empty channel names
- [+] Empty channel units
- [+] Empty samples
- [+] Channel count mismatch
- [+] Sample column mismatch
- [+] Missing required channel
- [+] Invalid timestamps
- [+] Missing values
- [+] Invalid AIM version

---

## Sprint 2.4 — Channel Mapping

### Goal

Establish the channel mapping layer between AIM telemetry files and the KartSimDT telemetry domain.

### Tasks

#### Channel Registry

- [+] Create AIM channel registry
- [+] Map AIM channel names to KartSimDT channel identifiers
- [ ] Define channel aliases *(deferred until alternative AIM channel variants are available)*
- [+] Normalize channel units

#### Mapper

- [+] Create `AimMapper` skeleton
- [+] Implement channel mapping
- [+] Create `TelemetryChannel` objects
- [+] Build `ChannelCollection`

#### Unit Tests

- [+] Test channel registry
- [ ] Test channel aliases *(deferred)*
- [+] Test unit normalization
- [+] Test channel mapping

~~## Sprint 2.5 — Metadata Extraction

Tasks:

* [+] Parse session metadata
* [+] Create SessionMetadata
* [ ] Parse logger information
* [+] Unit tests~~

---

## Sprint 2.6 — Lap Mapping

### Goal

Map AIM lap information into the KartSimDT telemetry domain model.

---

### Phase 1 — AIM Analysis

Tasks:

* [x] Analyze real AIM telemetry datasets
* [x] Inspect beacon marker information
* [x] Inspect lap timing information
* [x] Create `devtools/inspect_laps.py`
* [x] Verify full session CSV layout
* [x] Verify beacon marker consistency
* [x] Verify lap time consistency

---

### Phase 2 — Domain Design

Tasks:

* [+] Review `Lap` domain model
* [+] Extend `Lap` with future-proof attributes
* [+] Review `LapCollection`
* [+] Add convenient collection methods
* [+] Review future `Sector` model

---

### Phase 3 — AIM Lap Parsing

Tasks:

* [+] Create `lap_parser.py`
* [+] Parse `Beacon Markers`
* [+] Parse `Segment Times`
* [+] Normalize lap timing values
* [ ] Validate parsed lap information



---

### Phase 4 — Lap Mapping

Tasks:

* [ ] Implement `_map_laps()`
* [ ] Build `LapCollection`
* [ ] Preserve beacon information
* [ ] Preserve lap timing information

---

### Phase 5 — Validation

Tasks:

* [ ] Create `inspect_beacons.py`
* [ ] Verify mapped laps
* [ ] Create lap mapper unit tests
* [ ] Validate using `rotena_session.csv`

---

### Phase 6 — End-to-End Integration

Tasks:

* [x] Create end-to-end telemetry integration test
* [+] Complete `TelemetrySession` pipeline
* [+] Verify integration test passes

---

### Definition of Done

```text
TelemetrySession

✓ Metadata
✓ Channels
✓ Laps

Complete AIM Telemetry Import
```

```

### Phase 6 — End-to-End Integration

Tasks:

* [+] Create full AIM import integration test
* [+] Read real session CSV
* [+] Validate raw data
* [+] Map TelemetrySession
* [+] Verify complete domain object

Telemetry Core v1.0 completed.


### Definition of Done

```text
AIM CSV
      │
      ▼
Reader
      │
      ▼
AimRawData
      │
      ▼
Validator
      │
      ▼
Mapper
      ├── Metadata      ✓
      ├── Channels      ✓
      └── Laps          ✓
      │
      ▼
TelemetrySession
      ├── Metadata      ✓
      ├── Channels      ✓
      └── Laps          ✓
```

Telemetry Core v1.0 completed.


---

## Sprint 2.7 — Parser Integration

Tasks:

* [+] Build complete parser pipeline
* [+] Create TelemetrySession
* [+] Import complete AIM session
* [+] Integration tests

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
