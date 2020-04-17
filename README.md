# Chasi - an ARTI product

Software for launching the driver and simulation for the Chasi.


## License

For all files in this repository: Copyright 2018-2020 by ARTI - Autonomous Robot Technology GmbH. All rights reserved.


## Contents

This repository contains several ROS packages:
- `arti_chasi_gazebo`: gazebo simluation of the robot incuding different sensor configurations.
- `arti_chasi_mark2`: provides the URDF of the robot as well as launch files to spawn the URDF and the driver of the robot.
- `arti_convert_ackermann`: converts command velocity in an ackerman message. 
  !! Important this does not calculate ackermann messages instead it is a conversion of message. 
  Mapping is as follows: Liner -> Linear, Rotation -> Steering angular.


## Use

The launch files for simlation are in the `arti_chasi_gazebo` ROS package. To start the simulation with the sick LMS1000 on the robot run:

```sh
roslaunch arti_chasi_gazebo gazebo_with_sick.launch
```

The launch files for the robot base are in the `arti_chasi_mark2` ROS package. To start the robot base run:

```sh
roslaunch arti_chasi_mark2 arti_chasi_mark2_base.launch
```

## Prerequisites

- [Ubuntu Xenial](http://releases.ubuntu.com/16.04/)
- [ROS Kinetic](http://wiki.ros.org/kinetic)
- [Gazebo 7.15+](https://answers.ros.org/question/259989/ubuntu-1604-xenial-package-for-gazebo-740/)

## Installation

- Install Ubuntu, ROS, and Gazebo.
- Create a [catkin](http://wiki.ros.org/catkin) workspace (see
  [Creating a workspace for catkin](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)).
- Clone this repository into the workspace's `src` directory.
- Clone other, required repositories into the `src` directory:
    - [gazebo_utils](https://github.com/ARTI-Robots/gazebo_utils.git)
    - [base_control](https://github.com/ARTI-Robots/base_control.git)
    - [base_control_vesc](https://github.com/ARTI-Robots/base_control_vesc.git)
    - [vesc](https://github.com/ARTI-Robots/vesc.git)
- Execute `rosdep install -i --from-paths src` from the workspace to install ROS dependencies.
- Execute `catkin_make` from the workspace to build all packages in the workspace.

### Additional information

To clone all the required repositories and keep them up to date, we recommend using wstool:

```sh
sudo apt-get install python-wstool
cd catkin_ws/src
wstool init  # creates .rosinstall file
wstool scrape  # searches for untracked VCS directories
wstool up  # updates (pulls) all repositories
```

To avoid having to enter git credentials multiple times, it is useful to enable credential caching:

```sh
git config --global credential.helper cache
```
