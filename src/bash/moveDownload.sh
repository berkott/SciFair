#!/bin/bash
while [ ! -f ~/Downloads/Muse* ]
do
  sleep 2
done
mv ~/Downloads/Muse* ~/Code/SciFair/src/assets/new/
unzip ~/Code/SciFair/src/assets/new/*.zip -d ~/Code/SciFair/src/assets/new
rm ~/Code/SciFair/src/assets/new/*.zip

cut -d, -f3-4 ~/Code/SciFair/src/assets/new/Muse* > ~/Code/SciFair/src/assets/new/EEG.csv
cut -d, -f90-100 ~/Code/SciFair/src/assets/new/Muse* > ~/Code/SciFair/src/assets/new/PPG.csv

grep [0-9] ~/Code/SciFair/src/assets/new/EEG.csv | grep -v [a-zA-Z] > ~/Code/SciFair/src/assets/new/EEGF.csv
grep [0-9] ~/Code/SciFair/src/assets/new/PPG.csv | grep -v [a-zA-Z] > ~/Code/SciFair/src/assets/new/PPGF.csv

cat ~/Code/SciFair/src/assets/headEEG.txt ~/Code/SciFair/src/assets/new/EEGF.csv > ~/Code/SciFair/src/assets/new/FEEG.csv
cat ~/Code/SciFair/src/assets/headPPG.txt ~/Code/SciFair/src/assets/new/PPGF.csv > ~/Code/SciFair/src/assets/new/FPPG.csv

# rm EEG.csv EEGF.csv PPG.csv PPGF.csv