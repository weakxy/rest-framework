from rest_framework.parsers import BaseParser, JSONParser, FormParser


class MyBaseParser(BaseParser):
    def parse(self, stream, media_type=None, parser_context=None):
        pass

