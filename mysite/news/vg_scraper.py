import bs4 as bs
import urllib.request

home = urllib.request.urlopen('http://www.vg.no/').read()
soup = bs.BeautifulSoup(home, 'lxml')
list = []

def article_list(list):
    for article in soup.find_all('div',class_='article-content'):
        link = article.find('a')
        try:
            link = link.get('href')
            if "http" not in link:
                list.append("http://www.vg.no/"+link)
        except:
            pass


if __name__ == '__main__':
    article_list(list)
    print(list)