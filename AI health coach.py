import datetime
import os
import time

# the format: "MonthDay Name Surname" (Without Quotes)
exercise_file = 'exercise.txt'
def happiness_creativity():
    now = datetime.datetime.now()
    alarm_time = datetime.datetime.combine(now.date(), datetime.time(18, 0, 0))
    time.sleep((alarm_time - now).total_seconds())

    os.system("alarm.mp3")


def exercise_routine():
    fileName = open(exercise_file, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag = 1
            os.system('notify-send "exercise scheduled: ' + line[1]
                      + ' ' + line[2] + '"')
    if flag == 0:
        os.system('notify-send "No exercise today"')

if __name__ == '__main__':
    happiness_creativity()
    exercise_routine()