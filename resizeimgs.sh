#!/bin/sh
for img in docs/imgs/*;
do mogrify -quality 80% -strip -resize 700x\> $img;
done;

# 2nd round: compress pngs
for img in docs/imgs/*.png;
do optipng -o5 $img
done;   
# -strip Strip any comment or exif tag
#
#
# -resize 700x\>  resize only if img is larger than 700px
