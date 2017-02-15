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

import sys

import bpy

#use only the given devices or all if none were given
for i in range(4):
    if str(i) in sys.argv:
        bpy.context.user_preferences.addons['cycles'].preferences.get_devices()[0][i].use = True
    else:
        bpy.context.user_preferences.addons['cycles'].preferences.get_devices()[0][i].use = False
        
renderFolder = "/foo/bar"
filePath = bpy.data.filepath
fileFolder = filePath.split("/")[-2]
fileName = filePath.split("/")[-1].split(".")[0]


'''OPTIONS'''
#file type
bpy.context.scene.render.image_settings.file_format = "PNG"
#set render path
bpy.context.scene.render.filepath = renderFolder+"/"+fileFolder+"/"+fileName
#if a frame already exists, don't re-render it
bpy.context.scene.render.use_overwrite = False
#if you started rendering a frame, make an empty file for it so that other notes know you're taking care of it
bpy.context.scene.render.use_placeholder = True
#keep render data around for faster re-render
bpy.context.scene.render.use_persistent_data = True

'''RENDER'''
#render and write ouput to render path automatically
bpy.ops.render.render(animation=True, write_still=True)
