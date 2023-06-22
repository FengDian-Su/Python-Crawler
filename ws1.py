import urllib
from urllib import *
import ssl
from bs4 import BeautifulSoup

url = "https://ithelp.ithome.com.tw/articles/10271319?sc=iThelpR"
#url = "https://www.nchu.edu.tw/index1.php"
req = request.Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
response = request.urlopen(req)
html = response.read().decode("utf-8")
ssl._create_default_https_context = ssl._create_unverified_context
#html = request.urlopen(url).read()
soup = BeautifulSoup(html, "html5lib")
find_title = soup.find_all("h2", class_= "qa-header__title ir-article__title")
for f_title in find_title:
    print(f_title.string.strip())
find_author = soup.find_all("a", class_= "ir-article-info__name")
for f_author in find_author:
    print(f_author.string.strip())
find_text = soup.find("div", class_= "markdown__style")
find_p = find_text.find_all("p")
for p in find_p:
    print(p.text)
#print(soup)
#find_text = soup.find_all("div", class_="span")
#find_text = soup.find_all("li", target = "_blank")
#print(find_text)
#find_text = soup.find_all("div", class_="comm-news3")
#for ft in find_text:
#    print(ft)
#fa = soup.find("a", title = "系所評鑑專區(另開新視窗)")
#print(fa)
#print(find_h5)
