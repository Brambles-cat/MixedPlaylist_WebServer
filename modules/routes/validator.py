from app import flaskapp
from flask import request, make_response
from votevalidator import check_duplicates, upload_date, data_pulling, duration_check, ballot_check_blacklist
from votevalidator.classes.video_metadata import VideoMetadata
from ..bag_o_nifty_stuff import API_KEY
import json


@flaskapp.route("/validator", methods=['POST', 'GET'])
def validate():
    payload: list = request.get_json()
    
    ballot_urls = [url for url in payload if len(url) != 0]
    ballot: dict[str, VideoMetadata] = data_pulling.get_urls_to_metadata(ballot_urls, API_KEY)
    ineligible_votes = {}


    for url, metadata in ballot.items():
        if metadata is None:
            ineligible_votes[url] = "Couldn't Retrieve Metadata"

    for url in ineligible_votes:
        ballot.pop(url)


    duplicates = check_duplicates(ballot_urls)
    for url, occurences in duplicates.items():
        if not url in ineligible_votes:
            ineligible_votes[url] = f"Duplicate Vote x{occurences}"
    

    checklist: list[function] = [duration_check.check_durations, ballot_check_blacklist, upload_date.check_dates]

    for check in checklist:
        check_fails = check(ballot)

        for url, fail_msg in check_fails.items():
            if url in ineligible_votes:
                ineligible_votes[url] += f"; {fail_msg}"

            else:
                ineligible_votes[url] = fail_msg

    return make_response(json.dumps(ineligible_votes))