#!/bin/bash
# -*- coding: UTF-8 -*-

#   DistributedBlend is a software designed to render multiple blender
#   files on multiple GPUs with the click of a button
#   Copyright (C) 2017 Scott Winkelmann

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
# 

speed=80

nvidia-settings \
  -a "[gpu:0]/GPUFanControlState=1" \
  -a "[fan:0]/GPUTargetFanSpeed=$speed" \
  -a "[gpu:1]/GPUFanControlState=1" \
  -a "[fan:1]/GPUTargetFanSpeed=$speed" \
  -a "[gpu:2]/GPUFanControlState=1" \
  -a "[fan:2]/GPUTargetFanSpeed=$speed" \
  -a "[gpu:3]/GPUFanControlState=1" \
  -a "[fan:3]/GPUTargetFanSpeed=$speed"
