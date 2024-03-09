class Video:
    def __init__(self, thumbnail: str, index: int, title: str, url: str):
        self.thumbnail = thumbnail
        self.index = index
        self.title = title
        self.source = url.split("/")[2]
        self.url = url