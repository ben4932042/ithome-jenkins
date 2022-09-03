from typing import List
import datetime
import scrapy
from web_poet import ItemWebPage, WebPage
from src.items import IthomeContentInfoItem


class HomePage(WebPage):

    @property
    def get_next_page_url(self) -> list:
        return self.xpath('//ul[@class="pagination"]/li/a/@href').extract()

class ContentPage(ItemWebPage):

    @property
    def content_list(self) -> list:
        return self.xpath('//div[@class="qa-list profile-list ir-profile-list"]')

    def to_item(self) -> List[IthomeContentInfoItem]:
        items_list = []
        for content in self.content_list:
            profile_list = content.xpath('.//div[@class="profile-list__condition"]//span[@class="qa-condition__count"]/text()').extract()
            item = {
                "title": content.xpath('.//a[@class="qa-list__title-link"]/text()').extract_first().strip(),
                "like": profile_list[0],
                "comment":  profile_list[1],
                "view": profile_list[2],
                "url": self.url,
                "create_datetime": datetime.datetime.strptime(content.xpath('.//a[@class="qa-list__info-time"]/@title').extract_first().strip(), '%Y-%m-%d %H:%M:%S')
            }
            items_list.append(IthomeContentInfoItem(**item))

        return items_list

class IthomeSpider(scrapy.Spider):
    name = 'ithome'
    def __init__(self, ironman_man_page: str):
        if not ironman_man_page:
            raise scrapy.exceptions.CloseSpider('Lost input url.')
        self.ironman_man_page = ironman_man_page

    def start_requests(self):
        yield scrapy.Request(
            url=self.ironman_man_page,
            callback=self.parse
        )

    def parse(self, response, homepage: HomePage, content: ContentPage) -> IthomeContentInfoItem:

        page_url_list = homepage.get_next_page_url
        for next_page_url in set(page_url_list):
            yield response.follow(
                url=next_page_url,
                callback=self.parse_content,
            )
        
        for item in content.to_item():
            yield item
        
    def parse_content(self, response, content: ContentPage) -> IthomeContentInfoItem:
        for item in content.to_item():
            yield item

