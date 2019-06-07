---
layout: page
title: On-Orbit Pose Estimation
meta-title: Carson Schubert - On-Orbit Pose Estimation
subtitle: Relative Pose Estimation of Non-Cooperative Spacecraft via Monocular Camera Imagery
---

# At a Glance
- [Texas Spacecraft Laboratory](https://sites.utexas.edu/tsl/#) collaboration with NASA Johnson Space Center (JSC)
for follow on research to [Seeker Vision](https://cschubes.github.io/seeker).  

- Seeker Vision was only capable of computing relative azimuth and elevation of a target spacecraft,
not full 6 degree of freedom relative pose.

- Full relative pose will enable more complex autonomous proximity operations from free-flying spacecraft.

- Critically, the system must still be able to run onboard CubeSat-level hardware and is thus highly constrained
computationally.

- **Personal Contributions to Date**:  

    - Aided in the design of an end-to-end model training pipeline supported by AWS to enable rapid, iterative
    model development in the cloud.
    - Designed and am actively developing [ravenML](https://github.com/autognc/ravenML), an open-source, plugin based 
    Python CLI for training machine learning models quickly and easily. ravenML is one component of the previously
    mentioned model training pipeline.