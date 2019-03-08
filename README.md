# Deep Reinforcement Learning Project 2
## Continuous Control
Second Udacity Deep Reinforcement Learning Nanodegree Assignment

## Project details
* This project is the second mandatory project in Udacity Deep Reinforcement Learning Nanodegree.
* The goal of this project is to train a robot arm to reach target as long as possible. There are two versions of Unity environment provided.
  * The first version contains a single agent.
  * The second version contains 20 identical agents, each with its own copy of the environment.
* In this project I choose the second version of environment.
* The rewards are:
  * `+0.1` for each step the hand is in the goal location
  * `0` for else
* The observation space consist of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm.
* There are four action states, each of them corresponds to torque applicable to two joints.

## Task Requirements
* Codes must be written in Python 3 and PyTorch
* Agents are able to receive average reward of 30 or more (average of 20 agents)

## Getting started
1. Clone the DRLND Repository https://github.com/udacity/deep-reinforcement-learning/#dependencies
2. Download the Unity Environment
    * For this project, you will not need to install Unity - this is because Udacity have already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system
      * Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
      * Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
      * Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
      * Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)
3. Place the Unity Environment file from step 2 in the p2_continuous-control/ folder in the DRLND GitHub repository, and unzip (or decompress) the file. p2_continuous-control/ folder is from DRLND (step 1).

## Instruction
1. Open continuous_control.py to start training the agent.
2. Open play_the_agent.py to watch agent plays.












