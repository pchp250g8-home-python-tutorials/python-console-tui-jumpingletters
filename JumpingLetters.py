# --coding:utf-8--

import curses
import time

strLine = "Hello World!!! Jumping Letters!!! Press Any Key To Exit!!!"
scr = curses.initscr()
curses.curs_set(0)
scr.clear()
nLen = len(strLine)
for i in range(0, nLen):
    for j in range(80, 10 + i, -1):
        scr.addstr(10, 10 + j, strLine[i] + " ")
        scr.refresh() 
        time.sleep(.005) 
scr.getch()
curses.endwin()
