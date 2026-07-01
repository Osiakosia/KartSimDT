# 📘 KartSimDT Style Guide

## 📄 Document Information

| Property | Value |
|----------|-------|
| Document | STYLE GUIDE |
| Version | v1.0 |
| Status | Active |
| Last Updated | 2026-07-01 |

---

# 🎯 Purpose

This document defines the engineering, coding, documentation, and development standards used throughout the KartSimDT project.

Its purpose is to establish a consistent engineering methodology that guides the development of the entire Digital Twin platform.

The Style Guide serves as the primary engineering reference for every contributor and every project module.

The standards defined in this document apply to:

- Software architecture
- Python source code
- Documentation
- Testing
- Version control
- Engineering workflow
- Project organization

Consistency across all engineering disciplines is considered a fundamental project requirement.

---

# 🏗 Engineering Principles

KartSimDT is developed as an engineering-grade Digital Twin platform.

Every engineering decision should support the project's long-term vision.

The following principles guide all development activities.

## Core Principles

- Architecture before implementation.
- Domain before visualization.
- Physics before graphics.
- Test before integration.
- Digital Twin before rendering.

## Engineering Principles

- Design before coding.
- Explicit over implicit.
- Strong typing by default.
- One responsibility per module.
- One responsibility per class.
- One responsibility per function.
- Small, composable components.
- Engineering decisions should be documented.
- Every module should remain maintainable.
- Avoid unnecessary complexity.

## Platform Principles

KartSimDT Core shall remain independent from:

- Visualization software
- Simulation software
- Telemetry vendors
- Hardware vendors
- Rendering engines

External systems are integrated through adapters rather than becoming part of the Core.

---

# 🧠 Consistency Principle

Engineering consistency is one of the fundamental goals of KartSimDT.

Consistency reduces cognitive load, improves maintainability, and simplifies long-term development.

Every engineering artifact should follow the same conventions.

This includes:

- Source code
- Documentation
- Project structure
- Naming conventions
- Testing
- Git history
- Engineering terminology

A developer should immediately recognize:

- document purpose
- engineering context
- module responsibility
- project status

without learning a different structure for each module.

Consistency is considered an engineering feature rather than a cosmetic preference.

---

# 🔄 Development Workflow

Every implementation follows the same engineering workflow.

```text
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
    │
    ▼
Sprint Review
```

A feature is considered complete only after every stage has been successfully completed.

> [!IMPORTANT]
> Passing all quality gates is mandatory before creating a Git commit.

---

# 📁 Project Structure Standards

KartSimDT is organized as a collection of independent engineering domains.

Each module has a clearly defined responsibility.

The architecture follows the Digital Twin philosophy.

```
External Data
        │
        ▼
Import Layer
        │
        ▼
Core Domain
        │
        ▼
Analysis
        │
        ▼
Simulation
        │
        ▼
Applications
```

Every external technology must communicate with the Core through dedicated adapters.

The Core must never depend on:

- Blender
- Assetto Corsa
- Unity
- AIM
- MoTeC
- RaceBox
- Any visualization platform

Applications depend on the Core.

The Core never depends on applications.

---

# 🐍 Python Standards

KartSimDT follows modern Python development practices.

## Python Version

- Python 3.13+

## General Rules

- Follow PEP 8.
- UTF-8 encoding.
- Four-space indentation.
- Use `from __future__ import annotations`.
- Prefer explicit code over implicit behavior.
- Prefer readability over cleverness.

## Typing

- Type hints are mandatory.
- Public APIs must always be typed.
- Internal functions should be typed whenever practical.

## Formatting

- Use f-strings.
- Keep functions focused on a single responsibility.
- Prefer composition over inheritance.
- Avoid global state whenever possible.

## Dependencies

External dependencies should be minimized.

A dependency must provide clear engineering value before being introduced into the project.

> [!NOTE]
> KartSimDT prioritizes maintainability and long-term stability over rapid feature development.
> 
> ---
---

# 🏷 Naming Conventions

Consistent naming improves readability, maintainability, and engineering communication.

The following naming conventions apply throughout the project.

| Element | Convention | Example |
|---------|------------|---------|
| Class | PascalCase | SessionManager |
| Function | snake_case | load_data |
| Method | snake_case | validate_input |
| Variable | snake_case | sample_count |
| Constant | UPPER_CASE | DEFAULT_TIMEOUT |
| Module | snake_case | validator.py |
| Package | snake_case | telemetry |
| Enum | PascalCase | DataType |

## Naming Rules

Names should:

- describe engineering intent
- remain consistent across the project
- avoid unnecessary abbreviations
- reflect the engineering domain

Avoid generic names whenever possible.

Prefer descriptive names that clearly express responsibility.

---

# 🧩 Type Hints

KartSimDT uses static typing throughout the project.

Static typing improves:

- readability
- maintainability
- IDE assistance
- static analysis

Type annotations should be used consistently across public APIs.

## Preferred Types

| Category | Preferred Style |
|-----------|-----------------|
| List | list[...] |
| Dictionary | dict[..., ...] |
| Set | set[...] |
| Optional | Type \| None |
| Return values | Explicitly declared |

Avoid ambiguous or implicit types whenever practical.

---

# 📝 Docstrings

Public modules, classes, and functions should include English docstrings.

Docstrings should describe:

- purpose
- responsibility
- parameters
- return values

Docstrings should explain engineering intent rather than implementation details.

## Good Practice

Describe:

- what the component is responsible for
- why it exists
- what it produces

Avoid describing every implementation step.

---

# 📦 Imports

Imports should always be grouped in the following order.

1. Standard Library

2. Third-party Libraries

3. Project Modules

## Import Rules

- Import only required modules.
- Avoid wildcard imports.
- Remove unused imports.
- Keep imports grouped.
- Keep imports alphabetically ordered within each group.

The import section should remain compact and easy to read.

---

# ⚠ Exception Handling

Engineering failures should be communicated using descriptive exceptions.

Exception messages should explain the engineering problem rather than implementation details.

## Good Examples

- Required input is missing.
- Invalid configuration value.
- Unsupported file format.

## Poor Examples

- Error.
- Invalid.
- Failed.

Meaningful exception messages significantly simplify debugging.

---

# ✅ Code Quality

Every implementation must successfully pass all quality gates.

## Required Tools

| Tool | Purpose |
|-------|----------|
| black | Code formatting |
| ruff | Linting |
| mypy | Static type checking |
| pytest | Automated testing |

## Quality Pipeline

```text
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
```

> [!IMPORTANT]
> Code should never be committed before every quality gate has passed.

---

# 🧪 Testing Standards

Testing is considered part of implementation.

Every completed feature should include automated tests.

## Unit Tests

Verify individual components independently.

## Integration Tests

Verify complete engineering workflows.

## Regression Tests

Prevent previously solved problems from reappearing.

## Engineering Rule

A feature is considered complete only when:

- implementation is finished
- formatting passes
- linting passes
- static analysis passes
- automated tests pass
- documentation is updated

Only then should the implementation be committed.

---

# 🌿 Git Workflow

KartSimDT follows a structured Git workflow to ensure traceability, consistency, and maintainability.

## Branches

| Branch | Purpose |
|---------|---------|
| `main` | Stable KartSimDT Core development |
| `applied` | Engineering demonstrators and validation |

Development should be performed in small, logical engineering steps.

Each commit should represent one completed engineering milestone.

---

## Commit Strategy

A commit should contain:

- one completed feature
- one completed refactoring
- one completed documentation update
- one completed engineering milestone

Avoid mixing unrelated changes within the same commit.

> [!TIP]
> Small commits are easier to review, debug, and maintain.

---

## Commit Sequence

```text
Implementation
        │
        ▼
Formatting
        │
        ▼
Quality Checks
        │
        ▼
Documentation
        │
        ▼
Git Commit
```

---

# 🌳 Branch Strategy

KartSimDT development is separated into two engineering branches.

```
KartSimDT
      │
      ├──────────────┐
      │              │
      ▼              ▼
   Main          Applied
      │              │
      ▼              ▼
 Stable Core   Engineering Validation
```

---

## Main Branch

Responsible for:

- Core architecture
- Domain models
- Physics engine
- Simulation engine
- Stable releases

---

## Applied Branch

Responsible for:

- Digital Twin demonstrators
- Assetto Corsa integration
- Track validation
- Real telemetry validation
- Experimental engineering

The Applied Branch validates the Core architecture but never replaces it.

---

# 📚 Documentation Standards

Documentation is considered an engineering artifact.

Every important engineering decision should be documented.

Documentation must remain synchronized with the implementation.

---

## Documentation Language

| Component | Language |
|-----------|----------|
| Discussions | Lithuanian |
| Documentation | English |
| Source Code | English |
| Comments | English |
| Docstrings | English |
| Git Messages | English |

---

## Documentation Principles

Documentation should explain:

- purpose
- architecture
- engineering decisions
- workflows

Avoid documenting implementation details that can be understood directly from the source code.

---

# 🎨 Documentation Visual Style

KartSimDT documentation follows a unified visual language.

Every document should be immediately recognizable as part of the project.

---

## Section Icons

| Icon | Meaning |
|------|---------|
| 📘 | Main document |
| 📄 | Document information |
| 🎯 | Purpose |
| 🏗 | Architecture |
| 🔄 | Workflow |
| 📁 | Structure |
| 🐍 | Python |
| 🏷 | Naming |
| 🧩 | Type System |
| 📝 | Documentation |
| 📦 | Modules |
| ⚠ | Exceptions |
| ✅ | Quality |
| 🧪 | Testing |
| 🌿 | Git |
| 🌳 | Branches |
| 📚 | Documentation |
| 📑 | Markdown |
| 📊 | Progress |
| 💬 | Commits |
| 📐 | Engineering Rules |
| 📌 | Summary |

---

## Engineering Diagrams

ASCII diagrams should be preferred whenever they improve readability.

Example

```text
Reader
    │
    ▼
Validator
    │
    ▼
Mapper
    │
    ▼
Telemetry Session
```

---

## Tables

Markdown tables should be used for:

- standards
- conventions
- progress
- configuration
- comparisons

Tables should remain concise and consistently formatted.

---

## Callout Blocks

Use GitHub Markdown callouts when emphasizing important information.

Available callouts include:

- NOTE
- TIP
- IMPORTANT
- WARNING

Callouts should be used sparingly to maintain readability.

---

# 📑 Markdown Standards

Every engineering document should follow the same structure.

Recommended document layout:

1. 📄 Document Information
2. 🎯 Purpose
3. 🏗 Main Content
4. 📌 Summary

Section titles should remain concise and descriptive.

Use consistent heading levels throughout every document.

Separate major sections using horizontal rules (`---`).

Prefer Markdown tables over plain text when presenting structured information.

Documentation should prioritize clarity over visual complexity.

---

# 📊 Progress Visualization

KartSimDT uses a unified progress visualization system across the entire project.

Progress indicators provide a quick overview of engineering status and should remain synchronized with the implementation.

---

## Sprint Status

| Symbol | Status | Description |
|:------:|--------|-------------|
| ⚪ | Not Started | Work has not yet begun |
| 🟡 | In Progress | Active development |
| 🟢 | Complete | Engineering implementation completed |
| 🔵 | Validated | Verified using real-world data or demonstrators |
| 🔴 | Blocked | Progress temporarily blocked |

---

## Task Status

Development tasks use standard Markdown checkboxes.

| Symbol | Meaning |
|---------|---------|
| `[ ]` | Not Started |
| `[x]` | Complete |

Example

```text
Sprint 2.3 — Validator

[x] Validate structure
[x] Validate timestamps
[x] Validate required channels
[ ] Create integration tests
```

---

## Engineering Workflow

Every engineering task follows the same lifecycle.

```text
⚪ Planned
        │
        ▼
🟡 In Development
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
        │
        ▼
🟢 Complete
        │
        ▼
🔵 Validated
```

---

## Project Progress

Major project documents should include a sprint progress table whenever appropriate.

Example

| Sprint | Status |
|---------|:------:|
| Module Foundation | 🟢 |
| CSV Reader | 🟢 |
| Validator | 🟢 |
| Channel Mapping | ⚪ |
| Metadata Extraction | ⚪ |
| Lap Detection | ⚪ |

Progress indicators should always reflect the actual engineering state.

---

# 💬 Commit Message Convention

KartSimDT follows the Conventional Commits specification.

## Recommended Types

| Type | Purpose |
|------|---------|
| feat | New functionality |
| fix | Bug fix |
| refactor | Internal improvements |
| docs | Documentation |
| test | Testing |
| style | Formatting and style |
| chore | Maintenance |

---

## Examples

```text
feat(aim): implement channel mapper

fix(parser): handle empty metadata

refactor(core): simplify telemetry model

docs(style): establish engineering standards

test(validator): add timestamp validation

style(reader): apply formatting

chore(ci): update development workflow
```

Commit messages should be concise, descriptive, and represent a single engineering milestone.

---

# 📐 Engineering Rules

The following engineering rules apply throughout the KartSimDT project.

## General Rules

- Complete one sprint before starting the next.
- Complete one engineering milestone per commit.
- Keep implementation and documentation synchronized.
- Maintain clear module responsibilities.
- Prefer simplicity over unnecessary complexity.
- Avoid premature optimization.
- Document important engineering decisions.

---

## Architecture Rules

- The Core must remain platform independent.
- External systems communicate through adapters.
- Applications depend on the Core.
- The Core never depends on applications.
- Maintain a clear separation between domain logic and infrastructure.

---

## Development Rules

- Pass all quality gates before committing.
- Never ignore failing tests.
- Refactoring should preserve functionality.
- New features should include tests whenever practical.
- Keep technical debt under control.

---

## Documentation Rules

- Documentation is part of implementation.
- Keep documentation synchronized with the source code.
- Use consistent terminology.
- Follow the KartSimDT Documentation Design Language.
- Prefer diagrams and tables over long paragraphs where appropriate.

> [!IMPORTANT]
> Engineering quality is measured not only by working software, but also by maintainability, traceability, and documentation quality.

---

# 📌 Summary

The KartSimDT Style Guide defines the engineering standards governing the entire project.

It establishes common rules for architecture, implementation, documentation, testing, version control, and project organization.

Following these standards ensures that KartSimDT remains consistent, maintainable, scalable, and aligned with its long-term vision of becoming an engineering-grade Digital Twin platform.
