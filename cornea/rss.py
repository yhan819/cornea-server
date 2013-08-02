from cornea import app, crossdomain
import feedparser
import json

@app.route('/get_chosun')
@crossdomain(origin='*')
def get_chosun():
    d = feedparser.parse('http://myhome.chosun.com/rss/www_section_rss.xml')
    articles = parse_items(d)
    return json.dumps({"articles": articles})

@app.route('/get_joongang')
@crossdomain(origin='*')
def get_joongang():
    d = feedparser.parse('http://rss.joins.com/joins_homenews_list.xml')
    articles = parse_items(d)
    return json.dumps({"articles": articles})

@app.route('/get_donga')
@crossdomain(origin='*')
def get_donga():
    d = feedparser.parse('http://rss.donga.com/total.xml')
    articles = parse_items(d)
    return json.dumps({"articles": articles})

@app.route('/get_yonhap')
@crossdomain(origin='*')
def get_yonhap():
    d = feedparser.parse('http://www.yonhapnews.co.kr/RSS/province.xml')
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
