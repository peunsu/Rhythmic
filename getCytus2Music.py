import urllib.request
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def query_sender():
    url = 'https://cytus.fandom.com/wiki/Songs_Imformation_(Cytus_II)'
    request = urllib.request.Request(url)
    request.get_method = lambda: 'GET'

    responce_body = urllib.request.urlopen(request).read()
    return responce_body

def chk_existence(output_path, output_file):
    savePath = output_path
    saveFile = output_file
    if not os.path.exists(savePath):
        os.makedirs(savePath)

def process_data(inputData):
    df = pd.DataFrame(columns=['character', 'song', 'artist', 'len', 'bpm', 'easy', 'hard', 'chaos'])

    soup = BeautifulSoup(inputData, "html.parser")

    i = 0
    arr = []
    for item in soup.find('table').findAll("tr"):
        if i != 0:
            textdata = str(item).replace("\n<p> ", "").replace("\n</p>", "").replace("</td>", "").replace("<p>\n", "").split("\n<td>")
            for text, j in zip(textdata, range(0, len(textdata))):
                if (j >= 1 and j <= 6) or j == 10 or j == 14:
                    arr.append(text)
            df.loc[i-1] = arr
            arr.clear()
        i = i + 1

    df = df.replace({'character': r'^N.*$'}, {'character': 'NEKO#ΦωΦ'}, regex=True)
    df = df.replace({'character': r'^P.*$'}, {'character': 'Paff'}, regex=True)
    df = df.replace({'character': r'^R.*$'}, {'character': 'ROBO_Head'}, regex=True)
    df = df.replace({'character': r'^I.*$'}, {'character': 'Ivy'}, regex=True)
    df = df.replace({'character': r'^M.*$'}, {'character': 'Miku'}, regex=True)
    df = df.replace({'character': r'^X.*$'}, {'character': 'Xenon'}, regex=True)
    df = df.replace({'character': r'^C.*$'}, {'character': 'ConneR'}, regex=True)
    df = df.replace({'character': r'^H.*$'}, {'character': 'Cherry'}, regex=True)
    df = df.replace({'character': r'^J.*$'}, {'character': 'Joe'}, regex=True)
    df = df.replace({'character': r'^A.*$'}, {'character': 'Aroma'}, regex=True)
    df = df.replace({'character': r'^O.*$'}, {'character': 'Nora'}, regex=True)
    df = df.replace({'character': r'^E.*$'}, {'character': 'Neko'}, regex=True)


    df.to_csv(os.path.join(output_path, output_file), encoding='utf-8-sig', index=False, header=True)

data = query_sender()

output_path = "data"
output_file = "cytus2.csv"

chk_existence(output_path, output_file)
process_data(data)
