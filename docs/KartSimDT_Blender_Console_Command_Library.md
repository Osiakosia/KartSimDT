# KartSimDT Blender Console Command Library

## Purpose

This document records the Blender Python Console commands used during the
Aukštadvaris TrackRoad construction and validation workflow.

The console is treated as a **development and diagnostic interface**, not as
the final implementation layer.

### Architecture rule

Commands fall into three groups:

1. **Diagnostics / inspection**
   - May remain in this library.
   - Useful for checking objects, geometry, elevation and topology.

2. **One-time scene setup**
   - Can be kept here for reference.
   - Should not become part of the reusable track-building workflow.

3. **Geometry generation / scene mutation**
   - Must eventually move into reusable Blender generators.
   - Example: `TrackRoadGenerator`, `TrackKerbGenerator`, `TrackTerrainGenerator`.

The final workflow should therefore be:

```text
KartSimDT Track Survey
        |
        v
canonical track data
        |
        v
Blender generators
        |
        +--> TrackRoad
        +--> TrackKerbs
        +--> TrackTerrain
        +--> TrackObjects
        |
        v
final Blender scene
        |
        v
simulator export
```

---

# 1. Blender object inspection

## List scene objects

```python
for obj in bpy.context.scene.objects:
    print(
        obj.name,
        "| type=", obj.type,
        "| location=", tuple(round(v, 3) for v in obj.location),
        "| scale=", tuple(round(v, 3) for v in obj.scale),
    )
```

## Inspect TrackSurvey

```python
obj = bpy.data.objects.get("TrackSurvey")
print(obj.name, obj.type)
```

## Inspect spline

```python
obj = bpy.data.objects["TrackSurvey"]
spline = obj.data.splines[0]

print("OBJECT:", obj.name)
print("TYPE:", obj.type)
print("SPLINE TYPE:", spline.type)
print("POINTS:", len(spline.points))
```

Expected Aukštadvaris result:

```text
OBJECT: TrackSurvey
TYPE: CURVE
SPLINE TYPE: POLY
POINTS: 677
```

---

# 2. TrackSurvey geometry inspection

## First, middle and last point

```python
obj = bpy.data.objects["TrackSurvey"]
points = obj.data.splines[0].points

print("P0:", tuple(points[0].co))
print("P338:", tuple(points[338].co))
print("P676:", tuple(points[676].co))
```

Aukštadvaris reference values observed during development:

```text
P0:
(0.0, 0.0, 0.0, 1.0)

P338:
(-199.23634338378906, -19.93812370300293, 3.448364019393921, 1.0)

P676:
(-0.15632426738739014, -0.541163444519043,
 -0.007079999893903732, 1.0)
```

## Elevation range

```python
obj = bpy.data.objects["TrackSurvey"]
points = obj.data.splines[0].points

print("POINTS:", len(points))
print("Z MIN:", min(p.co.z for p in points))
print("Z MAX:", max(p.co.z for p in points))
print("Z DELTA:", max(p.co.z for p in points) - min(p.co.z for p in points))
```

Observed Aukštadvaris values:

```text
POINTS: 677
Z MIN: -1.440322995185852
Z MAX: 3.991821050643921
Z DELTA: 5.432144045829773
```

---

# 3. TrackRoad creation — POC

This was the first working TrackRoad generator executed directly in the
Blender console.

```python
import mathutils

obj = bpy.data.objects["TrackSurvey"]
s = obj.data.splines[0]

pts = [p.co.xyz.copy() for p in s.points]

left = []
right = []

half = 4.0
n = len(pts)

[
    (
        lambda t: (
            left.append(
                p + mathutils.Vector((-t.y, t.x, 0)).normalized() * half
            ),
            right.append(
                p - mathutils.Vector((-t.y, t.x, 0)).normalized() * half
            ),
        )
    )(pts[(i + 1) % n] - pts[(i - 1) % n])
    for i, p in enumerate(pts)
]

me = bpy.data.meshes.new("TrackRoadMesh")

verts = [
    v
    for pair in zip(left, right, strict=True)
    for v in pair
]

faces = [
    (
        2 * i,
        2 * i + 1,
        2 * ((i + 1) % n) + 1,
        2 * ((i + 1) % n),
    )
    for i in range(n)
]

me.from_pydata(verts, [], faces)
me.update()

old = bpy.data.objects.get("TrackRoad")

if old:
    bpy.data.objects.remove(old, do_unlink=True)

road = bpy.data.objects.new("TrackRoad", me)
bpy.context.scene.collection.objects.link(road)

print(
    "TrackRoad:",
    len(me.vertices),
    "vertices,",
    len(me.polygons),
    "faces",
)
```

Expected:

```text
TrackRoad: 1354 vertices, 677 faces
```

### Important

This is a **POC implementation**.

It should eventually be replaced by:

```text
TrackRoadGenerator
```

with configurable:

```text
default_width_m
width_zones
```

rather than hard-coded:

```python
half = 4.0
```

---

# 4. TrackRoad topology validation

## Basic mesh statistics

```python
road = bpy.data.objects["TrackRoad"]
me = road.data

print("VERTICES:", len(me.vertices))
print("FACES:", len(me.polygons))
print("EDGES:", len(me.edges))
```

Observed:

```text
VERTICES: 1354
FACES: 677
EDGES: 2031
```

## Boundary and non-manifold edge check

Blender 5.1 `MeshEdge` does not provide `is_boundary`, so use polygon
edge usage instead:

```python
from collections import Counter

road = bpy.data.objects["TrackRoad"]

counts = Counter(
    e
    for p in road.data.polygons
    for e in p.edge_keys
)

print(
    "BOUNDARY EDGES:",
    sum(1 for c in counts.values() if c == 1),
)

print(
    "NON-MANIFOLD EDGES:",
    sum(1 for c in counts.values() if c > 2),
)

print(
    "EDGE USAGE:",
    Counter(counts.values()),
)
```

Observed:

```text
BOUNDARY EDGES: 1354
NON-MANIFOLD EDGES: 0
EDGE USAGE: Counter({1: 1354, 2: 677})
```

Interpretation:

- `1354` boundary edges are expected for this open road surface.
- `0` non-manifold edges means there are no invalid multi-face edges.
- The object is a surface strip, not a closed solid.

---

# 5. Selecting TrackRoad

```python
road = bpy.data.objects["TrackRoad"]

bpy.context.view_layer.objects.active = road
road.select_set(True)
```

---

# 6. Orthophoto visibility

## Hide orthophoto

```python
bpy.data.objects["Orthophoto"].hide_viewport = True
```

## Show orthophoto

```python
bpy.data.objects["Orthophoto"].hide_viewport = False
```

---

# 7. Orthophoto reference elevation

The Aukštadvaris TrackSurvey elevation range is approximately:

```text
-1.44 m ... +3.99 m
```

The orthophoto plane was at:

```text
Z = 0
```

Therefore lower parts of the 3D road could be hidden by the orthophoto.

Temporary reference-layer adjustment:

```python
bpy.data.objects["Orthophoto"].location.z = -1.6
```

This does **not** modify TrackSurvey or TrackRoad elevation.

### Architectural rule

Orthophoto is a:

```text
REFERENCE / VISUALIZATION LAYER
```

It is not the elevation source for TrackRoad.

---

# 8. Scene shading / viewport

## Set Material Preview

```python
bpy.context.space_data.shading.type = 'MATERIAL'
```

## Set Solid mode

```python
bpy.context.space_data.shading.type = 'SOLID'
```

---

# 9. Apply scale

Used during scene preparation:

```python
bpy.ops.object.transform_apply(
    location=False,
    rotation=False,
    scale=True,
)
```

Use carefully: this is a scene mutation operation and should normally be
performed deliberately, not repeatedly during generation.

---

# 10. Smooth shading

Used during visual preparation:

```python
bpy.ops.object.shade_smooth()
```

For the final Road Builder this should be handled explicitly by the
generator/material pipeline.

---

# 11. Temporary asphalt material

POC material:

```python
road = bpy.data.objects["TrackRoad"]

mat = (
    bpy.data.materials.get("TrackRoad_Asphalt")
    or bpy.data.materials.new("TrackRoad_Asphalt")
)

mat.diffuse_color = (0.08, 0.08, 0.08, 1)

road.data.materials.clear()
road.data.materials.append(mat)
```

This is a visualization POC, not the final simulator material pipeline.

---

# 12. Recommended final Blender generator structure

The console commands above should not become the permanent architecture.

Recommended:

```text
data/
└── tracks/
    └── <TrackName>/
        └── blender/
            ├── scene.blend
            ├── scene_transform.json
            └── road_config.json
```

and source code:

```text
src/
└── kartsimdt/
    └── blender/
        ├── generators/
        │   ├── track_road.py
        │   ├── track_kerbs.py
        │   ├── track_terrain.py
        │   └── track_objects.py
        │
        ├── materials/
        │   └── ...
        │
        └── ...
```

The first reusable generator should expose configuration conceptually like:

```python
TrackRoadGenerator(
    default_width_m=8.0,
    width_zones=...,
)
```

For Aukštadvaris:

```text
default road width = 8 m
start/finish width = 11 m
```

The actual zone indices belong to track data/configuration, not hard-coded
generator logic.

---

# 13. Current KartSimDT Blender status

```text
Track Survey 3D
    PASS

        ↓

TrackSurvey
    CURVE / POLY
    677 points
    PASS

        ↓

TrackRoad POC
    1354 vertices
    677 faces
    2031 edges
    PASS

        ↓

Road elevation
    inherited from TrackSurvey
    PASS

        ↓

Orthophoto alignment
    PASS after reference Z adjustment

        ↓

NEXT
    Parametric TrackRoadGenerator

        ↓

    8 m default road
    11 m start/finish zone

        ↓

    TrackKerbs

        ↓

    TrackTerrain

        ↓

    TrackObjects

        ↓

    Final Blender Track

        ↓

    Simulator export
```

---

# 14. Working rule for future development

Do not accumulate permanent functionality in the Blender Console.

Use the Console for:

- inspection;
- diagnostics;
- quick experiments;
- validating generator output.

Move reusable functionality into generators.

This keeps the Blender part repeatable for:

```text
Aukštadvaris
Šiauliai
Kandava
Plytinė
Smalininkai
Mande_Kart
future tracks
```

without creating track-specific Python branches.

---

# 15. Current decision

The current Aukštadvaris TrackRoad is a successful geometry POC.

Before kerbs, the next architectural task is:

**Create a reusable parameter-driven TrackRoadGenerator with configurable
road width zones, including the 11 m start/finish section.**

The existing console commands remain here as the development/diagnostic
library and historical record.
