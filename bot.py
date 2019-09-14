import asyncio
import discord
from discord.ext import commands
import pandas as pd
import numpy as np
from difflib import SequenceMatcher

df = pd.read_csv("data/arcaea.csv", encoding='utf-8-sig')

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
    embed.add_field(name = "ARCAEA", value="`ramdom`", inline=False)
    embed.add_field(name = "CYTUS 2", value="`random`", inline=False)
    embed.add_field(name = "LANOTA", value="`random`", inline=False)

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def arcaea(ctx, *, message):
    df_temp = pd.DataFrame()

    for list in df.loc[:, 'song']:
        ratio = SequenceMatcher(None, message, list.lower()).ratio()
        if ratio >= 0.7:
            df_temp = df.loc[df['song'] == list]
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

        embed = discord.Embed(colour = discord.Colour.blue(), title="Arcaea Song Info")
        embed.add_field(name = "Song", value=song, inline=False)
        embed.add_field(name = "Artist", value=artist, inline=False)
        embed.add_field(name = "Difficulty", value=diff, inline=True)
        embed.add_field(name = "Length", value=length, inline=True)
        embed.add_field(name = "BPM", value=bpm, inline=True)
        embed.add_field(name = "Pack", value=pack, inline=True)
        embed.add_field(name = "Updated Version", value=version, inline=True)

        await ctx.send(embed=embed)
    except KeyError:
        embed = discord.Embed(colour = discord.Colour.red(), title="Arcaea Song Info", description="No search results found. Please search correct song name.")
        await ctx.send(embed=embed)

client.run(token)
