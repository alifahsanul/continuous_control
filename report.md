# Report of Assignment
This report explains the method used to solve the Continuous Control Project and the result.

## Learning Algorithm
* To solve this reinforcement learning problem, [Deep Q-Learning](https://towardsdatascience.com/self-learning-ai-agents-part-ii-deep-q-learning-b5ac60c3f47) is used with the architectures depicted in the following images. All hidden layers use relu activation function.
<img src="https://raw.githubusercontent.com/alifahsanul/banana_navigation/master/image/nn.jpg" alt="drawing" width="500"/>

* For tutorial on how to use PyTorch to build Deep Q Network, visit this [page](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html).
* Hyperparameters used:
  * Discount factor &gamma; = 0.99
  * Learning Rate &alpha; = 5 &times; 10<sup>-4</sup>

## Plof of Rewards
The agent was trained for 704 episodes before reaching 13 average score for 100 consecutive episodes.
![alt text](https://raw.githubusercontent.com/alifahsanul/banana_navigation/master/image/Score.jpg)

Trained agent at play:
![alt text](https://github.com/alifahsanul/banana_navigation/blob/master/image/agent_simulate.gif?raw=true)

## Ideas for future work
  * Double Deep Q-Learning
  * Different activation function (leaky relu, sigmoid, etc.)
  * Learning from pixels instead of direct information from environment
  * Various number of hidden layers and its nodes
