from scrapy import Spider, Request
from yt.models.video import Video
import urllib.parse as urlparse


class YoutubeSpider(Spider):
    name = 'youtube'
    allowed_domains = ['youtube.com']
    youtube = 'https://www.youtube.com/'
    model = Video()
    start_yt_id: str = model.find_last_id() or "E3HsEPLsJJk"
    black_list_yt_ids: set = model.find_all_yt_id()
    start_urls: list = [f"{youtube}watch?v={start_yt_id}"]

    def __init__(self):
        print(len(self.black_list_yt_ids))

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url)

    def parse_url(self, url, param='v'):
        parsed = urlparse.urlparse(url)
        return urlparse.parse_qs(parsed.query)[param]

    def parse(self, r):
        yt_id = r.xpath("//meta[@itemprop='videoId']/@content").get(self.parse_url(r.url, 'v')[0])
        if yt_id:
            if yt_id not in self.black_list_yt_ids:
                self.black_list_yt_ids.add(yt_id)

                title = r.xpath('//title/text()').get('')
                title = title.encode('ascii', 'ignore').decode('ascii').replace('YouTube', '').replace(' - ', ' ')

                description = r.xpath('//p[@id="eow-description"]/text()').get(default='')
                description = description.encode('ascii', 'ignore').decode('ascii').replace('YouTube', '')

                yield {
                    'title': title,
                    'description': description,
                    'tags': str(r.xpath("//meta[@property='og:video:tag']/@content").getall()),
                    'regions_allowed': r.xpath("//meta[@itemprop='regionsAllowed']/@content").get(),
                    'is_family_frendly': int('True' == r.xpath("//meta[@itemprop='isFamilyFriendly']/@content").get()),
                    'image': r.xpath("//meta[@property='og:image']/@content").get(),
                    'yt_id': yt_id,
                    'width': r.xpath("//meta[@itemprop='width']/@content").get(),
                    'height': r.xpath(f"//meta[@itemprop='height']/@content").get(),
                    'interaction_count': int(r.xpath(f"//meta[@itemprop='interactionCount']/@content").get(0)),
                    'date_published': r.xpath("//meta[@itemprop='datePublished']/@content").get(),
                    'channel': r.xpath("//meta[@itemprop='channelId']/@content").get(),
                    'category': r.xpath("//meta[@itemprop='genre']/@content").get(),
                    # 'content_region': '',
                    # 'ads': '',
                    # 'locate': '',
                    # 'language': '',
                }
        else:
            print('None found yt_id', yt_id)

        for href in r.xpath("//a[contains(@href,'watch?v=')]/@href"):
            yield r.follow(href, callback=self.parse)

    def meta(self, r, name):
        return r.xpath(f"//meta[@itemprop='{name}']/@content").get(),
