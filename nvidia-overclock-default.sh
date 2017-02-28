#!/bin/bash

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
