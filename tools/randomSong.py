import pandas as pd
import numpy as np
from random import randint
from . import getDict

arcaea_url_list = getDict.arcaea()
cytus2_url_list = getDict.cytus2()
lanota_url_list = getDict.lanota()
deemo_url_list = getDict.deemo()

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
        except Exception as e:
            print(e)
            return 0

    output_arr = []

    try:
        output_arr.append(df_temp['song'])
        output_arr.append(df_temp['artist'])
        pst = str(df_temp['pst'])
        prs = str(df_temp['prs'])
        ftr = str(df_temp['ftr'])
        diff = " / ".join([pst, prs, ftr])
        output_arr.append(diff)
        output_arr.append(str(df_temp['len']))
        output_arr.append(str(df_temp['bpm']))
        output_arr.append(df_temp['pack'])
        output_arr.append(str(df_temp['update']))
        output_arr.append(arcaea_url_list[df_temp['pack']])

        return output_arr
    except Exception as e:
        print(e)
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
        except Exception as e:
            print(e)
            return 0

    output_arr = []

    try:
        output_arr.append(df_temp['song'])
        output_arr.append(df_temp['artist'])
        easy = str(df_temp['easy'])
        hard = str(df_temp['hard'])
        chaos = str(df_temp['chaos'])
        diff = " / ".join([easy, hard, chaos])
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
    except Exception as e:
        print(e)
        return 0

def dynamix(input_df, level):
    df_temp = pd.DataFrame()

    if level == None:
        i = randint(1, len(input_df.index))
        df_temp = input_df.iloc[i-1]
    else:
        try:
            df_temp = input_df.loc[(input_df['casual'].isin([level])) | (input_df['normal'].isin([level])) | (input_df['hard'].isin([level])) | (input_df['mega'].isin([level])) | (input_df['giga'].isin([level]))]

            i = randint(1, len(df_temp.index))
            df_temp = df_temp.iloc[i-1]
        except Exception as e:
            print(e)
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
        diff = " / ".join([casual, normal, hard, mega, giga])
        output_arr.append(diff)
        output_arr.append(str(df_temp['bpm']))
        output_arr.append(df_temp['update'])

        return output_arr
    except Exception as e:
        print(e)
        return 0

def lanota(input_df, level):
    df_temp = pd.DataFrame()

    if level == None:
        i = randint(1, len(input_df.index))
        df_temp = input_df.iloc[i-1]
    else:
        try:
            df_temp = input_df.loc[(input_df['whisper'].isin([level])) | (input_df['acoustic'].isin([level])) | (input_df['ultra'].isin([level])) | (input_df['master'].isin([level]))]

            i = randint(1, len(df_temp.index))
            df_temp = df_temp.iloc[i-1]
        except Exception as e:
            print(e)
            return 0

    output_arr = []

    try:
        output_arr.append(df_temp['song'])
        output_arr.append(df_temp['artist'])
        whisper = str(df_temp['whisper'])
        acoustic = str(df_temp['acoustic'])
        ultra = str(df_temp['ultra'])
        master = str(df_temp['master'])
        diff = " / ".join([whisper, acoustic, ultra, master])
        output_arr.append(diff)
        output_arr.append(str(df_temp['length']))
        output_arr.append(str(df_temp['bpm']))
        output_arr.append(df_temp['chapter'])
        output_arr.append(df_temp['area'])
        output_arr.append(lanota_url_list[df_temp['chapter']])

        return output_arr
    except Exception as e:
        print(e)
        return 0

def deemo(input_df, level):
    df_temp = pd.DataFrame()

    if level == None:
        i = randint(1, len(input_df.index))
        df_temp = input_df.iloc[i-1]
    else:
        try:
            df_temp = input_df.loc[(input_df['easy'].isin([level])) | (input_df['normal'].isin([level])) | (input_df['hard'].isin([level])) | (input_df['extra'].isin([level]))]

            i = randint(1, len(df_temp.index))
            df_temp = df_temp.iloc[i-1]
        except Exception as e:
            print(e)
            return 0

    output_arr = []

    try:
        output_arr.append(df_temp['song'])
        output_arr.append(df_temp['artist'])
        easy = str(df_temp['easy'])
        normal = str(df_temp['normal'])
        hard = str(df_temp['hard'])
        extra = str(df_temp['extra'])
        diff = " / ".join([easy, normal, hard, extra])
        output_arr.append(diff)
        output_arr.append(str(df_temp['bpm']))
        output_arr.append(df_temp['collection'])
        output_arr.append(deemo_url_list[df_temp['collection']])

        return output_arr
    except Exception as e:
        print(e)
        return 0
