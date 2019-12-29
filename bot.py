import asyncio
import discord
from discord.ext import commands
import pandas as pd
import numpy as np
from difflib import SequenceMatcher
from tools import randomSong, getDict, getSongList, arcaeaProber, getProbeDetail

#Load URL
arcaea_url_list = getDict.arcaea()
cytus2_url_list = getDict.cytus2()
lanota_url_list = getDict.lanota()
deemo_url_list = getDict.deemo()
err_msg = getDict.err()

#Load Song Data
arcaea_df = pd.read_csv("data/arcaea.csv", encoding='utf-8-sig')
cytus2_df = pd.read_csv("data/cytus2.csv", encoding='utf-8-sig')
dynamix_df = pd.read_csv("data/dynamix.csv", encoding='utf-8-sig')
lanota_df = pd.read_csv("data/lanota.csv", encoding='utf-8-sig')
deemo_df = pd.read_csv("data/deemo.csv", encoding='utf-8-sig')

#Bot Information
client = commands.Bot(command_prefix='~')
client.remove_command('help')

token = "NjIyMzQxNzQ2MTg5NDAyMTMy.XXyksg.EZP5X3C4hBF_o_lhIYOWtFuU0A4"

#Login
@client.event
async def on_ready():
    print("다음으로 로그인합니다: ")
    print(client.user.name)
    print(client.user.id)
    print("==========")

    activity = discord.Game(name="Rhymical! :D")
    await client.change_presence(status=discord.Status.online, activity=activity)

#Ping Pong
@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send("pong!")

#Help
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.blue(), title="Rhythmic Command Help", description="Hello! I'm Rhythmic! Here is command list:")
    embed.add_field(name = "ARCAEA", value="`arcaea [search]`: Search for Arcaea song.", inline=True)
    embed.add_field(name = "CYTUS 2", value="`cytus2 [search]`: Search for Cytus2 song.", inline=True)
    embed.add_field(name = "DYNAMIX", value="`dynamix [search]`: Search for Dynamix song.", inline=True)
    embed.add_field(name = "LANOTA", value="`lanota [search]`: Search for Lanota song.", inline=True)
    embed.add_field(name = "DEEMO", value="`deemo [search]`: Search for Deemo song.", inline=True)
    embed.add_field(name = "RANDOM", value="`random [game_name] (level)`: Random Songs! LOL", inline=False)
    embed.add_field(name = "SONG LIST", value="`songlist [game_name] [page_number]`: Get list of songs by DM.", inline=False)
    embed.add_field(name = "PROBER", value="`probe [userid]`: Probe Arcaea user info.\n`probeall [userid] [page_number]`: Probe detailed Arcaea score info.\n`probeall [userid] refresh`: Refresh Arcaea score info.", inline=False)
    embed.set_footer(text="Bot Made by Xestiny_")

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def probe(ctx, *args):
    try:
        if len(args[0]) == 9 and args[0].isdecimal():
            if len(args) == 1:
                embed = discord.Embed(colour = discord.Colour.purple(), title="Arcaea Prober", description="Please wait a few seconds...")
                await ctx.send(embed=embed)

                username, register, ptt, img = await arcaeaProber.arcaea_prober(uid=args[0])

                if register == 0:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Prober", description=err_msg['no_uid'])
                    await ctx.send(embed=embed)
                    print("Arcaea Prober: Wrong UID")
                else:
                    embed = discord.Embed(colour = discord.Colour.purple(), title="Arcaea Prober")
                    embed.add_field(name = "Username", value=username, inline=False)
                    embed.add_field(name = "Register Date", value=register, inline=False)
                    embed.add_field(name = "Potential", value=ptt, inline=False)
                    embed.set_thumbnail(url=img)
                    embed.set_footer(text="UID: " + str(args[0]))
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Prober", description=err_msg['usage_prober'])
                await ctx.send(embed=embed)
                print("Arcaea Prober: Argument Error")
        else:
            embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Prober", description=err_msg['no_uid'])
            await ctx.send(embed=embed)
            print("Arcaea Prober: Wrong UID")
    except:
        embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Prober", description=err_msg['usage_prober'])
        await ctx.send(embed=embed)
        print("Arcaea Prober: Argument Error")

@client.command(pass_context=True)
async def probeall(ctx, *args):
    if len(args) == 2:
        if args[1].lower() == "refresh":
            embed = discord.Embed(colour = discord.Colour.purple(), title="Arcaea Prober", description="Please wait a few seconds...")
            await ctx.send(embed=embed)

            username, register, ptt, img = await arcaeaProber.arcaea_prober_all(uid=args[0])

            if register == 0:
                embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Prober", description=err_msg['no_uid'])
                await ctx.send(embed=embed)
                print("Arcaea Prober: Wrong UID")
            else:
                embed = discord.Embed(colour = discord.Colour.purple(), title="Arcaea Prober", description="Refresh Complete.")
                await ctx.send(embed=embed)
                print("Arcaea Prober: Refresh")
        else:
            embed = discord.Embed(colour = discord.Colour.purple(), title="Arcaea Prober", description="Please wait a few seconds...")
            await ctx.send(embed=embed)

            username, register, ptt, img = await arcaeaProber.arcaea_prober(uid=args[0])

            if register == 0:
                embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Prober", description=err_msg['no_uid'])
                await ctx.send(embed=embed)
                print("Arcaea Prober: Wrong UID")
            else:
                temp = getProbeDetail.getProbeDetail(username, args[1])

                if temp != 0:
                    await ctx.author.send(temp)
                    print("Arcaea Prober: " + args[0])
                elif temp == 0:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Prober", description=err_msg['out_of_index'])
                    await ctx.send(embed=embed)
                    print("Arcaea Prober: Out of index")
    else:
        embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Prober", description=err_msg['usage_prober_all'])
        await ctx.send(embed=embed)
        print("Arcaea Prober: Argument Error")

#Arcaea Search
@client.command(pass_context=True)
async def arcaea(ctx, *, message):
    df_temp = pd.DataFrame()

    try:
        top_ratio = 0.0
        for list in arcaea_df.loc[:, 'song']:
            ratio = SequenceMatcher(None, message, list.lower()).ratio()
            if ratio >= 0.3:
                if ratio >= top_ratio:
                    top_ratio = ratio
                    df_temp = arcaea_df.loc[arcaea_df['song'] == list]

        song = df_temp['song'].values[0]
        artist = df_temp['artist'].values[0]
        pst = str(df_temp['pst'].values[0])
        prs = str(df_temp['prs'].values[0])
        ftr = str(df_temp['ftr'].values[0])
        diff = " / ".join([pst, prs, ftr])
        length = str(df_temp['len'].values[0])
        bpm = str(df_temp['bpm'].values[0])
        pack = df_temp['pack'].values[0]
        version = str(df_temp['update'].values[0])

        embed = discord.Embed(colour = discord.Colour.purple(), title="Arcaea Song Info")
        embed.add_field(name = "Song", value=song, inline=False)
        embed.add_field(name = "Artist", value=artist, inline=False)
        embed.add_field(name = "Difficulty", value=diff, inline=True)
        embed.add_field(name = "Length", value=length, inline=True)
        embed.add_field(name = "BPM", value=bpm, inline=True)
        embed.add_field(name = "Pack", value=pack, inline=True)
        embed.add_field(name = "Updated Version", value=version, inline=True)

        embed.set_thumbnail(url=arcaea_url_list[pack])

        await ctx.send(embed=embed)
        print("Arcaea Song Info: " + song)
    except Exception as e:
        embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Arcaea Song Info: No Result")
        print(e)

#Cytus2 Search
@client.command(pass_context=True)
async def cytus2(ctx, *, message):
    df_temp = pd.DataFrame()

    try:
        top_ratio = 0.0
        for list in cytus2_df.loc[:, 'song']:
            ratio = SequenceMatcher(None, message, list.lower()).ratio()
            if ratio >= 0.3:
                if ratio >= top_ratio:
                    top_ratio = ratio
                    df_temp = cytus2_df.loc[cytus2_df['song'] == list]

        song = df_temp['song'].values[0]
        artist = df_temp['artist'].values[0]
        easy = str(df_temp['easy'].values[0])
        hard = str(df_temp['hard'].values[0])
        chaos = str(df_temp['chaos'].values[0])
        diff = " / ".join([easy, hard, chaos])
        try:
            length_temp = int(df_temp['len'].values[0])
            length = "{0}:{1:02d}".format(length_temp // 60, length_temp % 60)
        except ValueError:
            length = "NaN"
        bpm = str(df_temp['bpm'].values[0])
        character = df_temp['character'].values[0]

        embed = discord.Embed(colour = discord.Colour.blue(), title="Cytus2 Song Info")
        embed.add_field(name = "Song", value=song, inline=False)
        embed.add_field(name = "Artist", value=artist, inline=False)
        embed.add_field(name = "Difficulty", value=diff, inline=True)
        embed.add_field(name = "Length", value=length, inline=True)
        embed.add_field(name = "BPM", value=bpm, inline=True)
        embed.add_field(name = "Character", value=character, inline=True)

        embed.set_thumbnail(url=cytus2_url_list[character])

        await ctx.send(embed=embed)
        print("Cytus2 Song Info: " + song)
    except Exception as e:
        embed = discord.Embed(colour = discord.Colour.red(), title="Cytus2 Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Cytus2 Song Info: No Result")
        print(e)

#Dynamix Search
@client.command(pass_context=True)
async def dynamix(ctx, *, message):
    df_temp = pd.DataFrame()

    try:
        top_ratio = 0.0
        for list in dynamix_df.loc[:, 'song']:
            ratio = SequenceMatcher(None, message, list.lower()).ratio()
            if ratio >= 0.3:
                if ratio >= top_ratio:
                    top_ratio = ratio
                    df_temp = dynamix_df.loc[dynamix_df['song'] == list]

        song = df_temp['song'].values[0]
        artist = df_temp['artist'].values[0]
        casual = str(df_temp['casual'].values[0])
        normal = str(df_temp['normal'].values[0])
        hard = str(df_temp['hard'].values[0])
        mega = str(df_temp['mega'].values[0])
        giga = str(df_temp['giga'].values[0])
        diff = " / ".join([casual, normal, hard, mega, giga])
        bpm = str(df_temp['bpm'].values[0])

        embed = discord.Embed(colour = discord.Colour.dark_blue(), title="Dynamix Song Info")
        embed.add_field(name = "Song", value=song, inline=False)
        embed.add_field(name = "Artist", value=artist, inline=False)
        embed.add_field(name = "Difficulty", value=diff, inline=True)
        embed.add_field(name = "BPM", value=bpm, inline=True)

        await ctx.send(embed=embed)
        print("Dynamix Song Info: " + song)
    except Exception as e:
        embed = discord.Embed(colour = discord.Colour.red(), title="Dynamix Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Dynamix Song Info: No Result")
        print(e)

#Lanota Search
@client.command(pass_context=True)
async def lanota(ctx, *, message):
    df_temp = pd.DataFrame()

    try:
        top_ratio = 0.0
        for list in lanota_df.loc[:, 'song']:
            ratio = SequenceMatcher(None, message, list.lower()).ratio()
            if ratio >= 0.3:
                if ratio >= top_ratio:
                    top_ratio = ratio
                    df_temp = lanota_df.loc[lanota_df['song'] == list]

        song = df_temp['song'].values[0]
        artist = df_temp['artist'].values[0]
        area = df_temp['area'].values[0]
        whisper = str(df_temp['whisper'].values[0])
        acoustic = str(df_temp['acoustic'].values[0])
        ultra = str(df_temp['ultra'].values[0])
        master = str(df_temp['master'].values[0])
        diff = " / ".join([whisper, acoustic, ultra, master])
        length = str(df_temp['length'].values[0])
        bpm = str(df_temp['bpm'].values[0])
        chapter = df_temp['chapter'].values[0]

        embed = discord.Embed(colour = discord.Colour.gold(), title="Lanota Song Info")
        embed.add_field(name = "Song", value=song, inline=False)
        embed.add_field(name = "Artist", value=artist, inline=False)
        embed.add_field(name = "Difficulty", value=diff, inline=True)
        embed.add_field(name = "Length", value=length, inline=True)
        embed.add_field(name = "BPM", value=bpm, inline=True)
        embed.add_field(name = "Chapter", value=chapter, inline=True)
        embed.add_field(name = "Area", value=area, inline=True)

        embed.set_thumbnail(url=lanota_url_list[chapter])

        await ctx.send(embed=embed)
        print("Lanota Song Info: " + song)
    except Exception as e:
        embed = discord.Embed(colour = discord.Colour.red(), title="Lanota Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Lanota Song Info: No Result")
        print(e)

#Lanota Search
@client.command(pass_context=True)
async def deemo(ctx, *, message):
    df_temp = pd.DataFrame()

    try:
        top_ratio = 0.0
        for list in deemo_df.loc[:, 'song']:
            ratio = SequenceMatcher(None, message, list.lower()).ratio()
            if ratio >= 0.3:
                if ratio >= top_ratio:
                    top_ratio = ratio
                    df_temp = deemo_df.loc[deemo_df['song'] == list]

        song = df_temp['song'].values[0]
        artist = df_temp['artist'].values[0]
        easy = str(df_temp['easy'].values[0])
        normal = str(df_temp['normal'].values[0])
        hard = str(df_temp['hard'].values[0])
        extra = str(df_temp['extra'].values[0])
        diff = " / ".join([easy, normal, hard, extra])
        bpm = str(df_temp['bpm'].values[0])
        collection = df_temp['collection'].values[0]

        embed = discord.Embed(colour = discord.Colour.teal(), title="Deemo Song Info")
        embed.add_field(name = "Song", value=song, inline=False)
        embed.add_field(name = "Artist", value=artist, inline=False)
        embed.add_field(name = "Difficulty", value=diff, inline=True)
        embed.add_field(name = "BPM", value=bpm, inline=True)
        embed.add_field(name = "Collection", value=collection, inline=False)

        embed.set_thumbnail(url=deemo_url_list[collection])

        await ctx.send(embed=embed)
        print("Deemo Song Info: " + song)
    except Exception as e:
        embed = discord.Embed(colour = discord.Colour.red(), title="Deemo Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Deemo Song Info: No Result")
        print(e)

#Random Song
@client.command(pass_context=True)
async def random(ctx, *args):
    if len(args) != 0:
        try:
            if args[0].lower() == "arcaea":
                #Check the number of arguments
                if len(args) == 1:
                    temp = randomSong.arcaea(arcaea_df, None)
                elif len(args) == 2:
                    temp = randomSong.arcaea(arcaea_df, args[1])
                else:
                    raise IndexError

                if temp != 0:
                    embed = discord.Embed(colour = discord.Colour.purple(), title="Random Song: Arcaea")
                    embed.add_field(name = "Song", value=temp[0], inline=False)
                    embed.add_field(name = "Artist", value=temp[1], inline=False)
                    embed.add_field(name = "Difficulty", value=temp[2], inline=True)
                    embed.add_field(name = "Length", value=temp[3], inline=True)
                    embed.add_field(name = "BPM", value=temp[4], inline=True)
                    embed.add_field(name = "Pack", value=temp[5], inline=True)
                    embed.add_field(name = "Updated Version", value=temp[6], inline=True)

                    embed.set_thumbnail(url=temp[7])

                    await ctx.send(embed=embed)
                    print("Arcaea Random: " + temp[0])
                #Catch ValueError Exception
                elif temp == 0:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Random Song: Arcaea", description=err_msg['value_error'])
                    await ctx.send(embed=embed)
                    print("Arcaea Random: ValueError")

            elif args[0].lower() == "cytus2":
                if len(args) == 1:
                    temp = randomSong.cytus2(cytus2_df, None)
                elif len(args) == 2:
                    temp = randomSong.cytus2(cytus2_df, args[1])
                else:
                    raise IndexError

                if temp != 0:
                    embed = discord.Embed(colour = discord.Colour.blue(), title="Random Song: Cytus2")
                    embed.add_field(name = "Song", value=temp[0], inline=False)
                    embed.add_field(name = "Artist", value=temp[1], inline=False)
                    embed.add_field(name = "Difficulty", value=temp[2], inline=True)
                    embed.add_field(name = "Length", value=temp[3], inline=True)
                    embed.add_field(name = "BPM", value=temp[4], inline=True)
                    embed.add_field(name = "Character", value=temp[5], inline=True)

                    embed.set_thumbnail(url=temp[6])

                    await ctx.send(embed=embed)
                    print("Cytus2 Random: " + temp[0])
                elif temp == 0:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Random Song: Cytus2", description=err_msg['value_error'])
                    await ctx.send(embed=embed)
                    print("Cytus2 Random: ValueError")

            elif args[0].lower() == "dynamix":
                if len(args) == 1:
                    temp = randomSong.dynamix(dynamix_df, None)
                elif len(args) == 2:
                    temp = randomSong.dynamix(dynamix_df, args[1])
                else:
                    raise IndexError

                if temp != 0:
                    embed = discord.Embed(colour = discord.Colour.dark_blue(), title="Random Song: Dynamix")
                    embed.add_field(name = "Song", value=temp[0], inline=False)
                    embed.add_field(name = "Artist", value=temp[1], inline=False)
                    embed.add_field(name = "Difficulty", value=temp[2], inline=True)
                    embed.add_field(name = "BPM", value=temp[3], inline=True)
                    embed.add_field(name = "Updated Version", value=temp[4], inline=True)

                    await ctx.send(embed=embed)
                    print("Dynamix Random: " + temp[0])
                elif temp == 0:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Random Song: Dynamix", description=err_msg['value_error'])
                    await ctx.send(embed=embed)
                    print("Dynamix Random: ValueError")

            elif args[0].lower() == "lanota":
                if len(args) == 1:
                    temp = randomSong.lanota(lanota_df, None)
                elif len(args) == 2:
                    temp = randomSong.lanota(lanota_df, args[1])
                else:
                    raise IndexError

                if temp != 0:
                    embed = discord.Embed(colour = discord.Colour.gold(), title="Random Song: Lanota")
                    embed.add_field(name = "Song", value=temp[0], inline=False)
                    embed.add_field(name = "Artist", value=temp[1], inline=False)
                    embed.add_field(name = "Difficulty", value=temp[2], inline=True)
                    embed.add_field(name = "Length", value=temp[3], inline=True)
                    embed.add_field(name = "BPM", value=temp[4], inline=True)
                    embed.add_field(name = "Chapter", value=temp[5], inline=True)
                    embed.add_field(name = "Area", value=temp[6], inline=True)

                    embed.set_thumbnail(url=temp[7])

                    await ctx.send(embed=embed)
                    print("Lanota Random: " + temp[0])
                elif temp == 0:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Random Song: Lanota", description=err_msg['value_error'])
                    await ctx.send(embed=embed)
                    print("Lanota Random: ValueError")

            elif args[0].lower() == "deemo":
                if len(args) == 1:
                    temp = randomSong.deemo(deemo_df, None)
                elif len(args) == 2:
                    temp = randomSong.deemo(deemo_df, args[1])
                else:
                    raise IndexError

                if temp != 0:
                    embed = discord.Embed(colour = discord.Colour.teal(), title="Random Song: Deemo")
                    embed.add_field(name = "Song", value=temp[0], inline=False)
                    embed.add_field(name = "Artist", value=temp[1], inline=False)
                    embed.add_field(name = "Difficulty", value=temp[2], inline=True)
                    embed.add_field(name = "BPM", value=temp[3], inline=True)
                    embed.add_field(name = "Collection", value=temp[4], inline=False)

                    embed.set_thumbnail(url=temp[5])

                    await ctx.send(embed=embed)
                    print("Deemo Random: " + temp[0])
                elif temp == 0:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Random Song: Deemo", description=err_msg['value_error'])
                    await ctx.send(embed=embed)
                    print("Deemo Random: ValueError")

            #If input is not existing game
            else:
                embed = discord.Embed(colour = discord.Colour.red(), title="Random Song", description=err_msg['usage_random'])
                await ctx.send(embed=embed)
                print("Random Song: Argument Error")
        #Catch Any Exception
        except Exception as e:
            embed = discord.Embed(colour = discord.Colour.red(), title="Random Song", description=err_msg['usage_random'])
            await ctx.send(embed=embed)
            print("Random Song: Argument Error")
            print(e)
    #No Argument
    else:
        embed = discord.Embed(colour = discord.Colour.red(), title="Random Song", description=err_msg['usage_random'])
        await ctx.send(embed=embed)
        print("Random Song: Argument Error")

@client.command(pass_context=True)
async def songlist(ctx, *args):
    #Check the number of arguments
    if len(args) == 2:
        if args[0].lower() == "arcaea":
            temp = getSongList.getList(arcaea_df, args[1], 0)

            if temp != 0:
                await ctx.author.send(temp)
                print("Arcaea Song List: " + args[1])
            elif temp == 0:
                embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Song List", description=err_msg['out_of_index'])
                await ctx.send(embed=embed)
                print("Arcaea Song List: Out of index")

        elif args[0].lower() == "cytus2":
            temp = getSongList.getList(cytus2_df, args[1], 1)

            if temp != 0:
                await ctx.author.send(temp)
                print("Cytus2 Song List: " + args[1])
            elif temp == 0:
                embed = discord.Embed(colour = discord.Colour.red(), title="Cytus2 Song List", description=err_msg['out_of_index'])
                await ctx.send(embed=embed)
                print("Cytus2 Song List: Out of index")

        elif args[0].lower() == "dynamix":
            temp = getSongList.getList(dynamix_df, args[1], 2)

            if temp != 0:
                await ctx.author.send(temp)
                print("Dynamix Song List: " + args[1])
            elif temp == 0:
                embed = discord.Embed(colour = discord.Colour.red(), title="Dynamix Song List", description=err_msg['out_of_index'])
                await ctx.send(embed=embed)
                print("Dynamix Song List: Out of index")

        elif args[0].lower() == "lanota":
            temp = getSongList.getList(lanota_df, args[1], 3)

            if temp != 0:
                await ctx.author.send(temp)
                print("Lanota Song List: " + args[1])
            elif temp == 0:
                embed = discord.Embed(colour = discord.Colour.red(), title="Lanota Song List", description=err_msg['out_of_index'])
                await ctx.send(embed=embed)
                print("Lanota Song List: Out of index")

        elif args[0].lower() == "deemo":
            temp = getSongList.getList(deemo_df, args[1], 4)

            if temp != 0:
                await ctx.author.send(temp)
                print("Deemo Song List: " + args[1])
            elif temp == 0:
                embed = discord.Embed(colour = discord.Colour.red(), title="Lanota Song List", description=err_msg['out_of_index'])
                await ctx.send(embed=embed)
                print("Deemo Song List: Out of index")

        #If input is not existing game
        else:
            embed = discord.Embed(colour = discord.Colour.red(), title="Song List", description=err_msg['usage_songlist'])
            await ctx.send(embed=embed)
            print("Song List: Unknown Argument")
    #No Argument or only 1 argument
    else:
        embed = discord.Embed(colour = discord.Colour.red(), title="Song List", description=err_msg['usage_songlist'])
        await ctx.send(embed=embed)
        print("Song List: Argument Error")

client.run(token)
