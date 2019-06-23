import time
import tkinter as tk

win = tk.Tk()
win.title('stopwatch')
win.geometry('800x300')

starttime = 0
stoptime = 0
splittime = []
splitrecord = []
scounter = 0
laptime = []
laprecord = []
lcounter = 0
switch = 0

def start_stop():
    x = time.time()
    global starttime, stoptime, laptime, laprecord, lcounter, switch
    if switch == 0:
        if starttime == 0:
            starttime = x
            y = round(starttime, 3)
            laptime.append(float(y))
            labelResult['text'] = str('running...')
            switch += 1
        else:
            starttime += x - stoptime
            y = round(starttime, 3)
            laptime = []
            laprecord = []
            lcounter = 0
            laptime.append(float(y))
            labelResult['text'] = str('running...')
            switch += 1
    else:
        stoptime = x
        labelResult['text'] = float(round(stoptime-starttime, 5))
        switch -= 1

def split():
    x = time.time()
    global starttime, splittime, splitrecord, scounter, switch
    if switch == 1:
        splittime.append(x)
        y = float(round(splittime[scounter]-starttime, 3))
        splitrecord.append(y)
        labelSplit['text'] = str('split: {}'.format(splitrecord))
        scounter += 1

def lap():
    x = time.time()
    global laptime, laprecord, lcounter, switch
    if switch == 1:
        laptime.append(x)
        y = float(round(laptime[lcounter+1]-laptime[lcounter], 3))
        laprecord.append(y)
        labelLap['text'] = str('lap: {}'.format(laprecord))
        lcounter += 1

def reset():
    global switch, starttime, stoptime, splittime, splitrecord,\
        scounter, laptime, laprecord, lcounter
    if switch == 0:
        starttime = 0
        stoptime = 0
        splittime = []
        splitrecord = []
        scounter = 0
        laptime = []
        laprecord = []
        lcounter = 0
        labelResult['text'] = str('standby')
        labelSplit['text'] = str('split:')
        labelLap['text'] = str('lap:')

labelResult = tk.Label(win, text='standby')
startstopButton = tk.Button(win, text='start/stop', command=start_stop)
splitButton = tk.Button(win, text='split', command=split)
lapButton = tk.Button(win, text='lap', command=lap)
labelSplit = tk.Label(win, text='split:')
labelLap = tk.Label(win, text='lap:')
resetButton = tk.Button(win, text='reset', command=reset)

labelResult.pack()
startstopButton.pack()
splitButton.pack()
lapButton.pack()
labelSplit.pack()
labelLap.pack()
resetButton.pack()

win.mainloop()
