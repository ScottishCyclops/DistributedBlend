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

import os
import sys

from utils import *

jobsFile = "./jobs"

#We either give the file as an argument, or enter it
if len(sys.argv) < 2:
    job = input("New render job: ")
else:
    job = sys.argv[1]

#correction drag'n'drop path problems
job = CorrectPath(job)

#not a valid path
if not os.path.isfile(job):
    print("File does not exists")
    sys.exit(1)

#not a blender file
if not job.endswith(".blend"):
    print("Not a .blend file")
    sys.exit(1)

#already in the jobs
if job in GetJobs():
    print("A job already exists for this file")
    sys.exit(1)

#all gud. we add the job
AddJob(job)

print("Added render job for",job.split("/")[-1])
Log("ADDED JOB",job)
