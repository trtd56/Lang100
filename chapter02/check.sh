#echo "Q10"
#cat hightemp.txt | wc -l

#echo "\nQ11"
#cat hightemp.txt | sed -e "s/\t/ /g"

#echo "\nQ12"
#echo "\ncol1"
#cat hightemp.txt | cut -f 1
#echo "\ncol2"
#cat hightemp.txt | cut -f 2

#echo "\nQ13"
#paste col1.txt col2.txt

#echo "\nQ14"
#head -3 hightemp.txt

#echo "\nQ15"
#tail -3 hightemp.txt

#echo "\nQ16"
#split -l 3 hightemp.txt div_ 

#echo "\nQ17"
#cut -f1 hightemp.txt | sort | uniq

#echo "\nQ18"
#sort -k3 hightemp.txt

echo "\nQ19"
cut -f1 hightemp.txt | sort | uniq -c | sort -k1 -r
