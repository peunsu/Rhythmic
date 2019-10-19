import pandas as pd
import numpy as np
from random import randint
from . import getDict

arcaea_url_list = getDict.arcaea()
cytus2_url_list = getDict.cytus2()

def arcaea(input_df, level):
    df_temp = pd.DataFrame()

    if level == None:
        i = randint(1, len(input_df.index))
        df_temp = input_df.iloc[i-1]
    else:
        try:
            df_temp = input_df.loc[(input_df['pst'].isin([level])) | (input_df['prs'].isin([level])) | (input_df['ftr'].isin([level]))]

            i = randint(1, len(df_temp.index))
            df_temp = df_temp.iloc[i-1]
        except:
            return 0

    output_arr = []

    try:
        output_arr.append(df_temp['song'])
        output_arr.append(df_temp['artist'])
        pst = str(df_temp['pst'])
        prs = str(df_temp['prs'])
        ftr = str(df_temp['ftr'])
        diff = pst + " / " + prs + " / " + ftr
        output_arr.append(diff)
        output_arr.append(str(df_temp['len']))
        output_arr.append(str(df_temp['bpm']))
        output_arr.append(df_temp['pack'])
        output_arr.append(str(df_temp['update']))
        output_arr.append(arcaea_url_list[df_temp['pack']])

        return output_arr
    except:
        return 0

def cytus2(input_df, level):
    df_temp = pd.DataFrame()

    if level == None:
        i = randint(1, len(input_df.index))
        df_temp = input_df.iloc[i-1]
    else:
        try:
            df_temp = input_df.loc[(input_df['easy'].isin([level])) | (input_df['hard'].isin([level])) | (input_df['chaos'].isin([level]))]

            i = randint(1, len(df_temp.index))
            df_temp = df_temp.iloc[i-1]
        except:
            return 0

    output_arr = []

    try:
        output_arr.append(df_temp['song'])
        output_arr.append(df_temp['artist'])
        easy = str(df_temp['easy'])
        hard = str(df_temp['hard'])
        chaos = str(df_temp['chaos'])
        diff = easy + " / " + hard + " / " + chaos
        output_arr.append(diff)
        try:
            length_temp = int(df_temp['len'])
            length = "{0}:{1:02d}".format(length_temp // 60, length_temp % 60)
        except ValueError:
            length = "NaN"
        output_arr.append(length)
        output_arr.append(str(df_temp['bpm']))
        output_arr.append(df_temp['character'])
        output_arr.append(cytus2_url_list[df_temp['character']])

        return output_arr
    except:
        return 0

def dynamix(input_df, level):
    df_temp = pd.DataFrame()

    if level == None:
        i = randint(1, len(input_df.index))
        df_temp = pd.DataFrame()
        df_temp = input_df.iloc[i-1]
    else:
        try:
            df_temp = input_df.loc[(input_df['casual'].isin([level])) | (input_df['normal'].isin([level])) | (input_df['hard'].isin([level])) | (input_df['mega'].isin([level])) | (input_df['giga'].isin([level]))]

            i = randint(1, len(df_temp.index))
            df_temp = df_temp.iloc[i-1]
        except:
            return 0

    output_arr = []

    try:
        output_arr.append(df_temp['song'])
        output_arr.append(df_temp['artist'])
        casual = str(df_temp['casual'])
        normal = str(df_temp['normal'])
        hard = str(df_temp['hard'])
        mega = str(df_temp['mega'])
        giga = str(df_temp['giga'])
        diff = casual + " / " + normal + " / " + hard + " / " + mega + " / " + giga
        output_arr.append(diff)
        output_arr.append(str(df_temp['bpm']))
        output_arr.append(df_temp['update'])

        return output_arr
    except:
        return 0
