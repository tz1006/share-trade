#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: trade.py

from ghost import Ghost, Session
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image



gh = Ghost()
se = Session(gh, wait_timeout=30, wait_callback=None, display=True, viewport_size=(800, 680), download_images=True)

username = '880001112385'

def login(username, password):
    url = 'https://trade.cgws.com/cgi-bin/user/Login'
    se.open(url)
    # username
    se.set_field_value('#fundAccount', username)
    # password
    #se.show()
    se.fire('#normalpassword', 'focus')
    #se.sleep(0.1)
    html = se.content
    soup =  BeautifulSoup(html, "html.parser")
    keys = soup.select('tbody > tr > td')
    key_list = []
    for key in keys:
        key_list.append(key.text)
    for i in password:
        m = (key_list.index(i) // 4) + 1
        n = (key_list.index(i) % 4) + 1
        se.click('tbody > tr:nth-child(%s) > td:nth-child(%s)' % (m, n))
    # vcode
    se.capture_to('s/vcode.png', selector='#ticketImg')
    image = Image.open('s/vcode.png')
    vcode = pytesseract.image_to_string(image)
    se.set_field_value('#ticket', vcode)
    se.sleep(0.1)
    se.click('#submit', expect_loading=True)


login(username, password)

    
    
url = 'https://trade.cgws.com/cgi-bin/user/Login'
se.open(url)
# username
se.set_field_value('#fundAccount', username)
# password
se.fire('#normalpassword', 'focus')
se.show()
html = se.content
soup =  BeautifulSoup(html, "html.parser")
keys = soup.select('tbody > tr > td')
key_list = []
for key in keys:
    key_list.append(key.text)

for i in password:
    m = (key_list.index(i) // 4) + 1
    n = (key_list.index(i) % 4) + 1
    se.click('tbody > tr:nth-child(%s) > td:nth-child(%s)' % (m, n))

#se.click('tbody > tr:nth-child(2) > td:nth-child(2)')
se.capture_to('s/vcode.png', selector='#ticketImg')
image = Image.open('s/vcode.png')
vcode = pytesseract.image_to_string(image)
se.set_field_value('#ticket', vcode)
#se.click('#submit')
    
    


