# --encoding:utf-8--
import curses
import time

strLine = "Hello,World!!! Python Conio Example!!!"
scr = curses.initscr()
curses.curs_set(0)
scr.clear()
nLen = len(strLine)
for i in range(0,nLen - 1):
    for j in range(70, 10 + i, -1):
        scr.addstr(10, 10 + j, strLine[i] + " ")
        scr.refresh() 
        time.sleep(.005) 
scr.addstr(10, 10, strLine)
scr.addstr(11, 10, "Press any key") 
scr.getch()
curses.endwin()