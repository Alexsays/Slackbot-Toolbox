#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import time
import re
import slack
import subprocess
import sys


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'external-ip' in data['text']:
        channel_id = data['channel']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text="🌍 " + subprocess.run(['curl', 'ifconfig.co'], capture_output=True).stdout.decode('utf-8')
        )
    elif 'local-ip' in data['text']:
        channel_id = data['channel']
        user = data['user']
        local_ip = '🏠 '

        if sys.platform == 'darwin':
            local_ip = local_ip + subprocess.run(
                'ipconfig getifaddr en0',
                shell=True,
                capture_output=True
            ).stdout.decode('utf-8')
        else:
            local_ip = local_ip + subprocess.run(
                'hostname -i',
                shell=True,
                capture_output=True
            ).stdout.decode('utf-8')

        web_client.chat_postMessage(
            channel=channel_id,
            text=local_ip
        )


if __name__ == '__main__':
    slack_token = os.environ['SLACK_API_TOKEN']
    rtm_client = slack.RTMClient(token=slack_token)
    rtm_client.start()
