#!/bin/bash

nvidia-settings \
  -a "[gpu:0]/GPUFanControlState=0" \
  -a "[gpu:1]/GPUFanControlState=0" \
  -a "[gpu:2]/GPUFanControlState=0" \
  -a "[gpu:3]/GPUFanControlState=0"
