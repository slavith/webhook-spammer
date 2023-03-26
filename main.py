import random
from discord_webhook import DiscordWebhook
import requests
import time

names = ['john b', 'lisa', 'creig', 'user', '404', 'anonymous']
randommsg = ['heyy you got fucked!', 'bro how can you get spammed like that :skull:', 'dang bruh my bad', 'RIP']


multi = input("Multi Webhooks ? (y/n) >>")

if multi == 'y':
    howmuch = input("how much webhook you want to use / max is 3 >>")
    if howmuch == '1':
        webhooksimple = input("webhook url >> ")
        rdmmsg = input("random msg ? (y/n) >>")
        times = input("how much time should i spam >>")
        if rdmmsg == 'y':
            for i in range(int(times)):
                start = DiscordWebhook(url=webhooksimple, content=random.choice(randommsg), username=random.choice(names))
                response = start.execute()
        elif rdmmsg == 'n':
            msgtosend = input("message >>")
            for i in range(int(times)):
                start = DiscordWebhook(url=webhooksimple, content=msgtosend, username=random.choice(names))
                response = start.execute()
    elif howmuch == '2':
        firstwebhook = input("webhook #1 >>")
        twondwebhook = input("webhook #2 >>")
        rdmmsg = input("random msg ? (y/n) >>")
        times = input("how much time should i spam >>")
        if rdmmsg == 'y':
            for i in range(int(times)):
                start = DiscordWebhook(url=firstwebhook, content=random.choice(randommsg), username=random.choice(names))
                response = start.execute()
                start2 = DiscordWebhook(url=twondwebhook, content=random.choice(randommsg), username=random.choice(names))
                response = start2.execute()
        elif rdmmsg == 'n':
            msgtosend = input("message #1 >>")
            msgtosend2 = input("message #2 >>")
            for i in range(int(times)):
                start = DiscordWebhook(url=firstwebhook, content=msgtosend, username=random.choice(names))
                response = start.execute()
                start2 = DiscordWebhook(url=twondwebhook, content=msgtosend2, username=random.choice(names))
                response = start2.execute()
    elif howmuch == '3':
        firstwebhook = input("webhook #1 >>")
        twondwebhook = input("webhook #2 >>")
        threewebhook = input("webhook #3 >>")
        rdmmsg = input("random msg ? (y/n) >>")
        times = input("how much time should i spam >>")
        if rdmmsg == 'y':
            for i in range(int(times)):
                start = DiscordWebhook(url=firstwebhook, content=random.choice(randommsg), username=random.choice(names))
                response = start.execute()
                start2 = DiscordWebhook(url=twondwebhook, content=random.choice(randommsg), username=random.choice(names))
                response = start2.execute()
                start3 = DiscordWebhook(url=twondwebhook, content=random.choice(randommsg), username=random.choice(names))
                response = start3.execute()
        elif rdmmsg == 'n':
            msgtosend = input("message #1 >>")
            msgtosend2 = input("message #2 >>")
            msgtosend3 = input("message #3 >>")
            for i in range(int(times)):
                start = DiscordWebhook(url=firstwebhook, content=msgtosend, username=random.choice(names))
                response = start.execute()
                start2 = DiscordWebhook(url=twondwebhook, content=msgtosend2, username=random.choice(names))
                response = start2.execute()
                start3 = DiscordWebhook(url=twondwebhook, content=msgtosend3, username=random.choice(names))
                response = start3.execute()
elif multi == 'n':
    webhooksimple = input("webhook url >> ")
    rdmmsg = input("random msg ? (y/n) >>")
    times = input("how much time to spam >>")
    if rdmmsg == 'y':
            for i in range(int(times)):
                start = DiscordWebhook(url=webhooksimple, content=random.choice(randommsg), username=random.choice(names))
                response = start.execute()
    elif rdmmsg == 'n':
        msgtosend = input("message >>")
        for i in range(int(times)):
            start = DiscordWebhook(url=webhooksimple, content=msgtosend, username=random.choice(names))
            response = start.execute()
