from scrapy import Spider


class OlgaSpider(Spider):
    name = 'www'
    start_urls: list = ['https://en.wikipedia.org/wiki/AltaVista']

    def parse(self, r):

        title = r.xpath('//title/text()').get('')
        title = title.encode('ascii', 'ignore').decode('ascii').replace('YouTube', '').replace(' - ', ' ')

        yield {
            'title': title,
        }

        for href in r.xpath("//a/@href"):
            yield r.follow(href, callback=self.parse)

    def meta(self, r, name):
        return r.xpath(f"//meta[@itemprop='{name}']/@content").get(),
