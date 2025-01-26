#!/bin/bash

LAYOUT=$(setxkbmap -query | grep layout)
if [[ $LAYOUT == *"us"* ]]; then
  setxkbmap ru
else
  setxkbmap us
fi