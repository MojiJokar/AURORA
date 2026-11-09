# AURORA — Command Reference

**Project:** Autonomous UAV Operations, Recovery and Navigation Architecture  
**Purpose:** Central reference for launching and checking the AURORA simulation environment.

---

## 1. Start Gazebo Harmonic

Open Terminal 1:

```bash
cd ~/uav_recovery/ardu_ws/src/ardupilot_gazebo

export GZ_SIM_SYSTEM_PLUGIN_PATH="$PWD/build:$GZ_SIM_SYSTEM_PLUGIN_PATH"
export GZ_SIM_RESOURCE_PATH="$PWD/models:$PWD/worlds:$GZ_SIM_RESOURCE_PATH"

gz sim -v4 -r worlds/iris_runway.sdf
```

Expected result: Gazebo opens and displays the Iris aircraft on the runway.

## 2. Start ArduPilot SITL

Open Terminal 2:

```bash
cd ~/uav_recovery/ardupilot

source ~/uav_recovery/ardupilot-venv/bin/activate

./Tools/autotest/sim_vehicle.py \
  -v ArduCopter \
  -f gazebo-iris \
  --model JSON \
  --map \
  --console \
  --no-rebuild
```

Expected result: ArduPilot SITL starts and MAVProxy connects.

## 3. Start Mission Planner

Open Terminal 3:

```bash
cd "$HOME/.wine/drive_c/Program Files (x86)/Mission Planner"

ulimit -n 8192

MONO_IOMAP=drive:case \
LD_LIBRARY_PATH="$PWD:/lib/x86_64-linux-gnu" \
mono MissionPlanner.exe
```

In Mission Planner, connect using:

- Connection type: UDP
- Port: 14550

Expected result: Mission Planner receives simulated vehicle telemetry.

## 4. Check vehicle status

In the MAVProxy terminal, enter:

```text
status
```

Check the vehicle's telemetry, GPS and EKF information.

## 5. Check frame configuration

In MAVProxy:

```text
param show FRAME_CLASS
param show FRAME_TYPE
```

Expected configuration:

```text
FRAME_CLASS = 1
FRAME_TYPE = 1
```

This represents a Quad X frame.

## 6. Check PreArm warnings

In Mission Planner:

1. Open the Messages tab.
2. Look for messages beginning with `PreArm:`.
3. Record any warnings.
4. Resolve warnings before attempting to arm the simulated aircraft.

**Safety rule:** Do not arm or take off until the PreArm warnings are resolved and the simulated vehicle's operation has been checked.

## 7. Stop the simulation

When finished, use:

```text
Ctrl + C
```

in the relevant terminal windows to stop the simulation processes.

If the vehicle has been armed during a later test, disarm it before stopping the simulation.

## 8. Troubleshooting

### Mission Planner: Too many open files

Before launching Mission Planner, run:

```bash
ulimit -n 8192
```

Then launch Mission Planner using the command in Section 3.

### Gazebo cannot find models or plugins

Check that the Gazebo environment variables in Section 1 have been set in the same terminal used to launch Gazebo.

### MAVProxy cannot load the wx module

A warning about the missing `wx` Python module may appear. It does not necessarily prevent SITL telemetry from working.

---

## 9. Project installation paths

| Component | Location |
|---|---|
| AURORA project | `/data/AURORA` |
| ArduPilot | `~/uav_recovery/ardupilot` |
| ArduPilot Python environment | `~/uav_recovery/ardupilot-venv` |
| Gazebo plugin repository | `~/uav_recovery/ardu_ws/src/ardupilot_gazebo` |
| Gazebo runway world | `~/uav_recovery/ardu_ws/src/ardupilot_gazebo/worlds/iris_runway.sdf` |
| Mission Planner | `~/.wine/drive_c/Program Files (x86)/Mission Planner` |

---

## 10. Development record

Record important changes and test results here.

### Milestone 1 — Simulation environment

- Gazebo Harmonic installed and tested.
- ArduPilot SITL installed and tested.
- Mission Planner launched and connected.
- Quad X frame configuration set.
- Autonomous flight not yet demonstrated.

### Milestone 2 — Autonomous flight

Status: In progress.

Planned tests:

- Verify GPS and EKF telemetry.
- Resolve all PreArm warnings.
- Verify simulated vehicle response.
- Perform a controlled simulated takeoff.
- Test waypoint mission execution.
- Test autonomous landing.

**Important:** Update this document as each test is completed. Only mark a feature as completed after it has been tested successfully.