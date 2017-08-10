import bs4 as bs
import urllib.request
#MADE BY RANJITH

home = urllib.request.urlopen('http://www.vg.no/').read()
soup = bs.BeautifulSoup(home, 'lxml')
list = []

def article_list(list):
    for article in soup.find_all('div',class_='article-content'):
        link = article.find('a')
        try:
            link = link.get('href')
            if "http" not in link:
                if 'nyheter/' in link:
                    list.append("http://www.vg.no"+link)
        except:
            pass

def article_read(article):
    site = urllib.request.urlopen(article).read()
    soup = bs.BeautifulSoup(site, 'lxml')

    def article_title():
        header = soup.find('div', class_='reg-grid-full')
        title = header.find('h1', class_='main-title')
        title = title.text.strip()
        image = header.find('img').get('src')
    article_title()

if __name__ == '__main__':
    article_list(list)
    #print('\n'.join(list))

