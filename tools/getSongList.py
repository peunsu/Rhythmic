import pandas as pd
import numpy as np
from . import getDict

arcaea_url_list = getDict.arcaea()
cytus2_url_list = getDict.cytus2()

def getList(input_df, loc, game):
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

        firstPage = int(loc) // 10 + 1
        endPage = len(input_df.index) // 10 + 1
        for i, j in zip(range(0, endLoc-startLoc), range(startLoc, endLoc)):
            arr.append(str(j) + ". " + df_temp.iloc[i, 1])
            output = "\n".join(arr)
            if game == 0:
                output_text = "```css\n[Arcaea Song List (" + str(firstPage) + " of " + str(endPage) + ")]\n\n" + output + "\n```"
            elif game == 1:
                output_text = "```css\n[Cytus2 Song List (" + str(firstPage) + " of " + str(endPage) + ")]\n\n" + output + "\n```"
            elif game == 2:
                output_text = "```css\n[Dynamix Song List (" + str(firstPage) + " of " + str(endPage) + ")]\n\n" + output + "\n```"

        return output_text
    except:
        return 0
