#!/bin/bash
while [ ! -f ~/Downloads/Muse* ]
do
  sleep 2
done
mv ~/Downloads/Muse* ../assets/new/
unzip ../assets/new/*.zip -d ../assets/new
rm ../assets/new/*.zip

cut -d, -f3-4 ../assets/new/Muse* > ../assets/new/EEG.csv
cut -d, -f89-100 ../assets/new/Muse* > ../assets/new/PPG.csv

grep [0-9] ../assets/new/*EEG.csv > "$(date +"%Y_%m_%d_%I_%M_%p")EEG.csv"
grep [0-9] ../assets/new/*PPG.csv > "$(date +"%Y_%m_%d_%I_%M_%p")PPG.csv"

# cat ../assets/headEEG.txt EEGF.csv > "$(date +"%Y_%m_%d_%I_%M_%p")EEG.csv"
# cat ../assets/headPPG.txt PPGF.csv > "$(date +"%Y_%m_%d_%I_%M_%p")PPG.csv"

rm EEG.csv EEGF.csv PPG.csv PPGF.csv