#!/usr/bin/env python3
__author__ = 'Wan Pei Chih <davidwan58@gmail.com>'

import sys
def str2bool(s):
    if s.strip() == 'True':
        return True
    elif s.strip() == 'False':
        return False
    else:
        raise ValueError

def resPage():
    import requests
    URL = 'https://myip.com.tw'
    Ses = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = Ses.get(URL, headers=headers)
    except Exception as e:
        print('Resolve URL fail!')
        if DEBUG:
            print(e)
        os._exit(255)
    if response.status_code != 200:
        sys.exit('The url(%s) get to fail!' %URL)
    else:
        return analyseHtml(response.text)

def analyseHtml(text):
    try:
        from lxml import etree
    except:
        sys.exit('YOUR PYTHON3 NEED INSTALL "lxml" MODULE')
    html = etree.HTML(text)
    return ''.join(html.xpath('//h1/font/text()'))


if __name__ == '__main__':
    import os
    if 'DEBUG' not in os.environ.keys():
        DEBUG = False
    else:
        try:
            DEBUG = str2bool(os.environ['DEBUG'])
        except ValueError:
            DEBUG = False

    res = resPage()
    print(res)


