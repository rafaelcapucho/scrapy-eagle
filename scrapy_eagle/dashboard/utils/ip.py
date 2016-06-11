# -*- coding:utf-8 -*-

import os
import re
import requests
import random

def get_hostname():

    return os.uname()[1]

def get_external_ip():

    source_list = [
        'http://ip.dnsexit.com',
        'http://ifconfig.me/ip',
        'http://ipecho.net/plain',
        'http://ipogre.com/linux.php',
        'http://myexternalip.com/raw',
        'http://icanhazip.com/',
        'http://httpbin.org/ip'
    ]

    headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0'}

    for i in range(len(source_list)):

        target = random.choice(source_list)

        try:

            content = requests.get(target, headers=headers, timeout=6, verify=False)

            m = re.search(
                '(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',
                content.text
            )

            ip = m.group(0)

            if len(ip) > 0:
                return ip

        # Without Internet
        except requests.exceptions.ConnectionError as e:

            # Only interested in there kind of error
            if str(e).find("Temporary failure in name resolution") > -1:
                return None

        # Timeout
        except requests.exceptions.RequestException:
            # Try next
            source_list.pop(i)

        except Exception:
            continue


    return None
