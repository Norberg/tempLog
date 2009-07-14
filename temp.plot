#!/usr/bin/env gnuplot
set title "Temperature"
set xlabel "Datetime"
set ylabel "Celcius"

set terminal png
set output "temp.png"
set datafile separator "|"
set style data lines
set grid
set yrange [0:*]
set xdata time
set timefmt x "%H:%M"
set format x "%H:%M"
plot "< sqlite3 temp.db \"SELECT time, degree from temp where date = date('now') and sensor = 'test';\"" using 1:2 title "test", "< sqlite3 temp.db \"SELECT time, degree from temp where date = date('now') and sensor = 'outside';\"" using 1:2 title "outside"
