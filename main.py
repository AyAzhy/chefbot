from types import new_class
import discord
from discord.ext import commands
from bot_token import token
from class_algila import detect_bird
from datetime import datetime
import os
from embedler import *


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def algila(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"images/{file_name}"
            await attachment.save(file_path)
            model_path = "model/keras_model.h5"
            label_path = "model/labels.txt"
            name, score = detect_bird(file_path, model_path, label_path)
            if name.strip() == "Tavada Pratik Pizza":
                  await ctx.send(embed=pizza_embed)
            if name.strip() == "Tavuklu Kremalı Makarna":
                  await ctx.send(embed=makarna_embed)
            if name.strip() == "Karnabahar Köftesi":
                  await ctx.send(embed=karnabahar)
            if name.strip() == "Fırında Kaşarlı Mantar":
                    await ctx.send(embed=mantar)
            if name.strip() == "Çikolatalı Muzlu Krep":
                    await ctx.send(embed=cukulata)
            if name.strip() == "Peynirli ve Ispanaklı Börek":
                    await ctx.send(embed=borek)
            if name.strip() == "Yoğurtlu Mercimek Köftesi":
                    await ctx.send(embed=mercimek)
            if name.strip() == "Fırında Sebzeli Tavuk":
                    await ctx.send(embed=tavuk)
            if name.strip() == "Çıtır Soğan Halkaları":
                    await ctx.send(embed=soganhalka)
            if name.strip() == "Hamburger":
                    await ctx.send(embed=hamburger)
    else:
        await ctx.send("Komutla Birlikte Resim Gönderin.")

@bot.command()
async def yemekler(ctx):
      await ctx.send(embed=yemekler_embed)

bot.run(token)