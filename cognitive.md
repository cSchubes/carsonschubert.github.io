---
layout: page
title: Cognitive Communications
subtitle: Building the Cognitive Link at NASA's Glenn Research Center
---

# At a Glance
- 16 week research project conducted at NASA's [Glenn Research Center](https://www.nasa.gov/centers/glenn/home/index.html)
on the application of reinforcment learning to cognitive communications.

- Cognitive communications involve the use of ground software and software defined radios
to intelligently communicate in complex, dynamic environments.

- My work focused on the cognitive link: an intelligent point-to-point link that changes
link parameters based upon observed link characteristics to maintain the highest possible data rate.
    
- First author on a paper covering this reseach published at the [2019 IEEE Cognitive Communications for Aerospace Applications Workshop](http://ieee-ccaa.com/) in 
July 2019. Read it [here](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20190026713.pdf).
    
- **Personal Contributions**:  

    - Designed and implemented a new simulation environment for training and testing reinforcement learning agents for
    cognitive communcations. This environment was later used by other researchers beyond my project.
    - Built and trained an agent, modeled as a neural network, within this environment capable of acting as a cognitive link.
    - Tuned agent hyperparameters via grid search and performed k-fold cross validation to ensure agent would generalize.
    - Reported final results in a 16-page technical report that was later edited into the paper mentioned above.

![alt text](https://cschubes.github.io/img/Glenn-Last-Day.jpg "Last Day at Glenn Research Center")

# Details
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

The research resulted in a paper published at the [2019 IEEE Cognitive Communications for Aerospace Applications Workshop](http://ieee-ccaa.com/), on which I am first author.
You can read the paper [here](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20190026713.pdf).

A podcast from NASA covers the motivations behind this type of research in more detail and features my mentor from Glenn, Janette Briones! Find it [here](https://www.nasa.gov/mediacast/goddard/2018/the-invisible-network-podcast-episode-04-automation).