from scrapy import Spider, Request
import urllib.parse as urlparse


class YoutubeSpider(Spider):
    name = 'youtube'
    allowed_domains = ['youtube.com']
    youtube: str = 'https://www.youtube.com/'
    start_yt_id: str = "EplXWaTek5o"
    start_urls = [f"{youtube}watch?v={start_yt_id}"]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url)

    def parse_url(self, url, param='v'):
        parsed = urlparse.urlparse(url)
        return urlparse.parse_qs(parsed.query)[param]

    def parse(self, r):
        yt_id = r.xpath("//meta[@itemprop='videoId']/@content").get(self.parse_url(r.url, 'v')[0])
        if yt_id:
            tags = r.xpath("//meta[@property='og:video:tag']/@content").getall()
            tags = ','.join(set(x.lower() for x in tags))
            tags = self.optymize_text(tags)

            duration = r.xpath("//meta[@itemprop='duration']/@content").get('PT0M0S')
            duration_minutes, duration_sec = duration[2:-1].split('M')
            duration = int(duration_minutes) * 60 + int(duration_sec)

            yield {
                'title': self.optymize_text(r.xpath('//title/text()').get('')),
                'description': self.optymize_text(r.xpath('//p[@id="eow-description"]/text()').get('')),
                'tags': tags,
                'regions_allowed': r.xpath("//meta[@itemprop='regionsAllowed']/@content").get(),
                'is_family_frendly': int('True' == r.xpath("//meta[@itemprop='isFamilyFriendly']/@content").get(0)),
                'yt_id': yt_id,
                'width': r.xpath("//meta[@itemprop='width']/@content").get(),
                'height': r.xpath(f"//meta[@itemprop='height']/@content").get(),
                'interaction_count': int(r.xpath(f"//meta[@itemprop='interactionCount']/@content").get(0)),
                'date_published': r.xpath("//meta[@itemprop='datePublished']/@content").get(),
                'duration': duration,
                'channel': r.xpath("//meta[@itemprop='channelId']/@content").get(),
                'category': r.xpath("//meta[@itemprop='genre']/@content").get('None')
            }
        else:
            print('None found yt_id', yt_id)

        for href in r.xpath("//a[contains(@href,'watch?v=')]/@href"):
            yield r.follow(href, callback=self.parse)

    def optymize_text(self, text):
        return ''.join(c for c in text if c.isalnum() or c.isspace() or c == ',' or c == '.').replace('YouTube', '').replace('  ', ' ').strip()
