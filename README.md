# AURORA --- Autonomous UAV Operations, Recovery and Navigation Architecture

> **Project status:** Development / simulation baseline\
> **Platform:** Ubuntu 22.04.5 LTS\
> **Purpose:** A single integrated UAV project for autonomous
> navigation, perception, obstacle avoidance, precision landing and
> intelligent recovery.

AURORA is the working project name for this development effort. The
capabilities described in the roadmap are targets; they are not all
implemented yet.

------------------------------------------------------------------------

## 1. Project goals

Build and demonstrate one integrated UAV system that can:

1.  Execute autonomous missions using ArduPilot.
2.  Simulate the aircraft and environment in Gazebo Harmonic.
3.  Integrate perception sensors (camera and LiDAR/rangefinder).
4.  Detect obstacles and support navigation decisions.
5.  Identify a landing target and perform precision landing.
6.  Monitor mission/vehicle state and record useful logs.

## 2. Current development status

  -----------------------------------------------------------------------
  Component                           Current status
  ----------------------------------- -----------------------------------
  Ubuntu 22.04.5                      Installed and working

  Gazebo Harmonic 8.15.0              Launches; Iris model visible in
                                      runway world

  ArduPilot SITL                      Starts with the Gazebo Iris JSON
                                      model

  MAVProxy                            Starts and forwards MAVLink to UDP
                                      `14550`

  Mission Planner 1.3.82              Launches under Mono and has
                                      connected to SITL over UDP

  ROS 2                               Not yet installed/integrated

  Camera/LiDAR data integration       Not yet verified

  Autonomous takeoff/mission/landing  Not yet demonstrated

  Precision landing / obstacle        Planned
  avoidance                           
  -----------------------------------------------------------------------

**Safety/status note:** The setup has been connected for telemetry, but
a successful simulated takeoff and landing have not yet been verified. A
previous ArduCopter startup showed a frame/pre-arm warning. Check the
current pre-arm status and simulator behavior before attempting to arm.
Do not treat a connected HUD or GPS display as proof that flight
controls and simulated motors are working.

## 3. Storage and project directories

The dedicated AURORA data partition is mounted at `/data`:

``` text
/data/AURORA/
├── simulation/       # Gazebo worlds and simulation results
├── sensor_data/      # Camera, LiDAR and GPS recordings
├── logs/             # Flight and telemetry logs
├── models/            # UAV and landing-pad models
├── documentation/    # Project documents
└── backups/           # Project backups
```

Check that the data partition is mounted and has space:

``` bash
findmnt /data
df -h /data
```

The ArduPilot/Gazebo source trees currently remain in the home
directory. Do not move them without updating paths and testing the
launch setup.

## 4. Known installation paths

``` text
ArduPilot source:
~/uav_recovery/ardupilot

ArduPilot Python virtual environment:
~/uav_recovery/ardupilot-venv

ArduPilot Gazebo plugin repository:
~/uav_recovery/ardu_ws/src/ardupilot_gazebo

Gazebo world:
~/uav_recovery/ardu_ws/src/ardupilot_gazebo/worlds/iris_runway.sdf

Mission Planner executable:
~/.wine/drive_c/Program Files (x86)/Mission Planner/MissionPlanner.exe
```

## 5. Start the simulation

Use **three separate terminal windows**. Start Gazebo first, then
ArduPilot SITL, then Mission Planner.

### Terminal 1 --- Gazebo Harmonic

``` bash
cd ~/uav_recovery/ardu_ws/src/ardupilot_gazebo

export GZ_SIM_SYSTEM_PLUGIN_PATH="$PWD/build:$GZ_SIM_SYSTEM_PLUGIN_PATH"
export GZ_SIM_RESOURCE_PATH="$PWD/models:$PWD/worlds:$GZ_SIM_RESOURCE_PATH"

gz sim -v4 -r worlds/iris_runway.sdf
```

Expected result: Gazebo opens the `iris_runway` world and displays the
Iris aircraft on the runway.

### Terminal 2 --- ArduPilot Copter SITL + MAVProxy

``` bash
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

Expected result: ArduCopter SITL starts and MAVProxy opens with a prompt
such as:

``` text
STABILIZE>
```

MAVProxy has previously shown a GCS output to UDP `127.0.0.1:14550`,
which is the port used by Mission Planner in this setup.

If the virtual environment is no longer active in this terminal,
activate it again with:

``` bash
source ~/uav_recovery/ardupilot-venv/bin/activate
```

### Terminal 3 --- Mission Planner (Mono)

The Linux file-descriptor limit previously caused a
`Too many open files` error. Raise the limit in the same terminal before
launching Mission Planner:

``` bash
cd "$HOME/.wine/drive_c/Program Files (x86)/Mission Planner"

ulimit -n 8192

MONO_IOMAP=drive:case \
LD_LIBRARY_PATH="$PWD:/lib/x86_64-linux-gnu" \
mono MissionPlanner.exe
```

In Mission Planner:

1.  Select **UDP** as the connection type.
2.  Use port **14550** if prompted.
3.  Connect and confirm that telemetry is being received.

The `ulimit` setting applies to this terminal session. Repeat it
whenever launching Mission Planner from a new terminal.

## 6. Useful MAVProxy checks

At the MAVProxy prompt (for example, `STABILIZE>`), these read-only
commands can help inspect the connection:

``` text
status
param show FRAME_CLASS
param show FRAME_TYPE
```

The frame parameters were previously set to:

``` text
FRAME_CLASS = 1
FRAME_TYPE  = 1
```

The vehicle previously reported `Frame: QUAD/X`. Verify the current
values and current pre-arm messages; do not assume an earlier setting
guarantees that all checks now pass.

MAVProxy has previously forwarded telemetry to:

``` text
127.0.0.1:14550
```

## 7. Stopping the simulation

1.  If the vehicle is armed, disarm it through the appropriate
    simulator/ground-station control before shutting down.
2.  In each terminal, press `Ctrl+C` to stop its process.
3.  Stop SITL and Gazebo cleanly; do not force-kill processes unless
    they are unresponsive.

No takeoff/landing test is documented as completed yet.

## 8. Troubleshooting notes

### Mission Planner: `Too many open files`

Launch it from a terminal after running:

``` bash
ulimit -n 8192
```

Then use the Mission Planner launch command in Section 5.

### MAVProxy warning: missing `wx`

A message such as `Failed to load module: No module named 'wx'` has
appeared. The optional wx GUI module may be unavailable; MAVLink
telemetry forwarding has worked without it.

### Gazebo plugin/model paths

The Gazebo launch command sets both plugin and resource paths. Run it
from the `ardupilot_gazebo` repository directory so `$PWD` points to the
correct location.

### ArduPilot pre-arm warning

A frame/pre-arm warning appeared during earlier startup. Verify current
messages and simulator readiness before arming. Do not bypass pre-arm
checks merely to make a test proceed.

## 9. Planned architecture

``` text
Mission Planner / Ground Station
              |
            MAVLink
              |
        ArduPilot SITL  <---->  Gazebo Harmonic
              |
       Companion-computer interface
          (ROS 2 - planned)
              |
     +--------+---------+
     |                  |
  Perception          Mission logic
  Camera/LiDAR        State/recovery
     |                  |
     +------ Navigation+
              |
       Precision landing
```

Planned subsystems:

-   **Flight control:** ArduPilot, stabilization and mission execution.
-   **Perception:** camera, landing-target detection and LiDAR/range
    sensing.
-   **Navigation:** position estimation and obstacle-aware navigation.
-   **Precision recovery:** landing target alignment and controlled
    descent.
-   **Mission intelligence:** battery/state monitoring, recovery
    decisions and logging.

## 10. Development roadmap

-   [ ] Reconfirm stable Gazebo ↔ ArduPilot SITL connection.
-   [ ] Verify frame configuration and resolve any pre-arm warnings.
-   [ ] Demonstrate and record a safe simulated takeoff, waypoint
    mission and landing.
-   [ ] Verify camera sensor output in Gazebo.
-   [ ] Select and integrate a suitable rangefinder/LiDAR simulation.
-   [ ] Design and add the ROS 2 companion-computer interface (Ubuntu
    22.04-compatible distribution).
-   [ ] Implement and test obstacle detection/avoidance.
-   [ ] Implement landing-pad detection.
-   [ ] Implement and measure precision landing performance.
-   [ ] Add mission/recovery logic and structured logging.
-   [ ] Produce final demonstration video, architecture diagrams and
    test report.

## 11. Evidence and records

For each milestone, save:

-   Date and software versions.
-   Exact launch/configuration commands.
-   Screenshots or short screen recordings.
-   Relevant SITL/Gazebo logs.
-   Test conditions and observed results.
-   Known limitations and next actions.

Suggested locations:

``` text
/data/AURORA/logs/
/data/AURORA/simulation/
/data/AURORA/sensor_data/
/data/AURORA/documentation/
```

------------------------------------------------------------------------

**Documentation rule:** Update this README whenever a command, path,
parameter, software version or verified capability changes. Clearly
distinguish *planned*, *implemented* and *tested* features.
