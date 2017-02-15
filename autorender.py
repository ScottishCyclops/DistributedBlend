import bpy
import sys

#use only the given devices or all if none were given
for i in range(4):
    if str(i) in sys.argv:
        bpy.context.user_preferences.addons['cycles'].preferences.get_devices()[0][i].use = True
    else:
        bpy.context.user_preferences.addons['cycles'].preferences.get_devices()[0][i].use = False
        
renderFolder = "/home/scott/Documents/Concours/Bugnplay2017/6_renders"
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