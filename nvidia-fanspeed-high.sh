#!/bin/bash

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
