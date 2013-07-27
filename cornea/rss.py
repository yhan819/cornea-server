from cornea import app
import feedparser
import json

@app.route('/get_chosun')
def get_chosun():
    d = feedparser.parse('http://myhome.chosun.com/rss/www_section_rss.xml')
    articles = parse_items(d)
    return json.dumps({"articles": articles})

def parse_items(d):
    result = []
    for a in d["items"]:
        article = {}
        article["title"] = a["title"]
        article["link"] = a["link"]
        article["date"] = a["date"]
        article["description"] = a["description"]
        result.append(article)
    return result
