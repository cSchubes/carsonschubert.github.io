---
layout: page
title: Seeker Vision
meta-title: Carson Schubert - Seeker Vision
subtitle: Vision System for NASA JSC's Seeker CubeSat Mission
---
![alt text](https://cschubes.github.io/img/cygnus.jpg "Cygnus Resupply Spacecraft")

The [Texas Spacecraft Laboratory](https://sites.utexas.edu/tsl/#) (TSL) is a student-driven research group dedicated to designing and building small satellites, 
securing launches into space, and operating them once in orbit. I joined the lab as a sophomore undergrad and was privileged to see a project through from start to 
final delivery as a team lead during my sophomore year. I worked as the Flight Software and Hardware lead on the Seeker Vision project. Seeker Vision was a collaboration between 
NASA Johnson Space Center and UT Austin as part of the Seeker 1 CubeSat mission. The mission serves as a first technical demonstration of small, free flying, autonomous 
spacecraft which will one day be used to inspect stations and spacecraft for damage during flight. UT Austin was contracted to build a full vision system for the CubeSat, 
including flight software, novel vision algorithms, and robust error handling. The system was to use only a camera and microcomputing board - access to other sensors
onboard the satellite was restricted. Using Tensorflow, our team built a convolutional neural network to detect the 
target spacecraft, a Northrop Grumman Cygnus resupply ship (pictured above), within the camera's frame of view. Once the target was identified, OpenCV was used to determine relative azimuth and elevation of 
the target spacecraft. This information was then passed to the main flight computer and used as part of the Guidance, Naviation, and Control for the CubeSat.
As the Flight Software and Hardware lead, I was present at all three mission reviews and presented slides about the state of the various 
areas of the project I was working on. My responsibilities were threefold:

- Design, implement, and test flight software to handle boot sequence, facilitate vision algorithms, and communicate with main flight computer
- Develop a suite of logging and data visualization scripts to characterize algorithm performance onboard flight hardware
- Create technical documents detailing setup of mission hardware/testing procedures to simplify integration for flight

My team and I successfully built flight software using two-tier process monitoring to prevent crashes on orbit. The entire vision system was installable
with a single terminal command and ran automatically on boot if a camera was connected. After rigorous testing, the system was delivered to JSC in May of 2018 
with technical documents which detailed its use and integration.   

The delivered vision system was recently selected over multiple other vision systems for integration on the Seeker 1 CubeSat mission to launch in April 2019. Its
ability to successfully handle worst case scenarios in testing was cited as a primary reason for its selection.
