#!/bin/sh
for img in imgs/*;
do mogrify -resize 700x\> $img;
done;

