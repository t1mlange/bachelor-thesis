#!/bin/bash

for path in /home/tim/Projects/bachelor-thesis/chapters/*.tex; do
    file=$(basename $path)
    name=${file%.tex}
    newpath="/home/tim/Projects/bachelor-thesis/text/${name}.txt"
    detex $path > $newpath
done