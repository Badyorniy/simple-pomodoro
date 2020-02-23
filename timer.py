from playsound import playsound
from time import sleep

def pomodoro(msg, filename, min_to_sleep):
    print(msg)
    playsound(filename + '.mp3')
    sleep(min_to_sleep * 60)
    
while 1:
    pomodoro('Work time!', 'end', 25)
    pomodoro('Rest time!', 'start', 5)


