import pandas as pd
import numpy as np
from . import getDict

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

        firstPage = int(loc)
        endPage = len(input_df.index) // 10 + 1
        for i, j in zip(range(0, endLoc-startLoc), range(startLoc, endLoc)):
            if game == 0:
                arr.append(str(j) + ". " + df_temp.iloc[i, 1])
                output = "\n".join(arr)
                output_text = "```css\n[Arcaea Song List (" + str(firstPage) + " of " + str(endPage) + ")]\n\n" + output + "\n```"
            elif game == 1:
                arr.append(str(j) + ". " + df_temp.iloc[i, 1])
                output = "\n".join(arr)
                output_text = "```css\n[Cytus2 Song List (" + str(firstPage) + " of " + str(endPage) + ")]\n\n" + output + "\n```"
            elif game == 2:
                arr.append(str(j) + ". " + df_temp.iloc[i, 1])
                output = "\n".join(arr)
                output_text = "```css\n[Dynamix Song List (" + str(firstPage) + " of " + str(endPage) + ")]\n\n" + output + "\n```"
            elif game == 3:
                arr.append(str(j) + ". " + df_temp.iloc[i, 0])
                output = "\n".join(arr)
                output_text = "```css\n[Lanota Song List (" + str(firstPage) + " of " + str(endPage) + ")]\n\n" + output + "\n```"
            elif game == 4:
                arr.append(str(j) + ". " + df_temp.iloc[i, 0])
                output = "\n".join(arr)
                output_text = "```css\n[Deemo Song List (" + str(firstPage) + " of " + str(endPage) + ")]\n\n" + output + "\n```"

        return output_text
    except:
        return 0
