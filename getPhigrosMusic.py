import urllib.request
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def query_sender():
    url = 'https://phigros.fandom.com/wiki/Songs'
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
    df = pd.DataFrame(columns=['song', 'artist', 'ez', 'hd', 'in', 'sp', 'len', 'pack'])

    soup = BeautifulSoup(inputData, "html.parser")

    i = 0
    arr = []
    for item in soup.find('table').findAll("td"):
        textdata = item.text.strip()
        if textdata == "":
            arr.append("-")
        else:
            arr.append(textdata)
        if len(arr) == 8:
            df.loc[i] = arr
            print(arr)
            arr.clear()

        i = i + 1

    df.to_csv(os.path.join(output_path, output_file), encoding='utf-8-sig', index=False, header=True)

data = query_sender()

output_path = "data"
output_file = "phigros.csv"

chk_existence(output_path, output_file)
process_data(data)
