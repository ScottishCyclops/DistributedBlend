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
from datetime import datetime

def GetJobs(jobsFile = "./jobs"):
    """returns each line of the job file in a list"""
    with open(jobsFile, "r") as f:
        content = f.read().splitlines()
    f.close()
    return content

def RemoveJob(excludedJob,jobsFile = "./jobs"):
    """rewrites the job file excluding the given job.
    does not verify job validity"""
    _jobs = GetJobs()
    with open(jobsFile, "w") as f:
        for job in _jobs:
            if job != excludedJob:
                f.write(job+"\n")
    f.close()

def AddJob(newJob,jobsFile = "./jobs"):
    """adds a job to the jobs file.
       does not verify job validity"""
    with open(jobsFile, "a") as f:
        f.write(newJob+"\n")
    f.close()

def Log(message,value = "", logFile = "./log"):
    """write the given message to the log file with an optional value"""
    if not value.endswith("\n"):
        value+="\n"
    with open(logFile, "a") as f:
        f.write(str(datetime.now())+" | "+message.ljust(20)+" | "+value)
    f.close()

def CorrectPath(path):
    """removes the unwanted characters from a path"""
    if path.startswith("'") or path.startswith('"'):
        if path.endswith("'") or path.endswith('"'):
            return path[1:-1]
        if path.endswith("' ") or path.endswith('" '):
            return path[1:-2]
    return path
