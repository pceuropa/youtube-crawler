from scrapy.commands import ScrapyCommand
from elasticsearch import Elasticsearch
from yt.models.shema import Video

es = Elasticsearch()


class MigrateCommand(ScrapyCommand):

    def run(self, args, opts):
        """
        Entry point for running commands
        """
        print('elo')
        video = Video()

        for v in video.find_all():
            print(v)

        res = es.index(index="test2-index", doc_type='video-test2', id=2, body={
            'author': 'kimchy',
            'text': 'Elasticsearch: cool. bonsai cool.',
        })

        print('first res', res['result'])
