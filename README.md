# AURORA

## AI-Powered Autonomous UAV for Search, Inspection & Intelligent Mission Replanning

AURORA is a simulation-first autonomous UAV project exploring the integration of artificial intelligence, computer vision, autonomous flight control, geospatial safety, and intelligent mission planning.

The project focuses on two primary application areas:

- **Search & Rescue** — aerial observation, object detection research, and mission support.
- **Infrastructure Inspection** — aerial imagery, visual analysis, and repeatable inspection missions.

AURORA is being developed and evaluated in simulation before any consideration of physical deployment.

---

## 1. Project Vision

The goal of AURORA is to develop an intelligent UAV system that can:

- Observe and interpret its surroundings using camera imagery.
- Identify objects and potential areas of interest.
- Monitor mission routes and restricted geographical areas.
- Detect potential route conflicts.
- Alert the ground station when a safety concern is identified.
- Plan and evaluate safer alternative routes.
- Support mission monitoring and reporting.

The long-term objective is to connect aerial perception with safe, intelligent mission decisions.

## 2. Main Applications

### Search & Rescue

- Observe simulated search areas using an onboard camera.
- Explore AI-assisted object detection.
- Support identification of possible search targets.
- Monitor mission routes and restricted geographical areas.
- Report mission events to the ground station.

### Infrastructure Inspection

- Capture and analyse infrastructure imagery.
- Identify visible objects and potential anomalies.
- Support repeatable inspection routes.
- Record observations for later evaluation.

## 3. Core System Capabilities

| Capability | Current Status |
|---|---|
| Gazebo UAV simulation | Tested |
| ArduPilot SITL integration | Tested |
| Mission Planner connection | Tested |
| Live Gazebo camera stream | Tested |
| Initial YOLO model evaluation | Initial testing |
| Reliable target detection | Under development |
| Object tracking | Planned |
| Geofence monitoring | Planned |
| Proximity and route-conflict monitoring | Planned |
| Mission Planner safety alerts | Planned |
| Intelligent route replanning | Planned |
| Autonomous mission execution | Planned |
| Mission monitoring and reporting | Planned |

Statuses describe the current development stage, not guaranteed operational performance.

## 4. System Architecture

AURORA is organised into modular components:

| Module | Responsibility |
|---|---|
| AURORA-SIM | Gazebo and ArduPilot simulation |
| AURORA-VISION | Camera processing and AI-based object detection |
| AURORA-TRACK | Object tracking and observation continuity |
| AURORA-BRAIN | Decision-making and mission intelligence |
| AURORA-GEOFENCE | Restricted-zone and geospatial safety monitoring |
| AURORA-PLANNER | Route planning and mission replanning |
| AURORA-AUTONOMY | Mission planning and execution |
| AURORA-MONITOR | Mission status, alerts, and reporting |

These modules represent the intended system architecture. Not all modules are implemented yet.

## 5. Geofencing & Intelligent Mission Replanning

An important planned capability is to make AURORA aware of restricted geographical areas and route conflicts.

The intended workflow is:

1. Monitor the planned UAV route.
2. Check the route against configured restricted areas.
3. Identify potential conflicts before entering restricted areas.
4. Notify the ground station and Mission Planner.
5. Calculate and evaluate a safe alternative route.
6. Validate the alternative route against mission constraints.
7. Execute only an approved route.
8. Rejoin the original mission when it is safe to do so.

ArduPilot's native geofence functionality is intended to remain an independent safety backstop. AURORA is not intended to bypass or disable flight-controller safety protections.

This capability is part of the development roadmap and is not yet implemented.

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| OpenCV | Image processing |
| YOLO | Object detection experiments |
| NumPy | Image and numerical processing |
| Gazebo Harmonic | UAV simulation |
| ArduPilot SITL | Simulated flight control |
| MAVLink | Flight-control communication |
| Mission Planner | Ground station and mission monitoring |
| Ubuntu Linux | Development environment |

AI inference is currently evaluated on the CPU. CUDA acceleration is not assumed or required.

## 7. Development Roadmap

### Phase 1 — Simulation Foundation
- Set up Gazebo Harmonic.
- Integrate ArduPilot SITL.
- Establish Mission Planner communication.
- Verify simulated aircraft operation.

### Phase 2 — Computer Vision
- Access the simulated UAV camera.
- Process live camera frames.
- Evaluate lightweight YOLO models.
- Improve detection reliability and performance.

### Phase 3 — Tracking and Awareness
- Develop object tracking.
- Maintain observations across camera frames.
- Establish a foundation for situational awareness.

### Phase 4 — Geospatial Safety
- Define restricted geographical areas.
- Monitor planned routes against restricted areas.
- Detect route conflicts.
- Generate ground-station safety alerts.

### Phase 5 — Intelligent Mission Planning
- Develop safe alternative-route calculations.
- Validate proposed detours.
- Support safe mission continuation.
- Explore rejoining the original mission.

### Phase 6 — System Integration
- Connect perception, decision-making, and navigation.
- Integrate mission monitoring and reporting.
- Validate behaviour in controlled simulation scenarios.
- Demonstrate Search & Rescue and Infrastructure Inspection workflows.

## 8. Engineering Principles

AURORA follows these development principles:

- **Simulation first:** validate functionality in simulation before considering physical deployment.
- **Safety first:** preserve flight-controller safety protections.
- **Modular design:** keep perception, planning, control, and monitoring components separate.
- **CPU-friendly development:** favour lightweight models and practical processing requirements.
- **Measured performance:** document actual test results rather than assuming real-time capability.
- **Incremental validation:** test each component before integrating it into the complete system.

## 9. Repository Structure

```text
AURORA/
├── commands/
│   └── AURORA_COMMANDS.md
├── documentation/
│   ├── AURORA_MASTER_ARCHITECTURE.md
│   └── runbooks/
│       └── SIMULATION_STARTUP.md
├── vision/
│   └── live_camera.py
├── .gitignore
└── README.md
```

Additional modules and documentation will be added as development progresses.

## 10. Current Limitations

- The project is currently simulation-focused.
- No physical UAV deployment is claimed.
- Object detection requires further evaluation and validation.
- Reliable target identification has not yet been established.
- Object tracking is not yet implemented.
- Geofence monitoring and intelligent replanning are planned capabilities.
- Current simulation and image-processing performance is limited by available CPU resources.
- Autonomous route changes must be validated in controlled simulation before being considered operational.

## 11. Project Objective

AURORA aims to progress from a working simulated UAV environment toward an integrated intelligent aerial system combining:

**Computer Vision + Artificial Intelligence + Geospatial Safety + Autonomous Mission Planning**

The project will evolve through measurable development milestones, documented testing, and safety-focused simulation.

---

**AURORA — From aerial perception to intelligent autonomous action.**
