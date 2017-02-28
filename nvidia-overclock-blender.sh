#!/bin/bash

#stable overclock for my system
coreClock=230
memoryClock=200

nvidia-settings \
  -a "[gpu:0]/GPUGraphicsClockOffset[3]=$coreClock" \
  -a "[gpu:0]/GPUMemoryTransferRateOffset[3]=$memoryClock" \
  -a "[gpu:1]/GPUGraphicsClockOffset[3]=$coreClock" \
  -a "[gpu:1]/GPUMemoryTransferRateOffset[3]=$memoryClock" \
  -a "[gpu:2]/GPUGraphicsClockOffset[3]=$coreClock" \
  -a "[gpu:2]/GPUMemoryTransferRateOffset[3]=$memoryClock" \
  -a "[gpu:3]/GPUGraphicsClockOffset[3]=$coreClock" \
  -a "[gpu:3]/GPUMemoryTransferRateOffset[3]=$memoryClock"
