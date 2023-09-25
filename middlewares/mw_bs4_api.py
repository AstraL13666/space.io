import pprint

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from config_data import data
from utils import setting
from utils.misc import datanews
from .mw_logger import custom_notify
from .mw_translater import translate


class Parser:
    """
    Парсинг новостей с сайта

    Атрибуты:
        __ua -> str : Фейковый юзер-агент для имитации юзера
        __url -> str : Ссылка на сайт, откуда парсим новости
        __url_img -> str : Для генерации ссылок
        __setting -> str : настройки бота, получаем язык бота
    """

    def __init__(self, value):
        self.__ua = UserAgent().random
        self.__url_pars_ = "https://www.astronews.ru/cgi-bin/mng.cgi?page=news&"
        self.__url_pars__img = "https://www.astronews.ru"
        self.__url_nasa = "https://api.nasa.gov/planetary/apod?api_key={Key}"
        self.__setting = value

    @property
    async def __lang(self):
        return self.__setting.language  # язык бота

    @classmethod
    async def __check_encoding(cls, html):
        """
        Получаем энкодинг страницы для адекватного чтения

        :param html: сайт
        :return: str
        """
        soup = BeautifulSoup(html, 'html.parser')
        meta_tag = soup.find('meta', {'http-equiv': 'Content-Type'})
        return meta_tag['content'].split('=')[-1]

    async def __response_query(self, filt: str = None):
        """
        Парсим страницу

        :return: str
        """

        if filt == 'news':
            get_url = f"{self.__url_pars_}str=1"
        else:
            get_url = self.__url_nasa.format(Key=data['nasa_api'])

        req = requests.get(get_url, headers={'User-Agent': self.__ua})

        if filt == 'news':
            req.encoding = await self.__check_encoding(html=req.text)

        return req.text if filt == 'news' else req

    async def __check_news(cls, page):
        """
        Проверяем актуальность страниц

        :param page: str
        :return: None
        """
        title_src = page.find('a', {"class": "name"}).text.strip()

        if datanews.news_ru is None:
            custom_notify(text="CHECK NEWS | Data is different")
            return False

        elif datanews.news_ru[0]["title"] != title_src:
            custom_notify(text="CHECK NEWS | Data is different")
            return False

        else:
            custom_notify(text="CHECK NEWS | Ok")
            return True

    def __filters(self, page):
        """
        Фильтруем полученные данные

        :param page: str
        :return: dict
        """
        title_src = page.find('a', {"class": "name"}).text.strip()
        desc = page.find('p').text.strip().split()
        desc_src = f"{' '.join(desc[:len(desc) - 4])} ..."

        link_src = f"{self.__url_pars_}{page.find('a')['href']}"
        date_src = page.find('div', {'class': 'date'}).text.strip()

        counts = page.find('div', {'class': 'counts'})
        counts_src = [int(img.next_sibling.strip()) for img in counts.find_all('img')]

        img = page.find('img', {'class': 'img_l'})
        img_src = img['src']

        return dict(title=title_src, desc=desc_src, link=link_src, date=date_src,
                    counts=dict(view=counts_src[0], comment=counts_src[1]),
                    image=f"{self.__url_pars__img}{img_src}")

    async def parsing(self):
        """
        Структура парсера, для работы скрипта

        :return: bool
        """
        res = await self.__response_query(filt='news')

        soup = BeautifulSoup(res, 'html.parser')
        news_list = soup.find_all('div', {'class': 'news-page'})

        check_result = await self.__check_news(page=news_list[0])

        if check_result is False:

            ru, en = list(), list()

            for ind in range(3):
                res_ru = self.__filters(page=news_list[ind])
                res_en = translate.get(text=self.__filters(page=news_list[ind]))

                ru.append(res_ru), en.append(res_en)

            datanews.news_ru, datanews.news_en = ru, en
            custom_notify(text="The news download is complete")
            return True
        else:
            return False

    async def api_get(self):
        apod_get = await self.__response_query(filt='apod')
        res = apod_get.json()

        data = {
            'date': res['date'],
            'explanation': res['explanation'],
            'pic': res['url'],
            'title': res['title']
        }

        return data


parser = Parser(value=setting)
