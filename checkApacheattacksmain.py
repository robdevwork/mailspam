 for i in $(find . -type f -mmin 0.5);do cat $i | awk '{print $1,$7,$12,$13,$14,$15,$18,$19,$20,$21}' | sort | uniq -c;done | awk '$1 >= 500'
