#!/bin/bash

source venv/bin/activate

CURRENT=`pwd`
BASENAME=`basename "$CURRENT"`

echo "$BASENAME"

instaloader --login=petrsmirnovblog profile $BASENAME
# instaloader profile $BASENAME


python3 make_index.py
