import pandas as pd
import numpy as np
from . import getDict

def getProbeDetail(username, loc):
    input_df = pd.read_csv("data/arcaea_probe/Arcaea - " + username + ".csv", encoding='utf-8-sig')
    try:
        startLoc = int(loc) * 10 - 9
        endLoc = int(loc) * 10 + 1
        if endLoc > len(input_df.index):
            endLoc = len(input_df.index)
        elif startLoc >= len(input_df.index):
            raise IndexError

        df_temp = pd.DataFrame()
        df_temp = input_df.iloc[startLoc:endLoc]

        arr = []

        firstPage = int(loc)
        endPage = len(input_df.index) // 10 + 1
        for i, j in zip(range(0, endLoc-startLoc), range(startLoc, endLoc)):
            arr.append("  ".join([str(j), df_temp.iloc[i, 0], df_temp.iloc[i, 1], str(df_temp.iloc[i, 2]), str(df_temp.iloc[i, 3]), str(round(df_temp.iloc[i, 4], 2))]))
            output = "\n".join(arr)
            output_text = "```css\n[Arcaea Probe (" + str(firstPage) + " of " + str(endPage) + ")]\n\nNO  Song  Difficulty  Constant  Score  Rating\n" + output + "\n```"

        return output_text
    except Exception as e:
        print(e)
        return 0
