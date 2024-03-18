import requests
from fastapi import APIRouter
import re
import html
import json


tags_metadata = ["Misc"]
news= APIRouter(tags=tags_metadata)
        
@news.get("/news")
async def get_news(category: str = "all", page: int = 1):

    if category == "all":
        url = "https://inshorts.com/api/en/news?category=all_news&max_limit=10&include_card_data=true"
    else:
        url = f"https://inshorts.com/api/en/search/trending_topics/{category}?page=/{page}"
    headers={
        "referer":"https://inshorts.com/en/read",
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 Edg/120.0.0.0"
    }
    res=requests.get(url,headers=headers)
    news_data = res.json()
    news_out = []
    
    if category == "all":
        news_list = news_data['data']['news_list']
    else:
        news_list = news_data['data']['suggested_news']
    for news in news_list:
        title = news['news_obj']['title']
        image = news['news_obj']['image_url']
        source = news['news_obj']['source_name']
        full_article = news['news_obj']['source_url']
        tags = news['news_obj']['relevancy_tags']
        time= news ['news_obj']['created_at']

        mapping = {
            "title": title,
            "image": image,
            "source": source,
            "tags": tags,
            "time": time,
            "full_article": full_article
        }
        news_out.append(mapping)
        
        
    return news_out