import time

def countdown(t):
    while t>0:
        t-=1
        time.sleep(1)
        print(t)
    print('Time is up!')
seconds = input('Enter the duration of countdown: \n')

while not seconds.isdigit():
    print('Error !! Enter an integer value only')
    seconds = input('Enter the duration of a countdown: \n')
seconds = int(seconds)
countdown(10)
