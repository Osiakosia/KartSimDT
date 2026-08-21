# KartSimDT — Elevation and Integration Development Directions

**Status:** Architecture checkpoint  
**Date:** 2026-08-16

## 1. Platform Vision

KartSimDT is a platform for **Karting Digital Twin + Digital Coach**.

The two branches are **parallel primary development directions** built on the same KartSimDT Core.

```text
                         KartSimDT
                             |
                         CORE / DOMAIN
                             |
              +--------------+--------------+
              |                             |
              v                             v
        DIGITAL TWIN                  DIGITAL COACH
              |                             |
        Track Model                   Session Data
        Track Builder                 Telemetry
        3D Geometry                   Lap Analysis
        Visualization                 Optimal Lap
        Simulation                    Optimal Racing Line
                                      Fault Detection
                                      Fault Correction
```

Core principle:

> **One Core. Two parallel product branches: Digital Twin + Digital Coach.**

## 2. KartSimDT Core

KartSimDT Core is the **orchestrator and canonical domain/data layer**.

It owns platform-level concepts and contracts such as:

- Track
- Track geometry
- Elevation
- Kart
- Driver
- Session
- Lap
- Telemetry
- Analysis
- Simulation state

Blender and simulators are applications/backends, not the Core.

## 3. Elevation and 3D Track Direction

Elevation is a **first-class Track data product**.

Current outdoor workflow:

```text
GPS / KML
    |
    v
Track Survey
    |
    +-- latitude / longitude
    +-- elevation
    |
    v
Local 3D Geometry
    |
    +-- X
    +-- Y
    +-- Z / elevation
    |
    v
KartSimDT Track Model
```

Aukštadvaris has already demonstrated:

- 677 centerline points;
- local X/Y geometry;
- elevation preserved as Z;
- 3D Blender Curve;
- approximately 5.43 m elevation range;
- 8 m working racing-line width.

## 4. Outdoor and Indoor Survey

GPS must not be an architectural assumption for all tracks.

### Outdoor

```text
GPS / RTK
Camera
IMU
LiDAR
```

### Indoor

```text
LiDAR
   +
Camera
   +
IMU
   |
   v
Sensor Fusion / SLAM
   |
   v
3D Track Survey
   |
   v
KartSimDT Core
```

Indoor principle:

> **LiDAR provides the geometric foundation, Camera provides visual/semantic information, and IMU provides motion constraints.**

## 5. Digital Twin Direction

The Digital Twin branch transforms canonical KartSimDT track data into a simulation/visual representation.

```text
KartSimDT Track Model
        |
        v
3D Centerline
        |
        +-- elevation
        +-- working width
        +-- track metadata
        |
        v
Blender
        |
        +-- Road
        +-- Terrain
        +-- Kerbs
        +-- Objects
        +-- Layout
        |
        v
Simulator-ready Track Artifact
```

Do not build a custom KartSimDT track-building engine unless existing tools prove insufficient. First evaluate Blender and suitable addons.

## 6. Blender Output

The `.blend` file is a **Digital Twin artifact**, not the canonical KartSimDT Track Model.

```text
KartSimDT Canonical Track
          |
          v
      Blender
          |
          v
      scene.blend
          |
          v
    Simulator Adapter
```

## 7. Simulator Integration

Simulators are replaceable backends.

Candidates:

- Kart Racing Pro
- Assetto Corsa
- rFactor 2 / KartSim
- other kart-oriented simulation platforms

```text
                 KartSimDT Core
                       |
               Canonical Track
                       |
          +------------+------------+
          |            |            |
          v            v            v
         KRP           AC       rFactor/KartSim
          |            |            |
          +------------+------------+
                       |
                   Simulation
                       |
                   Telemetry
                       |
                       v
                 KartSimDT Core
```

## 8. Kart Racing Pro — Physics Backend Candidate

KRP is particularly interesting because its value is also its kart-oriented physics model.

The objective is **not** to create a new kart physics engine inside KartSimDT.

Instead:

```text
KartSimDT Kart Model
        |
        v
KRP Physics Adapter
        |
        v
KRP Kart / Engine / Physics Configuration
        |
        v
KRP Simulation
```

KartSimDT focuses on data, calibration, orchestration, telemetry, analysis and coaching.

## 9. Physics Calibration

Real telemetry should validate and calibrate the selected simulation backend.

```text
REAL KART
    |
    v
AIM / other telemetry
    |
    v
KartSimDT Core
    |
    +--------------------+
    |                    |
    v                    v
Reference Data       Simulation
                         |
                         v
                  Simulator Telemetry
                         |
                         v
                    Comparison
                         |
                         v
                 Physics Calibration
```

Relevant comparison dimensions include:

- lap time;
- speed profile;
- acceleration;
- braking;
- corner entry speed;
- minimum corner speed;
- exit speed;
- trajectory;
- throttle/brake behavior.

## 10. Digital Coach Direction

Digital Coach is a **parallel primary branch**, not a later Digital Twin feature.

Initial vision:

```text
Session Data Retrieval
        |
        v
Lap Analysis
        |
        v
Optimal Lap
        |
        v
Optimal Racing Line
        |
        v
Actual vs Optimal Comparison
        |
        v
Fault Detection
        |
        v
Correction
```

The Coach should ultimately identify where time was lost and provide actionable corrections.

## 11. Digital Twin + Digital Coach Feedback Loop

```text
REAL TRACK
    |
    v
Track Survey
    |
    v
KartSimDT Core
    |
    +----------------------+
    |                      |
    v                      v
DIGITAL TWIN          DIGITAL COACH
    |                      |
    v                      |
Simulator                  |
    |                      |
    v                      |
Simulation Session         |
    |                      |
    +----------+-----------+
               |
               v
           Telemetry
               |
               v
        KartSimDT Core
               |
               v
        Digital Coach
```

Target loop:

> **Real world → Digital Twin → Simulation → Telemetry → Digital Coach → improvement.**

## 12. Karting Physics Strategy

The first KartSimDT version should **not attempt to recreate every physics model internally**.

Exploit mature external physics engines where possible.

KartSimDT owns:

- kart specifications;
- driver data;
- telemetry;
- session/lap data;
- track data;
- physics calibration data;
- comparison and analysis.

The simulator owns real-time vehicle dynamics, tyre physics, engine dynamics, chassis dynamics and contact/surface physics.

## 13. Integration Principle

> **Build what is unique to KartSimDT. Integrate what already exists.**

Do not unnecessarily reproduce:

- Blender's modeling engine;
- mature SLAM implementations;
- established simulator physics;
- simulator rendering;
- existing track-building functionality.

Use adapters and canonical KartSimDT data contracts instead.

## 14. Aukštadvaris Role

Aukštadvaris is the **first real reference Digital Twin track**, not the platform architecture itself.

The architecture must remain independent of this particular track.

## 15. Current Development Priorities

### Priority 1 — Finish the minimum Blender Digital Twin

Evaluate the most efficient workflow for:

- 8 m working racing surface;
- terrain;
- kerbs;
- essential objects;
- simulator-ready track artifact.

Do not overbuild scenery.

### Priority 2 — Evaluate simulator backends

Compare:

- Kart Racing Pro;
- Assetto Corsa;
- rFactor 2 / KartSim.

Focus on physics quality, real-kart configurability, track import, telemetry access, external integration, automation and development cost.

### Priority 3 — Indoor Track Survey

Prototype:

```text
LiDAR + Camera + IMU
        |
        v
SLAM / Sensor Fusion
        |
        v
3D Track Survey
        |
        v
KartSimDT Track Model
```

### Priority 4 — Digital Coach foundation

Define data contracts for:

- session;
- lap;
- trajectory;
- speed;
- throttle;
- brake;
- steering;
- optimal lap;
- racing line;
- faults;
- corrections.

## 16. Fixed Architecture Decisions

1. KartSimDT Core is the platform orchestrator.
2. Digital Twin and Digital Coach are parallel primary branches.
3. Elevation is a first-class Track data product.
4. Outdoor and indoor Track Survey inputs are source-independent.
5. Indoor surveying prioritizes LiDAR + Camera + IMU + SLAM.
6. Blender is a Digital Twin construction application, not the Core.
7. `.blend` is an artifact, not the canonical Track model.
8. Simulators are replaceable backends accessed through adapters.
9. Kart Racing Pro is a leading candidate for kart physics backend.
10. KartSimDT should not initially implement a complete kart physics engine.
11. Real telemetry is used for physics validation/calibration and Digital Coach analysis.
12. Aukštadvaris is the first reference track, not the architecture.
13. Mature external technologies should be integrated rather than unnecessarily rebuilt.
14. Development decisions optimize total implementation time, cost, repeatability and integration quality.

## 17. Target Platform

```text
                         KARTSIMDT CORE
                              |
          +-------------------+-------------------+
          |                                       |
          v                                       v
     DIGITAL TWIN                            DIGITAL COACH
          |                                       |
    Track Survey                              Telemetry
    Track Model                              Session Data
    Blender                                  Lap Analysis
    Simulator                                Optimal Lap
          |                                  Racing Line
          |                                  Fault Detection
          |                                  Correction
          +-------------------+-------------------+
                              |
                              v
                         Driver / Engineer
```

Ultimate goal:

> **Real track + real kart + real session data → Digital Twin + Digital Coach → optimal lap, optimal racing line, fault identification and correction.**
