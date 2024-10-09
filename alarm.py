import pygame
import datetime
from pygame.locals import *
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time

devices = AudioUtilities.GetSpeakers()

interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

alarm_audio = "alarm.mp3"

hour = int(input("Hour: "))
minute = int(input("Minute: "))
second = int(input("Second: "))
meridiem = int(input("AM/PM: "))

hour += meridiem * 12

alarm_time = (datetime.datetime.now().replace(
hour=hour, 
minute=minute, 
second=second,
) - datetime.datetime.now()).seconds

def alarm():

    print(alarm_time/60/60, " hours")

    time.sleep(alarm_time)

    pygame.mixer.init()
    pygame.mixer.music.load(alarm_audio)

    print('Playing Sound')

    volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(-5, None)

    pygame.mixer.music.play()

    time.sleep(120)

#15 minute alarm interval

for i in range(0, 10):
    alarm()
    alarm_time = 15 * 60