# 🔬 KartSimDT Research Notebook

## Purpose

The Research Notebook records the scientific and engineering knowledge generated during the development of KartSimDT.

Unlike the technical documentation, this document captures ideas, hypotheses, experiments, observations and engineering decisions before they become part of the official project specification.

---

# Research Objectives

The long-term objectives of this notebook are:

* Document engineering investigations
* Record experimental results
* Preserve design rationale
* Compare algorithms
* Validate Digital Twin accuracy
* Support reproducible research

---

# Research Methodology

Every research topic should follow the same structure:

1. Problem
2. Hypothesis
3. Method
4. Results
5. Conclusions
6. Future Work

---

# Research Entry 001

## Project Vision

### Objective

Develop an engineering-grade Digital Twin platform capable of reconstructing kart racing circuits from real-world measurements.

### Initial Assumptions

* Real telemetry should always be preferred over synthetic datasets.
* Every engineering model must be reproducible.
* Validation is mandatory.
* The platform should remain modular.

### Status

✅ Accepted

---

# Research Entry 002

## Reference Dataset Strategy

### Objective

Define the primary datasets used during development.

### Decision

KartSimDT will use real reference tracks instead of artificial test datasets.

### Current Reference Tracks

* Aukštadvaris
* Rotena
* Anykščiai

Each reference dataset may contain:

* AIM telemetry
* Google Earth KML
* Orthophoto imagery
* Elevation data
* Metadata

### Status

🟡 Active

---

# Research Entry 003

## First Engineering Milestone

### Objective

Develop the first fully functional Digital Twin.

### Selected Track

Aukštadvaris Kart Track

### Required Components

* AIM Parser
* Fastest Lap Extraction
* KML Import
* Track Geometry
* Digital Twin
* Validation

### Success Criteria

The generated Digital Twin reproduces the real track geometry using measured data.

### Status

🟡 In Progress

---

# Future Research Topics

The following investigations are planned:

* Telemetry filtering
* Track centreline reconstruction
* Elevation interpolation
* Racing line optimisation
* Vehicle dynamics
* Tyre modelling
* Mass distribution
* Centre of Gravity estimation
* Physics validation
* AI-assisted optimisation

---

# Notes

This notebook is expected to evolve together with the project and serves as the primary record of engineering knowledge generated during the development of KartSimDT.
