import urllib.request
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from tools import getDict

url_list = getDict.lanota_data()

def query_sender(url):
    request = urllib.request.Request(url)
    request.get_method = lambda: 'GET'

    responce_body = urllib.request.urlopen(request).read()
    return responce_body

def chk_existence(output_path, output_file):
    savePath = output_path
    saveFile = output_file
    if not os.path.exists(savePath):
        os.makedirs(savePath)

def process_data(inputData, chapterList):
    df = pd.DataFrame(columns=['song', 'artist', 'area', 'whisper', 'acoustic', 'ultra', 'master', 'length', 'bpm', 'chapter'])

    j = 0
    for input, chapter in zip(inputData, chapterList):
        soup = BeautifulSoup(input, "html.parser")
        
        if chapter == 'Chapter ∞':
            i = 0
            arr = []
            for item in soup.find('table').findAll("td"):
                text = item.text.replace("\n", " ").rstrip()

                if text and i % 10 != 9:
                    arr.append(text)

                if len(arr) == 9:
                    arr.append(chapter)
                    df.loc[j] = arr
                    print(arr)
                    arr.clear()
                    j = j + 1
                i = i + 1
        else:
            soup = BeautifulSoup(input, "html.parser")

            i = 0
            arr = []
            for item in soup.find('table').findAll("td"):
                text = item.text.replace("\n", " ").rstrip()

                if text and i % 11 != 9 and i % 11 != 10:
                    arr.append(text)

                if len(arr) == 9:
                    arr.append(chapter)
                    df.loc[j] = arr
                    print(arr)
                    arr.clear()
                    j = j + 1
                i = i + 1

    df.to_csv(os.path.join(output_path, output_file), encoding='utf-8-sig', index=False, header=True)

data = []
for url in url_list.values():
    data.append(query_sender(url))

output_path = "data"
output_file = "lanota.csv"

chk_existence(output_path, output_file)
process_data(data, url_list.keys())
