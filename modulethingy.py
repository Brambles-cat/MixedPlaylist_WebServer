def video_data(thumbnail: str, index: int, title: str, url: str):
    return {
        'thumbnail': thumbnail,
        'index': index,
        'title': title,
        'source': url.split('/')[2],
        'url': url
    }