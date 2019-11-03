from scrapy.commands import ScrapyCommand
from yt.models.movie import Movie
from langdetect import detect
from textblob import TextBlob


class DetectLanguageCommand(ScrapyCommand):

    def run(self, args, opts):
        """
        Entry point for running commands
        """
        model = Movie()
        for v in model.detect_language():
            self.detect_language(v[1])
            self.detect_language(v[2])

    def detect_language(self, string: str = ''):
        try:
            textB = TextBlob(string).detect_language()
            print(f'TextBlob: {textB} {string}')
        except Exception as e:
            print(e)

        try:
            det = detect(string)
            print(f'Detect: {det}')
        except Exception as e:
            print(e)
