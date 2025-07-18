import requests
from bs4 import BeautifulSoup as Bs


url = 'https://govzalla.com/ламазан-хенаш-время-молитв'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36'
}

namaz = {}


def nama_time():
    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        soup = Bs(response.content, 'html.parser')
        div = soup.find_all('div', class_="col-6 col-md-4 col-lg-3 col-xl-2")

        for tm in div:
            t_m = tm.find('h4')
            desc = tm.find('div', class_="desc").text
            label = tm.find('div', class_="label").text

            if t_m:
                time_molitv = t_m.text.strip()
                desc_molitv = desc.strip()
                label_molitv = label.strip()
                namaz[label_molitv] = time_molitv, desc_molitv
        return namaz

    except Exception as e:
        print(f'ошибка сети {e}, повторите позже!')
        return None
