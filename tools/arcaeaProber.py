from arsenic import get_session
from arsenic.browsers import Chrome
from arsenic.services import Chromedriver
from bs4 import BeautifulSoup
import re
import shutil
import os
import functools
import asyncio

path = "D:/Github/Rhythm-Game-bot"
download_dir = "C:/Users/PJK/Downloads/"

def browser():
    service = Chromedriver(binary=path + "/tools/chromedriver.exe")
    browser = Chrome()
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(uid):
            async with get_session(service, browser) as session:
                copy_func = functools.partial(func, session=session, uid=uid)
                return await copy_func()
        return wrapped
    return wrapper

@browser()
async def arcaea_prober(session, uid):
    await session.get("https://redive.estertion.win/arcaea/probe/")

    submit = await session.get_element('button[id="submit"]')
    input = await session.get_element('input[id="user-code"]')

    await input.send_keys(uid)
    await submit.click()

    await asyncio.sleep(3.0)
    html = await session.get_page_source()

    soup = BeautifulSoup(html, 'html.parser')

    try:
        username = re.sub('UID:\s\d+', '', soup.select('#user-info > div.name')[0].text).strip()
        register = soup.select('#user-info > div.join-date > span > span.hover')[0].text
        ptt = soup.select('#user-info > div.ptt')[0].text[5:]
        img = soup.select('#user-info > img')[0]['src']
        img = "https://redive.estertion.win/arcaea" + img[2:]

        return username, register, ptt, img
    except IndexError as e:
        return 0, 0, 0, 0
        print(e)

@browser()
async def arcaea_prober_all(session, uid):
    await session.get("https://redive.estertion.win/arcaea/probe/")

    submit = await session.get_element('button[id="submit"]')
    export = await session.get_element('button[id="export"]')
    input = await session.get_element('input[id="user-code"]')

    await input.send_keys(uid)
    await submit.click()

    await asyncio.sleep(3.0)
    html = await session.get_page_source()

    soup = BeautifulSoup(html, 'html.parser')

    try:
        username = re.sub('UID:\s\d+', '', soup.select('#user-info > div.name')[0].text).strip()
        register = soup.select('#user-info > div.join-date > span > span.hover')[0].text
        ptt = soup.select('#user-info > div.ptt')[0].text[5:]
        img = soup.select('#user-info > img')[0]['src']
        img = "https://redive.estertion.win/arcaea" + img[2:]

        await asyncio.sleep(6.0)
        await export.click()

        doFileExist = False
        while doFileExist == False:
            file_list = os.listdir(download_dir)
            for list in file_list:
                if list[-4:] == ".csv":
                    shutil.move(download_dir + list, path + "/data/arcaea_probe/" + list)
                    doFileExist = True

        return username, register, ptt, img
    except IndexError as e:
        return 0, 0, 0, 0
        print(e)

#arcaea_prober('565336311')
