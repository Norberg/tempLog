#!/usr/bin/env gnuplot
set title "Temperature"
set xlabel "Datetime"
set ylabel "Celcius"

set terminal png
set output "temp.png"
set datafile separator "|"
set style data linespoint
set xdata time
set timefmt "%y-%m-%d %H:%M"
set xrange ["2008-07-12 00:00":"2009-07-13 00:00"]
set format x "%y-%m-%d %H:%M"
#set timefmt "%y-%m-%d"
plot "< sqlite3 temp.db 'select date, temp from temp'" using 1:2 title "test"
