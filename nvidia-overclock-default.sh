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

#last 3 GPus get underclocked, the first one is simply reset
#because it is beeing used for display
coreClock=-90
memoryClock=-402

nvidia-settings \
  -a "[gpu:0]/GPUGraphicsClockOffset[3]=0" \
  -a "[gpu:0]/GPUMemoryTransferRateOffset[3]=0" \
  -a "[gpu:1]/GPUGraphicsClockOffset[3]=$coreClock" \
  -a "[gpu:1]/GPUMemoryTransferRateOffset[3]=$memoryClock" \
  -a "[gpu:2]/GPUGraphicsClockOffset[3]=$coreClock" \
  -a "[gpu:2]/GPUMemoryTransferRateOffset[3]=$memoryClock" \
  -a "[gpu:3]/GPUGraphicsClockOffset[3]=$coreClock" \
  -a "[gpu:3]/GPUMemoryTransferRateOffset[3]=$memoryClock"
