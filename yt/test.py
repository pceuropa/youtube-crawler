from scrapy.utils.project import get_project_settings as settings
from yt.models.video import Video


def test_settings():
    assert isinstance(settings().get("CONNECTION_STRING"), str)


class TestModelVideo(object):
    video = Video()

    def test_find_id(self):
        row = self.video.find(1)
        assert row[0] == 1

    def test_find_last_id(self):
        assert isinstance(self.video.find_last_id(), str)

    def test_find_all_id(self):
        assert isinstance(self.video.find_all_yt_id(), set)
