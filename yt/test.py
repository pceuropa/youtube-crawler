from scrapy.utils.project import get_project_settings as settings
from yt.models.movie import Movie


def test_settings():
    assert isinstance(settings().get("CONNECTION_STRING"), str)


class TestModelVideo(object):
    movie = Movie()

    def test_find_id(self):
        row = self.movie.find(1)
        assert row[0] == 1

    def test_find_last_id(self):
        assert isinstance(self.movie.find_last_id(), str)

    def test_find_all_id(self):
        assert isinstance(self.movie.ids(), set)
