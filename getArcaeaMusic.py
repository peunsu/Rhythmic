import urllib.request
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def query_sender():
    url = 'https://lowiro.fandom.com/wiki/Songs_by_Date'
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
    df = pd.DataFrame(columns=['no', 'song', 'artist', 'pst', 'prs', 'ftr', 'len', 'bpm', 'pack', 'update'])

    soup = BeautifulSoup(inputData, "html.parser")

    i = 0
    arr = []
    for item in soup.find('table').findAll("tr"):
        textdata = item.text.split('\n')
        for text in textdata:
            if text == "":
                continue
            else:
                arr.append(text)
        if len(arr) == 10:
            df.loc[i] = arr
        arr.clear()

        i = i + 1

    df = df.replace({
        ' Arc': 'Arcaea',
        ' EC': 'Eternal Core',
        ' CS': 'Crimson Solace',
        ' MA': 'Memory Archive',
        ' Dnx': 'Dynamix Collaboration',
        ' AV': 'Ambivalent Vision',
        ' VL': 'Vicious Labyrinth',
        ' Stl': 'Stellights Collaboration',
        ' Lnt': 'Lanota Collaboration',
        ' BE': 'Binary Enfold',
        ' LS': 'Luminous Sky',
        ' TS': 'Tone Sphere Collaboration',
        ' GC': 'Groove Coaster Collaboration',
        ' AR': 'Absolute Reason',
        ' CHN': 'CHUNITHM Collaboration',
        ' AP': 'Adverse Prelude',
        ' SR': 'Sunset Radiance'})

    df.to_csv(os.path.join(output_path, output_file), encoding='utf-8-sig', index=False, header=True)

data = query_sender()

output_path = "data"
output_file = "arcaea.csv"

chk_existence(output_path, output_file)
process_data(data)
