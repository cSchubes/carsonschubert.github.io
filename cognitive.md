---
layout: page
title: Cognitive Communications
subtitle: Building the Cognitive Link at NASA's Glenn Research Center
---
![alt text](https://cschubes.github.io/img/Glenn_Last_day-flip.jpg "Last Day at Glenn Research Center")

I was lucky enough to spend the fall semester of 2018 as a Machine Learning Intern at NASA's Glenn Research Center. It was a dream come true - the culmination of years
of preparation spent hoping for a chance in the space industry. My research was part of the Cognitive Communications project at Glenn Research Center, a next generation communications
project seeking to update NASA's communications infrastrucutre for the 21st century. As the number of assets in space increases, 
it is crucial that communications transition from the highly manual task they are today to an automated solution. With ever rising numbers of CubeSat and micro-satellite
 payloads being launched into orbit, this is a pressing issue. My work was focused on the cognitive link, 
a point to point link which aims to maximize data throughput by responding to variations in signal quality intelligently. There were three main goals:

- Build a simulation environment for testing and training reinforcement learning agents that implement the cognitive link.
- Build and train my own agent to inside this environment.
- Verify agent performance via statistical methods and visualize the learning process.

The reinforcement learning agent must switch between available radio links intelligently to achieve the maximum possible data rate. The simulation environment
was developed using pre-existing MATLAB code that could simulate orbital dynamics and radio communcations. This code was used to generate training data,
which was then fed into a custom [Gym](https://gym.openai.com/) environment. After developing the simulation environment, I began building and training agents within it. 
The agents were modelled as neural networks using [PyTorch](https://pytorch.org/). Each agent was given slightly different hypergitparameters and run through a test plan that characterized each 
agent's performance to compare them against one another. 
This involved extensive cross validation and statistical methods such as the F beta score. After completing this analysis, the 
best agent was selected and trained on all available episode data in the environment to produce a final agent capable of acting as a cognitive link.  

A research paper and visualization are pending release from NASA.

A podcast from NASA covers the motivations behind this type of research in more detail and features my mentor from Glenn, Janette Briones! Find it [here](https://www.nasa.gov/mediacast/goddard/2018/the-invisible-network-podcast-episode-04-automation).