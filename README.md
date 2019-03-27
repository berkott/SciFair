# SciFair
Early Detection of Sleep Apnea through Simplified Tests and Artificial Intelligence


## Push ionic code
git push ionic master

cut -d, -f1-5,89-100 Muse-2051_2019-03-23--12-58-33_1553360381740.csv > outputF.csv
grep -F '.0' outputPPG.csv > outputFiltered2.csv
cat head.txt outputFiltered2.csv > finalFilteredPPG.csv

The Respiration Rate can be obained from the low DC signal that offsets the PPG data. For obtaining the frequency of this low DC signal, I initiated a band pass filter with specifications that allow us to obtain the low frequency signals that correspond to the respiration rate(12-16 breaths per minute). I used a band pass filter to remove the high frequency signals from the PPG data and plotted the original and filtered data. I used a periodogram to obtain the maximum PSD value. I calculated the frequency associated with the maximum PSD value and used it to calculate the Respiration Rate.