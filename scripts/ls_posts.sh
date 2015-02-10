#!/bin/sh

# list all the posts
mds=`ls -r docs/????-*md` 

for md in $mds
	   do echo $md;
done
	      # strip metadata
# cat content of posts into docs/post.md
