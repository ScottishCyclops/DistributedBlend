# DistributedBlend
DistributedBlend is a association of scripts designed to render multiple Blender files on multiple GPUs with the click of a button.
Blender is a open source 3D creation package. I created this project because I needed a fast and easy way to render a lot of scenes for a personal animation project.
More info : https://blender.org

## How it works
It uses a file name *jobs*, by default in the same folder as the scripts, wich contains the blender files that need to be rendered.
The file *add_job.py* is used to add jobs to that list quickly.
You can make it even quicker by adding the script to your contextual menu. You just have to pass %f as a parameter to the script.
See http://askubuntu.com/questions/21953/how-do-i-customize-the-context-menu-in-nautilus for help.

Jobs can be removed the same way with the *remove_job.py* script.

Once the *jobs* file is filled, you start the farm with *farm.sh*. That script will lauch the *farm.py* file 4 times.
Why 4 ? Because I have 4 GPUs.
The *farm.py* script takes an argument letting him know wich GPU(s) to use for rendering (0, 1, 2 or 3) in the order they are in the NVIDIA X Server Settings.
The script seeks available jobs in the *jobs* file and selects the first one.
It then opens a blender subprocess with the *autorender.py* script for configuration and the job as the file.
Any errors generated from the subprocess will be written to the *log* file, locatted, agin, in the script folder
(many other things are logged : added jobs, removed jobs, farms started, farms stopped, renders started, renders finished).

The *autorender.py* script is responsable for the Blender configuration and rendering. It takes a GPU id as a parameter, this time in blender oder (wich for some reasons is different from the system's order).
It sets different parametters for rendering and lauches the render, the most important ones being :
```python
bpy.context.scene.render.use_overwrite = False
bpy.context.scene.render.use_placeholder = True
```
The first on assures that the files alrdeady rendered are not going to be rendered again by another GPU.
The second tells blender to make a placeholder once it decided to render a frame.
More information on the why : https://youtu.be/y3EcpkwLCFI

Once a GPU has finished a job, or the remaining frames are already taken by others GPU, it removes the job from the jobs file.
It then proceeds to the next job. If they are none, it stops.

The *utils.py* file simply contains functions and methods used by all the mentioned scripts.

## Conclusion
I hope this code can be helpfull for some people. Of course, it is very centralised on my own needs and not usable out of the box in your projects, but changing some file paths and parameters are enough to get it to work.

I know a lot in Python, but I'm still quite new to the real programming world. In fact, this is my first repository ! Hey !

Please reports any typos in this file. My primary language isn't English and, despite my best efforts, there must be a lot of little errors.

I will be doing a video tutorial on how to set it up and use it, so if you're interrested, keep an eye on this : https://www.youtube.com/c/ScottishCyclops

-Scott
