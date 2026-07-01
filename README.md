# 📘 KartSimDT

> **Engineering the Digital Future of Kart Racing**

Telemetry → Track → Vehicle → Physics → Digital Twin → Optimization

**Kart Simulation Digital Twin Toolkit**

An open engineering and research platform for transforming real-world kart racing telemetry into validated Digital Twins for simulation, analysis, optimization, and scientific research.

---

# 🎯 Project Vision

KartSimDT is an engineering platform designed to reconstruct real kart racing circuits using telemetry, geospatial data, and physics-based simulation.

The project combines software engineering, telemetry analysis, computational geometry, and vehicle dynamics into a unified Digital Twin platform.

The long-term objective is to create reproducible and validated digital representations of kart tracks that support engineering research, simulation, and performance optimization.

---

# 🏗 Platform Architecture

```
                    KartSimDT

              Engineering Platform

                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   Import Layer    Core Domain    Applications
        │               │               │
        ▼               ▼               ▼
 Telemetry       Digital Twin      Blender
 GIS             Physics           Assetto Corsa
 Images          Simulation        Research
```

---

# ✨ Main Features

## 📡 Telemetry

- AIM Sports telemetry import
- Automatic lap detection
- Channel validation
- Session analysis
- Multi-session comparison

---

## 🗺 Track Reconstruction

- Google Earth KML import
- Orthophoto import
- Centerline reconstruction
- Elevation reconstruction
- 3D track generation

---

## 🚗 Digital Twin

- Complete digital track model
- Modular architecture
- Vehicle models
- Physics-based simulation

---

## 📈 Optimization

- Racing line optimization
- Driver comparison
- Corner analysis
- AI-assisted research

---

## 📂 Reference Data

- AIM telemetry
- Google Earth KML
- Orthophotos
- Validation datasets
- Reference tracks

---

## 📤 Export

- Blender
- Unity
- CSV
- KML
- Future simulation formats

---

# 📊 Current Development Status

| Module | Status |
|----------|:------:|
| Documentation | 🟢 |
| Project Architecture | 🟢 |
| AIM CSV Reader | 🟢 |
| AIM Validator | 🟢 |
| AIM Channel Mapper | 🟡 |
| Telemetry Domain | ⚪ |
| Track Reconstruction | ⚪ |
| Physics Engine | ⚪ |
| Digital Twin | ⚪ |

---

# 🛣 Development Roadmap

| Version | Status | Description |
|----------|:------:|-------------|
| v0.1 | 🟢 | Project foundation |
| v0.2 | 🟡 | AIM telemetry import |
| v0.3 | ⚪ | Google Earth KML |
| v0.4 | ⚪ | Track reconstruction |
| v0.5 | ⚪ | Digital Twin Core |
| v0.6 | ⚪ | Vehicle models |
| v0.7 | ⚪ | Physics engine |
| v0.8 | ⚪ | Optimization |
| v0.9 | ⚪ | Validation |
| v1.0 | ⚪ | Research Platform |

---

# ⚙ Technology Stack

## Programming

- Python 3.13+

## Scientific Computing

- NumPy
- Pandas
- SciPy
- Matplotlib

## GIS & Geometry

- Shapely
- PyProj
- lxml

## Computer Vision

- OpenCV

## Development

- black
- ruff
- mypy
- pytest
- pre-commit

---

# 📁 Repository Structure

```
KartSimDT/

docs/
data/
examples/
tests/

src/
└── kartsimdt/
    ├── core/
    ├── io/
    ├── telemetry/
    ├── geometry/
    ├── track/
    ├── terrain/
    ├── vehicle/
    ├── simulation/
    ├── optimization/
    ├── adapters/
    └── utils/
```

---

# 🔄 Development Workflow

Every engineering task follows the same workflow.

```
Plan
    │
    ▼
Architecture
    │
    ▼
Implementation
    │
    ▼
black
    │
    ▼
ruff
    │
    ▼
mypy
    │
    ▼
pytest
    │
    ▼
Documentation
    │
    ▼
Git Commit
```

---

# 🌳 Branch Strategy

```
KartSimDT
      │
      ├──────────────┐
      │              │
      ▼              ▼
    Main         Applied
      │              │
      ▼              ▼
 Stable Core   Engineering Validation
                     │
                     ▼
              Assetto Corsa
```

The **Applied** branch continuously validates the Core architecture using real engineering demonstrators.

---

# 📚 Documentation

Project documentation is located in the `docs/` directory.

| Document | Description |
|----------|-------------|
| 📘 Style Guide | Engineering standards |
| 🏗 Architecture | System architecture |
| 🛣 Roadmap | Development roadmap |
| 📈 Development | Current project status |
| 📑 Design Decisions | Architecture decisions |
| 📥 AIM Import | AIM telemetry specification |

---

# 💡 Project Philosophy

KartSimDT is developed according to engineering-first principles.

- Architecture before implementation
- Validation before assumptions
- Physics before visualization
- Digital Twins built from reality

---

# 📄 License

Distributed under the MIT License.

---

# 🚧 Project Status

KartSimDT is under active development.

The current focus is building a robust engineering foundation before expanding into full Digital Twin simulation and optimization.

---

> **Engineering the Digital Future of Kart Racing**