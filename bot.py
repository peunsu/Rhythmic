import asyncio
import discord
from discord.ext import commands
import pandas as pd
import numpy as np
from difflib import SequenceMatcher
from random import randint

arcaea_df = pd.read_csv("data/arcaea.csv", encoding='utf-8-sig')
cytus2_df = pd.read_csv("data/cytus2.csv", encoding='utf-8-sig')

arcaea_url_list = {
    'Arcaea': 'https://vignette.wikia.nocookie.net/iowiro/images/7/7d/Pack-arcaea.png/',
    'Adverse Prelude': 'https://vignette.wikia.nocookie.net/iowiro/images/2/23/Pack_AP.png/',
    'Luminous Sky': 'https://vignette.wikia.nocookie.net/iowiro/images/e/e9/Luminous_sky.png/',
    'Vicious Labyrinth': 'https://vignette.wikia.nocookie.net/iowiro/images/3/34/Pack-viciouslabyrinth.png/',
    'Eternal Core': 'https://vignette.wikia.nocookie.net/iowiro/images/1/17/Pack-eternalcore.png/',
    'Sunset Radiance': 'https://vignette.wikia.nocookie.net/iowiro/images/e/ed/Pack-sunsetradiance.png/',
    'Absolute Reason': 'https://vignette.wikia.nocookie.net/iowiro/images/2/21/Pack-absolutereason.png/',
    'Binary Enfold': 'https://vignette.wikia.nocookie.net/iowiro/images/8/86/Pack-binaryenfold.png/',
    'Ambivalent Vision': 'https://vignette.wikia.nocookie.net/iowiro/images/9/99/Pack-ambivalentvision.png/',
    'Crimson Solace': 'https://vignette.wikia.nocookie.net/iowiro/images/2/2e/Pack-crimsonsolace.png/',
    'CHUNITHM Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/a/a0/Pack_CHUNITHM.png/',
    'Groove Coaster Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/2/23/Pack_groove_coaster.png/',
    'Tone Sphere Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/e/e4/Tone_sphere_collaboration_pack.jpg/',
    'Lanota Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/8/80/Pack-lanota.png/',
    'Stellights Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/9/9d/Pack-stellights.png/',
    'Dynamix Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/c/c6/Pack-dynamix.png',
    'Memory Archive': 'https://vignette.wikia.nocookie.net/iowiro/images/6/66/Pack-memoryarchive.png/'
    }
cytus2_url_list = {
    'Paff': 'https://vignette.wikia.nocookie.net/cytus/images/9/96/Paff_Logo.png/revision/latest/scale-to-width-down/100?cb=20190701061057',
    'NEKO#ΦωΦ': 'https://vignette.wikia.nocookie.net/cytus/images/0/00/Neko_Logo.png/revision/latest/scale-to-width-down/100?cb=20180121105714',
    'ROBO_Head': 'https://vignette.wikia.nocookie.net/cytus/images/2/24/ROBO_Head_Logo.png/revision/latest/scale-to-width-down/100?cb=20180121105714',
    'Ivy': 'https://vignette.wikia.nocookie.net/cytus/images/4/4d/Ivy%27s_logo.png/revision/latest/scale-to-width-down/100?cb=20190113100008',
    'Miku': 'https://vignette.wikia.nocookie.net/cytus/images/c/ca/Miku_Logo.png/revision/latest/scale-to-width-down/100?cb=20190531143142',
    'Xenon': 'https://vignette.wikia.nocookie.net/cytus/images/6/65/Xenon_Logo.png/revision/latest?cb=20180121105713',
    'ConneR': 'https://vignette.wikia.nocookie.net/cytus/images/6/61/ConneR_Logo.png/revision/latest/scale-to-width-down/100?cb=20180121105714',
    'Cherry': 'https://vignette.wikia.nocookie.net/cytus/images/7/72/Cherry_Logo.png/revision/latest/scale-to-width-down/180?cb=20180309162205',
    'Joe': 'https://vignette.wikia.nocookie.net/cytus/images/5/52/68d7232784f8f125afde723b8c698bea1adc97bacb45e55abb0e2f63e35772c4046c9c191a95878cb6252683c58ab450628c2038fb89af4a9954fcf31395d29a6e9139c4e44e8968643edd639a142ee3.png/revision/latest?cb=20181007133420',
    'Aroma': 'https://vignette.wikia.nocookie.net/cytus/images/e/e3/Aroma_Logo.png/revision/latest?cb=20181007160910',
    'Nora': 'https://vignette.wikia.nocookie.net/cytus/images/f/fb/Nora_Logo.png/revision/latest?cb=20181101015219',
    'Neko': 'https://vignette.wikia.nocookie.net/cytus/images/e/e0/Neko_Logo2.png/revision/latest?cb=20190701045301'
    }

err_msg = {
    'no_result': "No search results found. Please search correct song name.",
    'unknown': "Unknown error occured.",
    'out_of_index': "Out of index. Input existing list number.",
    'value_error': "Input existing level.",
    'usage_random': "Usage: random [arcaea/cytus2] (level)",
    'usage_songlist': "Usage: songlist [arcaea/cytus2] [listnumber]"
    }

client = commands.Bot(command_prefix='~')
client.remove_command('help')

token = "NjIyMzQxNzQ2MTg5NDAyMTMy.XXyksg.EZP5X3C4hBF_o_lhIYOWtFuU0A4"

@client.event
async def on_ready():
    print("다음으로 로그인합니다: ")
    print(client.user.name)
    print(client.user.id)
    print("==========")

    activity = discord.Game(name="Rhymical! :D")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send("pong!")

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.blue(), title="Rhythmic Command Help", description="Hello! I'm Rhythmic! Here is command list:")
    embed.add_field(name = "ARCAEA", value="`arcaea [search]`: Search for Arcaea song info.", inline=False)
    embed.add_field(name = "CYTUS 2", value="`cytus2 [search]`: Search for Cytus2 song info.", inline=False)
    embed.add_field(name = "RANDOM", value="`random [arcaea/cytus2] (level)`: Random Songs! LOL")
    embed.add_field(name = "SONG LIST", value="`songlist [arcaea/cytus2] [listnumber]`: Get list of songs.")
    #embed.add_field(name = "LANOTA", value="`random`", inline=False)
    embed.set_footer(text="Bot Made by Xestiny_")

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def arcaea(ctx, *, message):
    df_temp = pd.DataFrame()

    for list in arcaea_df.loc[:, 'song']:
        ratio = SequenceMatcher(None, message, list.lower()).ratio()
        if ratio >= 0.7:
            df_temp = arcaea_df.loc[arcaea_df['song'] == list]

    try:
        song = df_temp['song'].values[0]
        artist = df_temp['artist'].values[0]
        pst = str(df_temp['pst'].values[0])
        prs = str(df_temp['prs'].values[0])
        ftr = str(df_temp['ftr'].values[0])
        diff = pst + " / " + prs + " / " + ftr
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
    except KeyError:
        embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Arcaea Song Info: No Result")

@client.command(pass_context=True)
async def cytus2(ctx, *, message):
    df_temp = pd.DataFrame()

    for list in cytus2_df.loc[:, 'song']:
        ratio = SequenceMatcher(None, message, list.lower()).ratio()
        if ratio >= 0.7:
            df_temp = cytus2_df.loc[cytus2_df['song'] == list]

    try:
        song = df_temp['song'].values[0]
        artist = df_temp['artist'].values[0]
        easy = str(df_temp['easy'].values[0])
        hard = str(df_temp['hard'].values[0])
        chaos = str(df_temp['chaos'].values[0])
        diff = easy + " / " + hard + " / " + chaos
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
    except KeyError:
        embed = discord.Embed(colour = discord.Colour.red(), title="Cytus2 Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Cytus2 Song Info: No Result")

@client.command(pass_context=True)
async def random(ctx, *args):
    if len(args) != 0:
        if len(args) == 1:
            if args[0].lower() == "arcaea":
                i = randint(1, len(arcaea_df.index))
                df_temp = pd.DataFrame()
                df_temp = arcaea_df.iloc[i-1]

                try:
                    song = df_temp['song']
                    artist = df_temp['artist']
                    pst = str(df_temp['pst'])
                    prs = str(df_temp['prs'])
                    ftr = str(df_temp['ftr'])
                    diff = pst + " / " + prs + " / " + ftr
                    length = str(df_temp['len'])
                    bpm = str(df_temp['bpm'])
                    pack = df_temp['pack']
                    version = str(df_temp['update'])

                    embed = discord.Embed(colour = discord.Colour.purple(), title="Random Song: Arcaea")
                    embed.add_field(name = "Song", value=song, inline=False)
                    embed.add_field(name = "Artist", value=artist, inline=False)
                    embed.add_field(name = "Difficulty", value=diff, inline=True)
                    embed.add_field(name = "Length", value=length, inline=True)
                    embed.add_field(name = "BPM", value=bpm, inline=True)
                    embed.add_field(name = "Pack", value=pack, inline=True)
                    embed.add_field(name = "Updated Version", value=version, inline=True)

                    embed.set_thumbnail(url=arcaea_url_list[pack])

                    await ctx.send(embed=embed)
                    print("Arcaea Random: " + song)
                except:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Random Song: Arcaea", description=err_msg['unknown'])
                    await ctx.send(embed=embed)
                    print("Arcaea Random: Error")

            elif args[0].lower() == "cytus2":
                i = randint(1, len(cytus2_df.index))
                df_temp = pd.DataFrame()
                df_temp = cytus2_df.iloc[i-1]

                try:
                    song = df_temp['song']
                    artist = df_temp['artist']
                    easy = str(df_temp['easy'])
                    hard = str(df_temp['hard'])
                    chaos = str(df_temp['chaos'])
                    diff = easy + " / " + hard + " / " + chaos
                    try:
                        length_temp = int(df_temp['len'])
                        length = "{0}:{1:02d}".format(length_temp // 60, length_temp % 60)
                    except ValueError:
                        length = "NaN"
                    bpm = str(df_temp['bpm'])
                    character = df_temp['character']

                    embed = discord.Embed(colour = discord.Colour.blue(), title="Random Song: Cytus2")
                    embed.add_field(name = "Song", value=song, inline=False)
                    embed.add_field(name = "Artist", value=artist, inline=False)
                    embed.add_field(name = "Difficulty", value=diff, inline=True)
                    embed.add_field(name = "Length", value=length, inline=True)
                    embed.add_field(name = "BPM", value=bpm, inline=True)
                    embed.add_field(name = "Character", value=character, inline=True)

                    embed.set_thumbnail(url=cytus2_url_list[character])

                    await ctx.send(embed=embed)
                    print("Cytus2 Random: " + song)
                except:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Random Song: Cytus2", description=err_msg['unknown'])
                    await ctx.send(embed=embed)
                    print("Cytus2 Random: Error")

            else:
                embed = discord.Embed(colour = discord.Colour.red(), title="Random Song", description=err_msg['usage_random'])
                await ctx.send(embed=embed)
                print("Random Song: Unknown Argument")
        elif len(args) == 2:
            if args[0].lower() == "arcaea":
                try:
                    df_temp = pd.DataFrame()
                    df_temp = arcaea_df.loc[(arcaea_df['pst'].isin([args[1]])) | (arcaea_df['prs'].isin([args[1]])) | (arcaea_df['ftr'].isin([args[1]]))]

                    i = randint(1, len(df_temp.index))
                    df_temp = df_temp.iloc[i-1]

                    song = df_temp['song']
                    artist = df_temp['artist']
                    pst = str(df_temp['pst'])
                    prs = str(df_temp['prs'])
                    ftr = str(df_temp['ftr'])
                    diff = pst + " / " + prs + " / " + ftr
                    length = str(df_temp['len'])
                    bpm = str(df_temp['bpm'])
                    pack = df_temp['pack']
                    version = str(df_temp['update'])

                    embed = discord.Embed(colour = discord.Colour.purple(), title="Random Song: Arcaea")
                    embed.add_field(name = "Song", value=song, inline=False)
                    embed.add_field(name = "Artist", value=artist, inline=False)
                    embed.add_field(name = "Difficulty", value=diff, inline=True)
                    embed.add_field(name = "Length", value=length, inline=True)
                    embed.add_field(name = "BPM", value=bpm, inline=True)
                    embed.add_field(name = "Pack", value=pack, inline=True)
                    embed.add_field(name = "Updated Version", value=version, inline=True)

                    embed.set_thumbnail(url=arcaea_url_list[pack])

                    await ctx.send(embed=embed)
                    print("Arcaea Random: " + song)
                except ValueError:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Random Song: Arcaea", description=err_msg['value_error'])
                    await ctx.send(embed=embed)
                    print("Arcaea Random: ValueError")

            elif args[0].lower() == "cytus2":
                try:
                    df_temp = pd.DataFrame()
                    df_temp = cytus2_df.loc[(cytus2_df['easy'].isin([args[1]])) | (cytus2_df['hard'].isin([args[1]])) | (cytus2_df['chaos'].isin([args[1]]))]

                    i = randint(1, len(df_temp.index))
                    df_temp = df_temp.iloc[i-1]

                    song = df_temp['song']
                    artist = df_temp['artist']
                    easy = str(df_temp['easy'])
                    hard = str(df_temp['hard'])
                    chaos = str(df_temp['chaos'])
                    diff = easy + " / " + hard + " / " + chaos
                    try:
                        length_temp = int(df_temp['len'])
                        length = "{0}:{1:02d}".format(length_temp // 60, length_temp % 60)
                    except ValueError:
                        length = "NaN"
                    bpm = str(df_temp['bpm'])
                    character = df_temp['character']

                    embed = discord.Embed(colour = discord.Colour.blue(), title="Random Song: Cytus2")
                    embed.add_field(name = "Song", value=song, inline=False)
                    embed.add_field(name = "Artist", value=artist, inline=False)
                    embed.add_field(name = "Difficulty", value=diff, inline=True)
                    embed.add_field(name = "Length", value=length, inline=True)
                    embed.add_field(name = "BPM", value=bpm, inline=True)
                    embed.add_field(name = "Character", value=character, inline=True)

                    embed.set_thumbnail(url=cytus2_url_list[character])

                    await ctx.send(embed=embed)
                    print("Cytus2 Random: " + song)
                except ValueError:
                    embed = discord.Embed(colour = discord.Colour.red(), title="Random Song: Cytus2", description=err_msg['value_error'])
                    await ctx.send(embed=embed)
                    print("Cytus2 Random: ValueError")

            else:
                embed = discord.Embed(colour = discord.Colour.red(), title="Random Song", description=err_msg['usage_random'])
                await ctx.send(embed=embed)
                print("Random Song: Unknown Argument")
        else:
            embed = discord.Embed(colour = discord.Colour.red(), title="Random Song", description=err_msg['usage_random'])
            await ctx.send(embed=embed)
            print("Random Song: Argument Error")
    else:
        embed = discord.Embed(colour = discord.Colour.red(), title="Random Song", description=err_msg['usage_random'])
        await ctx.send(embed=embed)
        print("Random Song: Argument Error")

@client.command(pass_context=True)
async def songlist(ctx, *args):
    if len(args) == 2:
        if args[0].lower() == "arcaea":
            try:
                startLoc = int(args[1]) * 10 - 9
                endLoc = int(args[1]) * 10 + 1
                if endLoc > len(arcaea_df.index):
                    endLoc = len(arcaea_df.index)
                elif startLoc >= len(arcaea_df.index):
                    raise IndexError

                df_temp = pd.DataFrame()
                df_temp = arcaea_df.iloc[startLoc:endLoc]

                arr = []
                for i, j in zip(range(0, endLoc-startLoc), range(startLoc, endLoc)):
                    arr.append(str(j) + ". " + df_temp.iloc[i, 1])
                    output = "\n".join(arr)
                    output_text = "```css\n[Arcaea Song List (" + str(startLoc) + "-" + str(endLoc-1) + ")]\n\n" + output + "\n```"

                await ctx.author.send(output_text)
                print("Arcaea Song List: " + args[1])
            except:
                embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Song List", description=err_msg['out_of_index'])
                await ctx.send(embed=embed)
                print("Arcaea Song List: Out of index")

        elif args[0].lower() == "cytus2":
            try:
                startLoc = int(args[1]) * 10 - 9
                endLoc = int(args[1]) * 10 + 1
                if endLoc > len(cytus2_df.index):
                    endLoc = len(cytus2_df.index)
                elif startLoc >= len(cytus2_df.index):
                    raise IndexError

                df_temp = pd.DataFrame()
                df_temp = cytus2_df.iloc[startLoc:endLoc]

                arr = []
                for i, j in zip(range(0, endLoc-startLoc), range(startLoc, endLoc)):
                    arr.append(str(j) + ". " + df_temp.iloc[i, 1])
                    output = "\n".join(arr)
                    output_text = "```css\n[Cytus2 Song List (" + str(startLoc) + "-" + str(endLoc-1) + ")]\n\n" + output + "\n```"

                await ctx.author.send(output_text)
                print("Cytus2 Song List: " + args[1])
            except:
                embed = discord.Embed(colour = discord.Colour.red(), title="Cytus2 Song List", description=err_msg['out_of_index'])
                await ctx.send(embed=embed)
                print("Arcaea Song List: Out of index")

        else:
            embed = discord.Embed(colour = discord.Colour.red(), title="Song List", description=err_msg['usage_songlist'])
            await ctx.send(embed=embed)
            print("Song List: Unknown Argument")
    else:
        embed = discord.Embed(colour = discord.Colour.red(), title="Song List", description=err_msg['usage_songlist'])
        await ctx.send(embed=embed)
        print("Song List: Argument Error")

client.run(token)
