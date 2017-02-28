#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
    DistributedBlend is a software designed to render multiple blender
    files on multiple GPUs with the click of a button
    Copyright (C) 2017 Scott Winkelmann

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import subprocess
import sys

from utils import *
from datetime import datetime

startTime = str(datetime.now()).split(":")[0].replace(" ", "_")
Log("FARM STARTED")

blenderPath  = "/path/to/blender" #path to the executable
renderScript = "./autorender.py"
jobsFile     = "./jobs"
logFile      = "./log"
gpus         = ""

#if no arguments are given, we assigne all the GPUs
if len(sys.argv) == 1:
    gpus = "0 1 2 3"
else:
    for arg in sys.argv:
        if len(arg) == 1:
            #converting gpu system id to blender id
            gpus+=str({
                0 : 2,
                1 : 3,
                2 : 0,
                3 : 1,
            }.get(int(arg)))

print("found",len(GetJobs()),"jobs")

#while there are jobs in the file, we get a new job
while len(GetJobs()) > 0:
    #getting next job
    job = GetJobs()[0]
    Log("RENDER BEGIN",job)
    print("Render started for ",job)

    #command to render a blender file
    #TODO: better output formatting 
    cmd = blenderPath+" -b "+job+" -P "+renderScript+" -t "+startTime+" "+gpus+" | grep 'Path Tracing Tile\|skipping existing frame'"
    try:
        #running the command and checking for errors in the subprocess
        subprocess.run(cmd, shell=True, check=True,stderr=subprocess.PIPE,universal_newlines=True)
    except subprocess.CalledProcessError as e:
        print("Job failed. Jumping to next job. See log file for details")
        Log("ERROR",str(e.stderr))
    else:
        Log("RENDER END",job)
        print("Render finished for",job)
    finally:
        #if a gpu has finished the job, it removes it from the list
        #every gpu runs this function once it's finished it's last attributable frame
        #but that doesn't matter, since the RemoveJob function handles it
        RemoveJob(job)
        
#the jobs file is empty
print("No more files to render")
Log("FARM STOPPED")
