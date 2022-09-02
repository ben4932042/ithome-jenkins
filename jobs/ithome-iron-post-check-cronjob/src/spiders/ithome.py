import scrapy
import datetime
from ..items import IthomeContentInfoItem


class IthomeSpider(scrapy.Spider):
    name = 'ithome'
    def __init__(self, ironman_man_page: str):
        if not ironman_man_page:
            raise scrapy.exceptions.CloseSpider('Lost input url.')
        self.ironman_man_page = ironman_man_page

    def start_requests(self):
        yield scrapy.Request(
            url=self.ironman_man_page,
            callback=self.parse,
            meta={'stop_contiune': False}
        )

    def parse(self, response):
        content_list = response.xpath('//div[@class="qa-list profile-list ir-profile-list"]')
        for content in content_list:
            item = IthomeContentInfoItem()
            item['title'] = content.xpath('.//a[@class="qa-list__title-link"]/text()').extract_first().strip()
            profile_list = content.xpath('.//div[@class="profile-list__condition"]//span[@class="qa-condition__count"]/text()').extract()
            item['like'] =  profile_list[0]
            item['comment'] = profile_list[1]
            item['view'] = profile_list[2]
            item['create_datetime'] = datetime.datetime.strptime(content.xpath('.//a[@class="qa-list__info-time"]/@title').extract_first().strip(), '%Y-%m-%d %H:%M:%S')

            yield item

        page_url_list = response.xpath('//ul[@class="pagination"]/li/a/@href').extract()
        if not response.meta.get('stop_continue'):
            for next_page_url in set(page_url_list):
                yield scrapy.Request(
                    url=next_page_url,
                    callback=self.parse,
                    meta={'stop_continue': True}
                )
