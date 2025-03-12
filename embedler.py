from types import new_class
import discord
from discord.ext import commands
from bot_token import token
from class_algila import detect_bird
from datetime import datetime
import os

pizza_embed = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

pizza_embed.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

pizza_embed.add_field(name="Malzemeler",
                value="2 dilim lavaş\n1 çay bardağı domates sosu\n1 su bardağı rendelenmiş kaşar\nSucuk, mısır, zeytin (isteğe bağlı)",
                inline=True)
pizza_embed.add_field(name="Yapılış",
                value="Lavaşı tavaya koyup üzerine domates sosu sürün.\nMalzemeleri ekleyin ve kaşarı serpin.\nKapağını kapatıp kısık ateşte 5-7 dakika pişirin.\nDilimleyip sıcak servis edin.",
                inline=False)

pizza_embed.set_footer(text="Made By AyAzhy")

makarna_embed = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

makarna_embed.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

makarna_embed.add_field(name="Malzemeler",
                value="250 gr makarna\n1 adet tavuk göğsü (küçük doğranmış)\n1 su bardağı krema\n1 yemek kaşığı tereyağı\n2 diş sarımsak (ince doğranmış)\nTuz, karabiber, pul biber\nYarım su bardağı rendelenmiş kaşar",
                inline=True)
makarna_embed.add_field(name="Yapılış",
                value="Makarnayı haşlayıp süzün.\nTavukları tereyağında kavurun, sarımsağı ekleyin.\nKrema, tuz, karabiber ve pul biber ekleyip 5 dakika pişirin.\nMakarnayı ekleyip karıştırın, kaşar serpip servis yapın.",
                inline=False)

makarna_embed.set_footer(text="Made By AyAzhy")

karnabahar = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

karnabahar.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

karnabahar.add_field(name="Malzemeler",
                value="1 küçük karnabahar\n1 adet yumurta\n3 yemek kaşığı galeta unu\n1 çay kaşığı tuz, karabiber, kimyon\n1 çay bardağı rendelenmiş kaşar\nSıvı yağ (kızartmak için)",
                inline=True)
karnabahar.add_field(name="Yapılış",
                value="Karnabaharı haşlayıp ezin.\nİçine yumurta, galeta unu, baharatlar ve kaşarı ekleyip yoğurun.\nKüçük köfteler yapıp kızgın yağda kızartın.\nYoğurtla servis yapın.",
                inline=False)

karnabahar.set_footer(text="Made By AyAzhy")

mantar = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

mantar.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

mantar.add_field(name="Malzemeler",
                value="10 adet büyük mantar\n1 su bardağı rendelenmiş kaşar\n1 yemek kaşığı tereyağı\nTuz, karabiber",
                inline=True)
mantar.add_field(name="Yapılış",
                value="Mantarları temizleyip saplarını çıkarın.\nİçlerine biraz tereyağı ve tuz ekleyin.\nÜzerine rendelenmiş kaşar koyup 180°C’de 15 dakika fırınlayın.\nSıcak servis yapın.",
                inline=False)

mantar.set_footer(text="Made By AyAzhy")

cukulata = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

cukulata.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

cukulata.add_field(name="Malzemeler",
                value="1 su bardağı süt\n1 su bardağı un\n1 adet yumurta\n1 yemek kaşığı şeker\n1 tatlı kaşığı kakao\n1 adet muz\nÇikolata kreması",
                inline=True)
cukulata.add_field(name="Yapılış",
                value="Süt, un, yumurta, şeker ve kakaoyu çırpın.\nTavada ince krep yapıp iki tarafını da pişirin.\nİçine çikolata sürüp muz ekleyin.\nRulo yapıp dilimleyerek servis edin.",
                inline=False)

cukulata.set_footer(text="Made By AyAzhy")

borek = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

borek.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

borek.add_field(name="Malzemeler",
                value="3 adet yufka\n1 su bardağı beyaz peynir\n1 su bardağı doğranmış ıspanak\n1 adet yumurta\n1 çay bardağı süt\nYarım çay bardağı sıvı yağ",
                inline=True)
borek.add_field(name="Yapılış",
                value="Ispanağı ince doğrayın ve beyaz peynirle karıştırın.\nYumurtayı, sütü ve yağı çırpın.\nYufkayı serip sos sürün, iç harcı ekleyip rulo yapın.\nÜzerine yumurta sarısı sürüp 180°C’de 30 dakika pişirin.",
                inline=False)

borek.set_footer(text="Made By AyAzhy")

mercimek = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

mercimek.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

mercimek.add_field(name="Malzemeler",
                value="1 su bardağı kırmızı mercimek\n1 su bardağı ince bulgur\n1 adet soğan\n1 yemek kaşığı salça\nTuz, kimyon, pul biber\nYoğurt ve sarımsak (sosu için)",
                inline=True)
mercimek.add_field(name="Yapılış",
                value="Mercimeği haşlayıp bulgurla karıştırın, demlenmeye bırakın.\nSoğanı kavurup salçayı ekleyin, mercimekle karıştırın.\nBaharatları ekleyip yoğurun ve küçük köfteler yapın.\nÜzerine sarımsaklı yoğurt dökerek servis yapın.",
                inline=False)

mercimek.set_footer(text="Made By AyAzhy")

tavuk = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

tavuk.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

tavuk.add_field(name="Malzemeler",
                value="2 adet tavuk budu\n1 adet patates\n1 adet havuç\n1 adet soğan\n1 çay bardağı zeytinyağı\nTuz, karabiber, kekik, pul biber",
                inline=True)
tavuk.add_field(name="Yapılış",
                value="Sebzeleri doğrayıp fırın kabına alın.\nTavukları ekleyip baharatları serpin.\nZeytinyağını gezdirip 200°C’de 40 dakika pişirin.",
                inline=False)

tavuk.set_footer(text="Made By AyAzhy")

soganhalka = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

soganhalka.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

soganhalka.add_field(name="Malzemeler",
                value="2 adet soğan\n1 su bardağı un\n1 su bardağı süt\n1 yumurta\n1 çay kaşığı tuz, karabiber\nGaleta unu\nKızartmak için sıvı yağ",
                inline=True)
soganhalka.add_field(name="Yapılış",
                value="Soğanları halka şeklinde doğrayın.\nUn, süt, yumurta ve baharatları çırpın.\nSoğanları önce karışıma sonra galeta ununa bulayın.\nKızgın yağda altın rengi olana kadar kızartın.",
                inline=False)

soganhalka.set_footer(text="Made By AyAzhy")

hamburger = discord.Embed(colour=0x00b0f4,
                      timestamp=datetime.now())

hamburger.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

hamburger.add_field(name="Köfte İçin",
                value="400 gr dana kıyma\n1 diş sarımsak (rendelenmiş)\n1 çay kaşığı tuz\n1 çay kaşığı karabiber\n1 çay kaşığı kimyon\n1 yemek kaşığı zeytinyağı",
                inline=True)
hamburger.add_field(name="Diğer Malzemeler:",
                value="4 adet hamburger ekmeği\n4 dilim cheddar peyniri\n1 adet domates (dilimlenmiş)\n4 yaprak marul\n1 adet soğan (halka doğranmış)\n4 yemek kaşığı mayonez\n2 yemek kaşığı ketçap\n2 yemek kaşığı hardal",
                inline=False)
hamburger.add_field(name="Yapılış",
                value="Köfteyi hazırlayın: Kıyma, sarımsak, tuz, karabiber, kimyon ve zeytinyağını bir kaba alıp güzelce yoğurun.\nKarışımdan 4 eşit parça alıp yuvarlak hamburger köftesi şekli verin.\nKöfteleri pişirin: Tavayı orta ateşte ısıtın ve az yağ ekleyin. Köfteleri 3-4 dakika önlü arkalı pişirin.\nKöfteler pişerken üzerlerine cheddar peyniri koyup erimesini bekleyin.\nEkmekleri ısıtın: Hamburger ekmeklerini tavada hafifçe kızartın.\nHamburgeri hazırlayın:\nEkmeklerin alt kısmına mayonez sürün.\nÜzerine marul, köfte, domates ve soğan ekleyin.\nKetçap ve hardal ekleyip üst ekmeği kapatın.\nSıcak servis yapın! 🍔😋",
                inline=False)

hamburger.set_footer(text="Made By AyAzhy")

yemekler_embed = discord.Embed(timestamp=datetime.now())

yemekler_embed.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

yemekler_embed.add_field(name="Yemeklerin Listesi",
                value="1 Tavuklu Kremalı Makarna\n2 Karnabahar Köftesi\n3 Fırında Kaşarlı Mantar\n4 Tavada Pratik Pizza\n5 Çikolatalı Muzlu Krep\n6 Peynirli ve Ispanaklı Börek\n7 Yoğurtlu Mercimek Köftesi\n8 Fırında Sebzeli Tavuk\n9 Çıtır Soğan Halkaları\n10 Hamburger",
                inline=True)
yemekler_embed.add_field(name="--------------------------------",
                value="",
                inline=False)
yemekler_embed.add_field(name="Tarifler İçin",
                value="!tarif yemeğin_adı",
                inline=False)

yemekler_embed.set_footer(text="Made By AyAzhy")

yardim = discord.Embed(timestamp=datetime.now())

yardim.set_author(name="Chef",
                 icon_url="https://i.ibb.co/qFsSVyxP/chef-logo-design-vector.jpg")

yardim.add_field(name="Komutlar",
                value=".yardım\n.algıla\n.yemekler",
                inline=False)

yardim.set_footer(text="Made By AyAzhy")
