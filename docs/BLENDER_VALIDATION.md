# Blender Validation

## Objective

Validate KartSimDT generated centerline geometry against the engineering
reference centerline created in Blender.

---

## Reference Data

- Blender reference centerline
- KartSimDT generated centerline

---

## Workflow

```text
Reference Centerline

↓

Export JSON

↓

KartSimDT

↓

Generated Centerline

↓

Geometry Comparison

↓

Deviation Report
```

---

## Tasks

- [ ] Export Blender reference centerline
- [ ] Create JSON reference format
- [ ] Import reference geometry
- [ ] Compare centerlines
- [ ] Engineering report
- [ ] Validate deviations

---

## Deliverables

- Reference JSON
- Geometry comparison report
- Engineering validation report

---

## Acceptance Criteria

- Point count matches
- Coordinate system matches
- Reference origin matches
- Maximum deviation reported
- Average deviation reported