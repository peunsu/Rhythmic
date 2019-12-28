import urllib.request
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from tools import getDict

url_list = getDict.deemo_data()

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
    df = pd.DataFrame(columns=['song', 'artist', 'easy', 'normal', 'hard', 'extra', 'bpm', 'collection'])

    j = 0
    for input, chapter in zip(inputData, chapterList):
        soup = BeautifulSoup(input, "html.parser")

        if chapter == "Deemo's Collection Vol. 1A" or chapter == "Deemo's Collection Vol. 1B" or chapter == "Deemo's Collection Vol. 2" or chapter == "Shattered Memories" or chapter == "Shattered Memories 2" or chapter == "Samsara Collection" or chapter == "Etude Collection" or chapter == "Collaboration Collection":
            i = 0
            arr = []
            for item in soup.find('table').findAll("td"):
                text = item.text.replace("\n", " ").strip()

                if i % 8 != 7:
                    if text == "":
                        arr.append("-")
                    else:
                        arr.append(text)

                if len(arr) == 7:
                    arr.append(chapter)
                    df.loc[j] = arr
                    arr.clear()
                    j = j + 1
                i = i + 1
        elif chapter == "Ice Collection":
            i = 0
            arr = []
            for item in soup.find('table').findAll("td"):
                text = item.text.replace("\n", " ").strip()

                if text == "":
                    arr.append("-")

                if len(arr) == 7:
                    arr.append(chapter)
                    df.loc[j] = arr
                    arr.clear()
                    j = j + 1
                i = i + 1
        else:
            i = 0
            arr = []
            for item in soup.find('table').findAll("td"):
                text = item.text.replace("\n", " ").strip()

                if i % 6 == 4:
                    arr.append(text)
                    arr.append("-")
                else:
                    if text == "":
                        arr.append("-")
                    else:
                        arr.append(text)

                if len(arr) == 7:
                    arr.append(chapter)
                    df.loc[j] = arr
                    arr.clear()
                    j = j + 1
                i = i + 1

    df.to_csv(os.path.join(output_path, output_file), encoding='utf-8-sig', index=False, header=True)

data = []
for url in url_list.values():
    data.append(query_sender(url))

output_path = "data"
output_file = "deemo.csv"

chk_existence(output_path, output_file)
process_data(data, url_list.keys())
