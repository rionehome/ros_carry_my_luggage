## Carry My Luggage

### turtlebot_bringup

### ydlidar

### follow_me
- https://github.com/rionehome/follow_me/tree/ros2/master

- follow_me.cpp
  - Subscriber
    - sensor_msgs/LaserScan, 'scan'
    - nav_msgs/Odometry, 'signal'
    - rione_msgs/Command, '/turtlebot2/odometry'
  - Publisher
    - geometry_msgs/Twist, '/turtlebot2/commands/velocity'

### sound_system
- turtlebot_button0.py
  - Subscriber
    - std_msgs/Bool, 'turtlebot2/button0'
  - Publisher
    - rione_msgs/Command, 'sound/speak1'

- sound_speak1.py
  - Subscriber
    - rione_msgs/Command, 'sound/speak1'
  - Publisher
    - rione_msgs/Command, '/signal'
    - rione_msgs/Command, 'sound/stop'

- sound_stop.py
  - Subscriber
    - rione_msgs/Command, 'sound/stop'
  - Publisher
    - rione_msgs/Command, '/signal'