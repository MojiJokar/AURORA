                  AURORA UAV SYSTEM
                         |
          +--------------+--------------+
          |                             |
     GROUND STATION               COMPANION COMPUTER
     Mission Planner                    ROS 2*
          |                             |
          | MAVLink                     |
          +--------------+--------------+
                         |
                   ARDUPILOT
                   Flight Control
                         |
                +--------+--------+
                |                 |
             Sensors          Actuators
                |                 |
          +-----+------+          |
          |            |          |
        Camera       LiDAR        |
          |            |          |
          +------+-----+          |
                 |                |
             PERCEPTION           |
                 |                |
          NAVIGATION &             |
          OBSTACLE AVOIDANCE       |
                 |                |
          PRECISION LANDING        |
                 |                |
          MISSION INTELLIGENCE     |
                 |                |
          FLIGHT LOGGING           |
                                  |
                           UAV SIMULATION
                         Gazebo + ArduPilot
