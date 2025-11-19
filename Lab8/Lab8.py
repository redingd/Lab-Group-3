# McKinley did function 1, David did
import requests
import pandas as pd
def func_1():
    list_websites = ["youtube.com", "facebook.com", "google.com", "instagram.com", "chatgpt.com", "x.com", "reddit.com",
                 "whatsapp.com", "wikipedia.org", "bing.com", "tiktok.com", "yahoo.com", "amazon.com", "baidu.com",
                 "linkedin.com", "naver.com", "office.com", "netflix.com", "temu.com", "live.com", "pinterest.com",
                 "microsoft.com", "twitch.tv", "sharepoint.com", "canva.com", "samsung.com", "weather.com",
                 "fandom.com", "duckduckgo.com", "nytimes.com", "zoom.com", "roblox.com", "ebay.com", "apnews.com",
                 "cnn.com", "nbcnews.com", "reuters.com", "news.google.com", "usatoday.com", "cbsnews.com",
                 "washingtonpost.com", "wsj.com", "time.com", "allrecipes.com", "pinchofyum.com", "food.com",
                 "epicurious.com", "simplyrecipes.com", "smittenkitchen.com", "foodnetwork.com", "espn.com",
                 "bleacherreport.com", "si.com", "foxsports.com", "sports.yahoo.com", "sbnation.com", "cbssports.com",
                 "nbcsports.com", "bookoutlet.com", "goodreads.com", "betterworldbooks.com", "getepic.com",
                 "openlibrary.org", "bookshop.org", "abebooks.com", "scholastic.com", "gutenberg.org", "asos.com",
                 "us.boohoo.com", "macys.com", "urbanoutfitters.com", "revolve.com", "theory.com", "uniqlo.com",
                 "francescas.com", "overstock.com", "westelm.com", "cityfurniture.com", "cb2.com",
                 "ashleyfurniture.com", "ikea.com", "levinfurniture.com", "hermanmiller.com", "centuryfurniture.com",
                 "aviationweek.com", "faa.gov", "avweb.com", "simpleflying.com", "txtav.com", "aopa.org",
                 "flyingmag.com", "geaerospace.com", "airlines.org", "bytron.aero", "purefishing.com",
                 "discounttackle.com", "kastking.com", "fishusa.com", "shopkarls.com", "takemefishing.org",
                 "tackledirect.com", "strikeking.com", "lurenet.com"]
    big_list = []
    for website in list_websites:
        # using the internet archive's wayback machine's api that says if a website has been archived, and if it has it
        # gives a timestamp and url to look at it on the wayback machine, as a json object - this doesn't require
        # authentication to use
        # more information about their apis can be found here: https://archive.org/help/wayback_api.php

        # making a list out of those json objects
        url = f"http://archive.org/wayback/available?url={website}"
        data = requests.get(url).json()
        big_list.append(data)

        # using pandas to flatten the json objects and build a csv file
        website_pd = pd.json_normalize(big_list)
        website_pd.to_csv("./Lab8_group3_function1.csv")
func_1()
