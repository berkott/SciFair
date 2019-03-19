#!/bin/bash
while [ ! -f ~/Downloads/Muse* ]
do
  sleep 2
done
mv ~/Downloads/Muse* ~/Code/SciFair/src/assets/new/
unzip assets/new/*.zip -d assets/new
rm assets/new/*.zip