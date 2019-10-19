import asyncio
import discord
from discord.ext import commands
import pandas as pd
import numpy as np
from difflib import SequenceMatcher
from tools import randomSong, getDict, getSongList

arcaea_url_list = getDict.arcaea()
cytus2_url_list = getDict.cytus2()
err_msg = getDict.err()

arcaea_df = pd.read_csv("data/arcaea.csv", encoding='utf-8-sig')
cytus2_df = pd.read_csv("data/cytus2.csv", encoding='utf-8-sig')
dynamix_df = pd.read_csv("data/dynamix.csv", encoding='utf-8-sig')

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
    embed.add_field(name = "DYNAMIX", value="`dynamix [search]`: Search for Dynamix song info.", inline=False)
    embed.add_field(name = "RANDOM", value="`random [arcaea/cytus2/dynamix] (level)`: Random Songs! LOL")
    embed.add_field(name = "SONG LIST", value="`songlist [arcaea/cytus2/dynamix] [listnumber]`: Get list of songs.")
    #embed.add_field(name = "LANOTA", value="`random`", inline=False)
    embed.set_footer(text="Bot Made by Xestiny_")

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def arcaea(ctx, *, message):
    df_temp = pd.DataFrame()

    try:
        for list in arcaea_df.loc[:, 'song']:
            ratio = SequenceMatcher(None, message, list.lower()).ratio()
            if ratio >= 0.7:
                df_temp = arcaea_df.loc[arcaea_df['song'] == list]

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
    except:
        embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Arcaea Song Info: No Result")

@client.command(pass_context=True)
async def cytus2(ctx, *, message):
    df_temp = pd.DataFrame()

    try:
        for list in cytus2_df.loc[:, 'song']:
            ratio = SequenceMatcher(None, message, list.lower()).ratio()
            if ratio >= 0.7:
                df_temp = cytus2_df.loc[cytus2_df['song'] == list]

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
    except:
        embed = discord.Embed(colour = discord.Colour.red(), title="Cytus2 Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Cytus2 Song Info: No Result")

@client.command(pass_context=True)
async def dynamix(ctx, *, message):
    df_temp = pd.DataFrame()

    try:
        for list in dynamix_df.loc[:, 'song']:
            ratio = SequenceMatcher(None, message, list.lower()).ratio()
            if ratio >= 0.7:
                df_temp = dynamix_df.loc[dynamix_df['song'] == list]

        song = df_temp['song'].values[0]
        artist = df_temp['artist'].values[0]
        casual = str(df_temp['casual'].values[0])
        normal = str(df_temp['normal'].values[0])
        hard = str(df_temp['hard'].values[0])
        mega = str(df_temp['mega'].values[0])
        giga = str(df_temp['giga'].values[0])
        diff = casual + " / " + normal + " / " + hard + " / " + mega + " / " + giga
        bpm = str(df_temp['bpm'].values[0])

        embed = discord.Embed(colour = discord.Colour.dark_blue(), title="Dynamix Song Info")
        embed.add_field(name = "Song", value=song, inline=False)
        embed.add_field(name = "Artist", value=artist, inline=False)
        embed.add_field(name = "Difficulty", value=diff, inline=True)
        embed.add_field(name = "BPM", value=bpm, inline=True)

        await ctx.send(embed=embed)
        print("Dynamix Song Info: " + song)
    except:
        embed = discord.Embed(colour = discord.Colour.red(), title="Dynamix Song Info", description=err_msg['no_result'])
        await ctx.send(embed=embed)
        print("Dynamix Song Info: No Result")


@client.command(pass_context=True)
async def random(ctx, *args):
    if len(args) != 0:
        try:
            if args[0].lower() == "arcaea":
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
            else:
                embed = discord.Embed(colour = discord.Colour.red(), title="Random Song", description=err_msg['usage_random'])
                await ctx.send(embed=embed)
                print("Random Song: Argument Error")
        except:
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

        else:
            embed = discord.Embed(colour = discord.Colour.red(), title="Song List", description=err_msg['usage_songlist'])
            await ctx.send(embed=embed)
            print("Song List: Unknown Argument")
    else:
        embed = discord.Embed(colour = discord.Colour.red(), title="Song List", description=err_msg['usage_songlist'])
        await ctx.send(embed=embed)
        print("Song List: Argument Error")

client.run(token)
