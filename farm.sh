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
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

resize -s 30 210 > /dev/null

OCPATH="."

$OCPATH/nvidia-fanspeed-high.sh > /dev/null
$OCPATH/nvidia-overclock-blender.sh > /dev/null

if (($# > 0))
then
    #if we got any arguments
    if [ $1 == "-m" ]
    then
        #if we wish to lauch multiple terminals (less responsive, but more readable)
        gnome-terminal -x sh -c "./farm.py 0; bash"
        sleep .5
        gnome-terminal -x sh -c "./farm.py 1; bash"
        sleep .5
        gnome-terminal -x sh -c "./farm.py 2; bash"
        sleep .5
        gnome-terminal -x sh -c "./farm.py 3; bash"

    elif [ $1 == '-l' ]
    then
        #low impact : we don't use the first GPU
        ./farm.py 1 & sleep .5 & ./farm.py 2 & sleep .5 & ./farm.py 3 & wait
    else
        echo "unknown argument. -m for multiple terminals, -l for low impact"
    fi
else
    #otherwise, we lauch all the processes in the same terminal
    #and wait for them to finish
    ./farm.py 0 & sleep .5 & ./farm.py 1 & sleep .5 & ./farm.py 2 & sleep .5 & ./farm.py 3 & wait
fi

$OCPATH/nvidia-fanspeed-auto.sh > /dev/null
$OCPATH/nvidia-overclock-default.sh > /dev/null
