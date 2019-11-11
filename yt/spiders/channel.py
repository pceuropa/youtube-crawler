# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from yt.models.movie import Movie


class YoutubeSpider(Spider):
    name = 'channel'
    allowed_domains = ['youtube.com']
    youtube: str = 'https://www.youtube.com/'
    all_channel_ids = Movie().channel_ids()
    blacklist_word = {'bajka', 'bajki', 'po', 'odcinki', 'odcinków', 'dzieci', 'całe', 'dla', 'kompilacja', 'polski', 'polska', 'polsku'}

    def start_requests(self):
        for channel_id in self.all_channel_ids:
            url = f"{self.youtube}/channel/{channel_id}"
            yield Request(url)

    def parse(self, r):
        channel_id = r.url.split('/')[-1]
        yield {
            'channel_id': channel_id,
            'title': self.optymize_text(r.xpath("//meta[@name='title']/@content").get('')),
            'description': self.optymize_text(r.xpath("//meta[@name='description']/@content").get('')),
            'tag': self.optymize_tag(r.xpath("//meta[@name='keywords']/@content").get(''))
        }

    def optymize_text(self, text):
        return ''.join(c for c in text if c.isalnum() or c.isspace() or c == ',' or c == '.').replace('YouTube', '').replace('  ', ' ').strip()

    def optymize_tag(self, text):
        text = self.optymize_text(text)
        text = set(text.split(' '))
        return ' '.join(text - self.blacklist_word)
