from votevalidator.classes.video_metadata import VideoMetadata
from votevalidator import upload_date, duration_check, check_blacklist, data_pulling
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv('apikey')

data_pulling.init_yt_service(API_KEY)

def get_video_issues(video_data: VideoMetadata) -> str | None:
    checks_failed: list[str] = []
    checks = [upload_date.check_date, duration_check.check_duration, check_blacklist]
    
    for check in checks:
        result = check(video_data)

        if result is not None:
            checks_failed.append(result)

    return "- " + "- ".join(checks_failed) if len(checks_failed) != 0 else None


def p_video_data(thumbnail: str, index: int, title: str, url: str, issues: str):
    return {
        'thumbnail': thumbnail,
        'index': index,
        'title': title,
        'source': url.split('/')[2],
        'url': url,
        'issues': issues
    }