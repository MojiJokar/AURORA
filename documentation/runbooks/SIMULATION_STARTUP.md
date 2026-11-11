# AURORA - Simulation Startup Guide

This guide explains how to start the AURORA simulation environment.

## 1. Start Gazebo - Terminal 1

    cd ~/uav_recovery/ardu_ws/src/ardupilot_gazebo
    export GZ_SIM_SYSTEM_PLUGIN_PATH="$PWD/build:$GZ_SIM_SYSTEM_PLUGIN_PATH"
    export GZ_SIM_RESOURCE_PATH="$PWD/models:$PWD/worlds:$GZ_SIM_RESOURCE_PATH"
    gz sim -v4 -r worlds/iris_runway.sdf

## 2. Start ArduPilot SITL - Terminal 2

    cd ~/uav_recovery/ardupilot
    source ~/uav_recovery/ardupilot-venv/bin/activate
    ./Tools/autotest/sim_vehicle.py -v ArduCopter -f gazebo-iris --model JSON --map --console --no-rebuild

## 3. Start Mission Planner - Terminal 3

    cd "/home/moji/.wine/drive_c/Program Files (x86)/Mission Planner"
    ulimit -n 8192
    MONO_IOMAP=drive:case LD_LIBRARY_PATH="$PWD:/lib/x86_64-linux-gnu" mono MissionPlanner.exe

Connect using UDP port 14550.

## 4. Verify the Simulated Aircraft

In MAVProxy, enter:

    status
    param show FRAME_CLASS
    param show FRAME_TYPE

Expected configuration:
- FRAME_CLASS = 1
- FRAME_TYPE = 1
- Aircraft frame = QUAD/X

## 5. Safety Checks

Before arming or taking off:
- Check GPS and EKF status.
- Check the Mission Planner Messages tab.
- Confirm there are no unresolved PreArm warnings.
- Confirm the simulated aircraft responds correctly to Gazebo.

Do not arm until these checks are complete.

## 6. Stop the Simulation

Disarm the aircraft if armed. Use Ctrl+C in the SITL and Gazebo terminals.

---

AURORA - Simulation first, safety always.
