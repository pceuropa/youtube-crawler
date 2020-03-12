from scrapy.commands import ScrapyCommand
from yt.models.movie import Movie
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from time import time

es = Elasticsearch()


#  class MigrateCommand(ScrapyCommand):
class MigrateCommand():

    def run(self, args, opts):
        """
        Entry point for running commands
        """
        helpers.bulk(es, self.gendata())

    def gendata(self):
        t = time()
        model = Movie()
        i = 0

        while True:
            chunk_videos = model.get_chunk(i)
            for v in chunk_videos:
                yield {
                    "_index": "i",
                    "_type": "t",
                    "_id": v[0],
                    "_source": dict(v)
                }

            print(len(chunk_videos))

            if len(chunk_videos) < 100:
                break

            i += 100

        print(time() - t)

    def sequentialy(self):
        t = time()
        video = Movie()

        i = 0
        while True:
            chunk_videos = video.get_chunk(i)
            for v in chunk_videos:
                res = es.index(index="test2-index", doc_type='video-test2', id=v[0], body=dict(v))
                print('first res', res)

            print(len(chunk_videos))

            if len(chunk_videos) < 100:
                break
            i += 100

        print(time() - t)
