import bs4 as bs
import urllib.request
#MADE BY RANJITH

home = urllib.request.urlopen('http://www.vg.no/').read()
soup = bs.BeautifulSoup(home, 'lxml')
list = []
main_li = []

def scraper():
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
            try:
                image = header.find('img').get('src')
            except:
                image = 'https://ichef.bbci.co.uk/news/660/cpsprodpb/37B5/production/_89716241_thinkstockphotos-523060154.jpg'

            try:
                image_text = str(header.find('img').get('alt')).replace('<p>','').replace('</p>','')
            except:
                image_text = "ingen bilder"
            return [image, image_text, title]

        def article_main(list):
            main = soup.find('div', class_="article-body-text")
            para = main.find_all('p')
            for i in para:
                i = str(i).replace('<p>','').replace('</p>','')
                if '<' not in i:
                    main_li.append('<p>'+i+'</p><br>')
            ingress = main.find('div', id ='preamble')
            ingress = str(ingress).replace('</div>', '')
            ingress = ingress.split('>')
            innled = ''
            for i in ingress:
                if '<' not in i:
                    innled = i
            kjede = ''
            for i in main_li:
                kjede = kjede + str(i)
            list.append(innled)
            list.append(kjede)

        top = article_title()
        article_main(top)
        return top

    article_list(list)
    out = []
    for ob in list:
        out.append(article_read(ob))
    #for i in reversed(out):
     #   print(i)
    return out

if __name__ == '__main__':
    out = scraper()