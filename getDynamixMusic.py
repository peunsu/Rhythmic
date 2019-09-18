import urllib.request
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def query_sender(url_input):
    url = url_input
    request = urllib.request.Request(url)
    request.get_method = lambda: 'GET'

    responce_body = urllib.request.urlopen(request).read()
    return responce_body

def chk_existence(output_path, output_file):
    savePath = output_path
    saveFile = output_file
    if not os.path.exists(savePath):
        os.makedirs(savePath)

def process_data(inputData, bpmData):
    df = pd.DataFrame(columns=['no', 'song', 'artist', 'casual', 'normal', 'hard', 'mega', 'giga', 'update'])

    soup = BeautifulSoup(inputData, "html.parser")

    i = 0
    arr = []
    for item in soup.find('table').findAll("tr"):
        if i != 0:
            textdata = item.text.split('\n')
            for text, j in zip(textdata, range(0, len(textdata))):
                if text != "":
                    arr.append(text)
            print(arr)
            df.loc[i-1] = arr
            arr.clear()
        i = i + 1

    df_bpm = pd.DataFrame(columns=['no', 'bpm'])

    soup_bpm = BeautifulSoup(bpmData, "html.parser")

    k = 0
    arr = []
    for item in soup_bpm.find('table').findAll("tr"):
        if k >= 2:
            textdata = item.text.split('\n')
            for text, j in zip(textdata, range(0, len(textdata))):
                if j == 1 or j == 4:
                    arr.append(text)
            print(arr)
            df_bpm.loc[k-2] = arr
            arr.clear()
        k = k + 1

    df_output = pd.merge(df, df_bpm, on="no")
    df_output.to_csv(os.path.join(output_path, output_file), encoding='utf-8-sig', index=False, header=True)

data = query_sender('https://dynamixc4cat.fandom.com/wiki/Songs_by_Artist')
data_bpm = query_sender('https://dynamixc4cat.fandom.com/wiki/Songs_by_BPM')

output_path = "data"
output_file = "dynamix.csv"

chk_existence(output_path, output_file)
process_data(data, data_bpm)
