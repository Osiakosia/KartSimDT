## Technical Debt — Telemetry MyPy Compatibility

### Status

Accepted / Deferred

### Scope

The existing telemetry subsystem is considered stable.

All existing telemetry tests pass, and the subsystem has already been validated
as part of earlier project work.

### Current MyPy Findings

`mypy src` currently reports five type-related errors in code consuming the
existing telemetry API:

- `survey/track_survey_3d/lap_gps_dataset_builder.py`
  - 4 errors caused by `TelemetrySession.channels.get()` being typed as
    `TelemetryChannel | None`.

- `survey/track_survey_3d/exporter.py`
  - 1 error caused by `elevation` being typed as `float | None`.

### Decision

These findings are NOT grounds for modifying the existing telemetry core
architecture at this stage.

The telemetry subsystem remains frozen while the Track Engineering architecture
is being developed.

No changes should be made to:

- `src/kartsimdt/telemetry/`
- existing telemetry channel contracts
- existing telemetry domain models

solely to satisfy MyPy.

### Rationale

The telemetry subsystem predates the current Track Engineering work and its
tests are passing.

Changing its core contracts now would introduce unnecessary regression risk
and would mix two separate architectural stages.

The current MyPy findings are therefore treated as known technical debt.

### Future Resolution

If telemetry type hardening is required later, it must be handled as a
dedicated refactoring task with the existing telemetry test suite used as the
regression gate.

Until that work is explicitly started, these findings should remain deferred.

### Current Track Engineering Priority

Development continues with the Track Engineering pipeline:

TrackContext
→ TrackDesign
→ RoadWidthResolver
→ RoadGeometryGenerator
→ RoadMesh
→ Blender adapter
→ TrackRoad
