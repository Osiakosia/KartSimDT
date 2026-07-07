# 📍 Track Survey Methodology

Version: 0.1

Status: Draft

---

# Purpose

Track Survey is the engineering process used by KartSimDT to create a validated
digital representation of a real kart racing circuit.

The objective is not only to record GPS trajectories, but to acquire all
reference information required for Digital Twin generation, visualization,
simulation and coaching.

---

# Objectives

The Track Survey session should collect:

- Track centerline
- Critical corner points
- Track width
- Reference objects
- GPS referenced photographs
- Elevation information
- Survey notes

The resulting dataset becomes the reference representation of the circuit.

---

# Survey Equipment

Minimum equipment:

- Android smartphone
- GPS Logger
- GPS Camera
- GPS Mapper

Recommended equipment:

- Measuring tape
- Laser range finder
- External GNSS receiver
- RTK receiver (future)

---

# Mobile Applications

| Application | Purpose |
|-------------|----------|
| GPS Logger | Centerline recording |
| GPS Mapper | Waypoints and critical points |
| GPS Camera | GPS referenced photographs |

---

# Survey Workflow

The complete survey follows the same engineering workflow.

```
Prepare

↓

Record Centerline

↓

Measure Critical Points

↓

Capture Reference Photos

↓

Collect Notes

↓

Validate Data

↓

Import into KartSimDT
```

---

# Centerline Acquisition

## Objective

Acquire the reference trajectory of the track.

## Procedure

- Walk along the center of the racing surface.
- Maintain a constant walking speed.
- Avoid unnecessary stops.
- Repeat the measurement 3–5 times.
- Export the result as GPX.

Future versions of KartSimDT may average multiple centerlines into a single
reference trajectory.

---

# Critical Point Survey

Every corner should contain four primary reference points.

```
ENTRY

↓

TURN-IN

↓

APEX

↓

EXIT
```

These points describe the driver's interaction with the track rather than only
its geometry.

---

## ENTRY

Beginning of the braking/preparation zone.

---

## TURN-IN

Location where steering input begins.

---

## APEX

Reference apex used by the optimal racing line.

---

## EXIT

Location where steering finishes and full acceleration begins.

---

# Optional Reference Points

Additional survey points improve future Digital Twin accuracy.

- Brake Marker
- Curb Start
- Curb End
- Elevation Change
- Surface Change

---

# Reference Photography

Every critical point should be documented with GPS referenced photographs.

Recommended photographs:

- Start / Finish
- Corner Entry
- Apex
- Corner Exit
- Brake markers
- Curbs
- Buildings
- Trees
- Safety barriers
- Marshal posts

Photos should always be taken facing the driving direction.

---

# Survey Notes

Record observations that cannot be derived from GPS.

Examples:

- Asphalt patch
- Bumps
- Curb usage
- Typical braking marker
- Surface condition
- Visibility

Voice notes are acceptable during acquisition.

---

# Data Organization

```
TrackSurvey/

centerline.gpx

waypoints.gpx

photos/

notes.txt
```

Future versions may additionally include:

```
track_width.csv

elevation.csv

survey.json
```

---

# Validation Checklist

Before leaving the circuit verify:

- GPX file recorded
- Waypoints recorded
- Photos contain GPS coordinates
- Correct date and time
- Notes saved
- Backup created

---

# Future Improvements

Future Track Survey versions may include:

- RTK GNSS
- LiDAR scanning
- Drone photogrammetry
- SLAM reconstruction
- Stereo camera mapping
- Automatic centerline extraction
- Automatic elevation reconstruction

---

# Integration with KartSimDT

Track Survey is one of the core data acquisition modules.

```
Track Survey

        │

        ▼

Track Geometry

        │

        ▼

Replay Engine

        │

        ▼

SimCoach

        │

        ▼

Digital Twin
```

The survey process creates the engineering foundation for all subsequent
platform modules.

---

# Engineering Principles

Track Survey follows the core KartSimDT philosophy.

- Reality before simulation.
- Measure before modeling.
- Validate before implementation.
- Build once. Reuse everywhere.
- Every survey should be repeatable.