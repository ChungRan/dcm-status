import requests
from bs4 import BeautifulSoup


def crawlingTest():
    # HTTP GET Request
    headers = [
        {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    ]

    url = 'https://gall.dcinside.com/m/'
    htmlText = requests.get(url, headers=headers[0]).text
    soup = BeautifulSoup(htmlText, 'html.parser')
    selects = soup.select('div.pop_content.pop_hot_mgall > ul')
    # selects.append(soup.select('div.pop_content.pop_hot_mgall ul#heung_list_ul'))
    # selects.append(soup.select('div.pop_content.pop_hot_mgall ul#heung_list_ul_2'))
    # selectList.append(soup.select('div.pop_content.pop_hot_mgall ul#heung_list_ul_3'))

    
    # for select in selects:
    #     print(select.get('href')

    gallList = [dict() for _ in range(300)]
    for select in selects:
        for element in select.find_all('a'):
            gallList[int(element.text.split()[0].rstrip('.')) - 1] = {
                'rank' : int(element.text.split()[0].rstrip('.')),
                'name' : ' '.join(element.text.split()[1:]),
                'url' : 'https://gall.dcinside.com' + element.get('href'),
            }
    text = ''
    for gall in gallList:
        text += str(gall['rank']) + ' ' + gall['name'] + ' ' + gall['url'] + ' <br>\n'
        
    print(text)
    return text
