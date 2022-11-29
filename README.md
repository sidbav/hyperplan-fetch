# Hyperplan-Fetch

This repo contains the configuration files corresponding to the hyperplan repo

`results` directory stores the results of running the hyperplanning optimization and then testing of the said configurations

The Only configuration files we will be running are:
- box_pick-*.yaml
- tall_pick-*.yaml
- tall_place-*.yaml
- thin_vert_place-*.yaml

We will only be running configuration files with the loss functions of:
- execution time
- path length
- memory_loss (when that is implemented)

NOTE: We have updated the accross_groups to only run on the small_pick configuration files

# Original Readme from paper authors
See the corresponding images of each dataset for a visualization of start and goal.


pathxxxx.yaml is a valid trajectory
requestxxxx.yaml contains the start and goal configurations in joint_space
scenexxxx.yaml contains the geometric description of the obstacles
scene_sensedxxxx.yaml contains the octomap representation of the obstacles

The box_pick and table_under_pick contain problems that are in "open space" so I would assume similar
parameters work best for them

The tall_pick, small_pick, thin_vert_pick are bookcases that are narrow

tall_place and thin_vert_place are similar to the "pick" versions but instead of the stow position the robot
starts inside a random shelf

The thin_vert_place is the hardest one of all so far "especially the octomap version"
