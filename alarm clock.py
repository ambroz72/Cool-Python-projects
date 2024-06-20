import datetime
from playsound import playsound

alh = int(input("Enter Hour: "))
alm = int(input("Enter minute: "))
al = input("am / pm: ")

if al == 'pm':
    alh += 12
elif al == 'am' and alh == 12:  # Midnight case
    alh = 0

while True:
    now = datetime.datetime.now()
    if alh == now.hour and alm == now.minute:
        print("Alarm is ringing...")
        playsound('zzz.mp3')
        break
