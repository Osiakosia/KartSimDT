# 🔬 KartSimDT Research Notebook

Version: 0.2

Status: Living Document

---

# Purpose

The Research Notebook records the engineering knowledge, scientific
investigations and future concepts developed during the evolution of
KartSimDT.

Unlike technical documentation, this notebook captures ideas,
hypotheses, experiments and architectural concepts before they become
part of the platform.

It serves as the long-term engineering memory of the project.

---

# Research Objectives

The objectives of this notebook are:

- Document engineering investigations
- Preserve design rationale
- Record experimental results
- Validate engineering assumptions
- Compare alternative approaches
- Support reproducible research
- Capture future platform concepts

---

# Research Methodology

Every investigation should follow the same engineering process.

1. Problem
2. Background
3. Hypothesis
4. Method
5. Results
6. Conclusions
7. Future Work

---

# Research Foundation

KartSimDT research follows several fundamental principles.

- Reality before simulation.
- Validation before implementation.
- Digital Twins originate from measured data.
- Every engineering process should be repeatable.
- Understanding is more valuable than visualization.
- Learning is the ultimate objective.

---

# Research Entry 001

## Platform Vision

### Objective

Develop an engineering platform capable of transforming real-world
motorsport data into validated Digital Twins.

### Initial Assumptions

- Real telemetry is preferred over synthetic datasets.
- Platform architecture must remain modular.
- Domain objects isolate external formats.
- Validation is mandatory.

### Status

✅ Accepted

---

# Research Entry 002

## Reference Dataset Strategy

### Objective

Establish engineering reference datasets.

### Current Reference Tracks

- Aukštadvaris
- Rotena
- Anykščiai

Reference datasets may contain:

- AIM telemetry
- Track Survey
- KML
- Orthophotos
- Elevation
- Metadata

### Status

🟡 Active

---

# Research Entry 003

## First Digital Twin

### Objective

Create the first validated Digital Twin of a real kart circuit.

### Selected Track

Aukštadvaris

### Components

- AIM Import
- TelemetrySession
- TrackSurveySession
- Track Geometry
- Replay
- Validation

### Status

🟡 In Progress

---

# Research Entry 004

## Ghost Kart

### Objective

Create a virtual driver reconstructed from measured telemetry.

Applications:

- Racing line comparison
- Corner analysis
- Replay visualization
- Simulator reference
- Driver coaching

Status:

💡 Research

---

# Research Entry 005

## SimCoach

### Objective

Transform completed training sessions into interactive learning
experiences.

Research topics:

- Root cause analysis
- Driver progress evaluation
- Corner-by-corner coaching
- Replay visualization
- Training recommendations

Core idea:

> Performance is measured. Understanding is learned.

Status:

💡 Research

---

# Research Entry 006

## Coaching Studio

### Objective

Develop a post-session engineering workspace combining telemetry,
Ghost Kart and Digital Twin visualization.

Potential components:

- Session replay
- Ghost comparison
- Corner coaching
- Performance timeline
- Interactive visualization

Status:

💡 Research

---

# Research Entry 007

## Drone Observer

### Objective

Investigate aerial data acquisition for outdoor circuits.

Potential applications:

- Racing line validation
- Multi-driver tracking
- Overtaking analysis
- Arbitration support
- Track reconstruction

Status:

💡 Research

---

# Long-Term Research Areas

Future investigations may include:

- Track centreline reconstruction
- Elevation modelling
- Indoor localization
- Outdoor localization
- Sensor synchronization
- Computer vision
- Drone photogrammetry
- LiDAR
- Vehicle dynamics
- Tyre modelling
- AI-assisted coaching
- Race intelligence
- Automatic Digital Twin generation

---

# Engineering Philosophy

Research ideas are intentionally separated from implementation.

Only validated engineering concepts become part of the KartSimDT
platform.

Ideas evolve into prototypes.

Prototypes evolve into validated platform modules.

---

# Research Evolution

```
Observation

↓

Idea

↓

Hypothesis

↓

Experiment

↓

Validation

↓

Prototype

↓

Platform Module
```

---

# Notes

This notebook is expected to evolve throughout the lifetime of
KartSimDT and serves as the permanent record of engineering knowledge
generated during the project.