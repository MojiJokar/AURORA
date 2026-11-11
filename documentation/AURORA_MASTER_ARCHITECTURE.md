# AURORA — Master System Architecture

## 1. System Overview

AURORA (AI-Powered Autonomous UAV for Search, Inspection & Intelligent Mission Replanning) is a simulation-first autonomous UAV research and development project.

Its objective is to integrate:

- Computer vision and AI-based environmental perception.
- Simulated autonomous flight control.
- Object detection and tracking.
- Geospatial awareness and restricted-zone monitoring.
- Intelligent mission planning and route replanning.
- Ground-station communication and mission monitoring.

The primary application is Search & Rescue. Infrastructure Inspection is the secondary application.

Development and validation are currently performed in simulation. No physical UAV deployment is claimed.

## 2. High-Level Architecture

AURORA consists of two main operational systems connected through communication and data interfaces.

### Flight Control System

- Gazebo Harmonic provides the simulated environment.
- ArduPilot SITL controls the simulated aircraft.
- MAVLink provides communication with the flight controller.
- Mission Planner provides ground-station monitoring and mission interaction.

### AI Companion System

- Python provides the application framework.
- OpenCV processes camera imagery.
- YOLO supports AI-based object detection.
- Tracking maintains object observations across frames.
- AURORA-BRAIN evaluates perception and mission information.
- AURORA-GEOFENCE monitors geographical restrictions.
- AURORA-PLANNER evaluates alternative routes.

The AI companion is intended to support mission decisions without bypassing the flight controller's safety protections.

## 3. System Architecture Diagram

```text
                    AURORA UAV SYSTEM
                            |
             +--------------+--------------+
             |                             |
       FLIGHT CONTROL                 AI COMPANION
             |                             |
       ArduPilot SITL                 Python Framework
             |                             |
          MAVLink                     AURORA-VISION
             |                             |
       Gazebo Harmonic                 OpenCV + YOLO
             |                             |
      Simulated Camera               Object Detection
             |                             |
             |                       AURORA-TRACK
             |                             |
             |                       AURORA-BRAIN
             |                             |
             |                 +-----------+-----------+
             |                 |           |           |
             |             GEOFENCE     PLANNER     MONITOR
             |                 |           |           |
             +-----------------+-----------+-----------+
                               |
                        Mission Decisions
                               |
                         Ground Station
                         Mission Planner
```

This diagram represents the intended architecture. Not every module is implemented.

## 4. Main System Components

### 4.1 AURORA-SIM — Simulation

Provides the simulated UAV environment.

Responsibilities:
- Run Gazebo Harmonic.
- Provide the simulated aircraft and camera.
- Connect the simulation to ArduPilot SITL.
- Support repeatable simulation tests.

Status: Gazebo and ArduPilot SITL integration tested.

### 4.2 AURORA-VISION — Computer Vision

Processes imagery from the simulated UAV camera.

Responsibilities:
- Receive camera frames.
- Convert and process image data.
- Run AI-based object detection.
- Provide visual information to other modules.

Technologies: Python, OpenCV, YOLO.

Status: Live camera stream tested; initial YOLO evaluation performed. Reliable target detection remains under development.

### 4.3 AURORA-TRACK — Object Tracking

Intended to maintain object identities and observations across multiple frames.

Responsibilities:
- Associate detections between frames.
- Maintain object tracks.
- Estimate movement from successive observations.
- Provide tracking information to the decision system.

Status: Planned.

### 4.4 AURORA-BRAIN — Decision Intelligence

The intended decision-making component of AURORA.

Responsibilities:
- Interpret perception results.
- Evaluate mission context.
- Coordinate information from other modules.
- Support mission-level decisions.

Status: Planned.

### 4.5 AURORA-GEOFENCE — Geospatial Safety

Monitors planned flight routes against configured geographical restrictions.

Responsibilities:
- Represent restricted geographical areas.
- Monitor planned routes.
- Identify potential restricted-zone conflicts.
- Generate safety warnings.
- Provide conflict information to the planner and ground station.

Status: Planned.

### 4.6 AURORA-PLANNER — Intelligent Mission Planning

Evaluates mission routes and possible alternative paths.

Responsibilities:
- Analyse route conflicts.
- Calculate alternative routes.
- Evaluate proposed routes against mission constraints.
- Support safe detours.
- Support rejoining the original mission when appropriate.

Status: Planned.

### 4.7 AURORA-AUTONOMY — Mission Execution

Coordinates mission planning and flight execution through the flight-control interface.

Responsibilities:
- Support mission definition.
- Coordinate approved mission changes.
- Interface with ArduPilot through MAVLink.
- Monitor mission execution.

Status: Existing simulation flight-control integration is tested; intelligent autonomous replanning is planned.

### 4.8 AURORA-MONITOR — Ground Station Monitoring

Provides mission status and event reporting.

Responsibilities:
- Monitor relevant mission information.
- Report safety warnings.
- Communicate mission events to the ground station.
- Support Mission Planner integration.

Status: Mission Planner connection tested; AURORA-generated alerts are planned.

## 5. Data and Control Flow

The intended information flow is:

1. Gazebo provides simulated camera imagery.
2. AURORA-VISION receives and processes camera frames.
3. YOLO evaluates images for possible objects of interest.
4. AURORA-TRACK maintains observations across frames.
5. AURORA-BRAIN evaluates perception and mission context.
6. AURORA-GEOFENCE checks planned routes against restricted areas.
7. AURORA-PLANNER evaluates safe alternative routes when conflicts are identified.
8. AURORA-MONITOR reports relevant events to the ground station.
9. Approved mission changes can be communicated to ArduPilot through MAVLink.

The complete workflow is a development objective, not a currently operational capability.

## 6. Geofencing and Mission Replanning

Geospatial safety and intelligent mission replanning are important planned AURORA capabilities.

The intended workflow is:

1. Monitor the planned flight route.
2. Compare the route with configured restricted areas.
3. Detect potential route conflicts.
4. Generate a warning for the ground station.
5. Calculate a possible alternative route.
6. Validate the alternative against geographical and mission constraints.
7. Execute only an approved route.
8. Rejoin the original mission when safe and appropriate.

ArduPilot's native geofence functionality is intended to remain an independent safety backstop.

AURORA must not bypass or disable flight-controller safety protections.

Status: Design and implementation planned.

## 7. Primary Applications

### Search & Rescue — Primary Application

The primary application is simulated aerial search and mission support.

Intended capabilities:
- Analyse aerial camera imagery.
- Detect potential persons or objects of interest.
- Track relevant detections.
- Support search mission decisions.
- Monitor restricted geographical areas.
- Report mission events to the ground station.

### Infrastructure Inspection — Secondary Application

The secondary application is visual inspection of structures and infrastructure.

Intended capabilities:
- Capture and analyse infrastructure imagery.
- Identify visible objects and potential anomalies.
- Support repeatable inspection routes.
- Record observations for later evaluation.

## 8. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| OpenCV | Image processing |
| YOLO | Object detection |
| NumPy | Numerical and image operations |
| Gazebo Harmonic | UAV simulation |
| ArduPilot SITL | Simulated flight control |
| MAVLink | Flight-control communication |
| Mission Planner | Ground-station monitoring |
| Ubuntu Linux | Development environment |

AI inference currently runs on CPU hardware. CUDA acceleration is not assumed.

## 9. Engineering Constraints

- Development is simulation-first.
- No physical UAV deployment is claimed.
- CPU inference limits processing performance.
- Lightweight models and sampled frames are preferred.
- Simulation performance must be measured.
- Detection results require validation.
- Planned modules must not be described as implemented.
- Mission changes require safety validation before execution.

## 10. Safety and Validation

AURORA follows these safety principles:

- Preserve ArduPilot pre-arm checks and flight-controller safety functions.
- Keep native geofence protections independent.
- Do not execute unvalidated alternative routes.
- Validate mission behaviour in simulation.
- Separate tested capabilities from planned capabilities.
- Record test conditions, results, and limitations.
- Require repeatable tests before marking a feature complete.

## 11. Development Roadmap

### Phase 1 — Simulation Foundation
- Gazebo Harmonic environment.
- ArduPilot SITL integration.
- MAVLink communication.
- Mission Planner connection.

### Phase 2 — Computer Vision
- Live camera processing.
- YOLO model evaluation.
- Detection reliability testing.
- CPU performance evaluation.

### Phase 3 — Tracking and Awareness
- Object tracking.
- Observation continuity.
- Situational awareness.

### Phase 4 — Geospatial Safety
- Restricted-area representation.
- Route-conflict detection.
- Ground-station warnings.

### Phase 5 — Intelligent Planning
- Alternative-route calculation.
- Route validation.
- Safe mission continuation.
- Original-route rejoining.

### Phase 6 — System Integration
- Connect perception and decision-making.
- Integrate planning and monitoring.
- Validate complete workflows in simulation.
- Demonstrate Search & Rescue and Infrastructure Inspection scenarios.

---

**AURORA — From aerial perception to intelligent autonomous action.**