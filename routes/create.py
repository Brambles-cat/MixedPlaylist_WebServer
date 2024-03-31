from app import flaskapp, usingRPi, render_create
from flask import request, make_response, session
import uuid
from yt_dlp import YoutubeDL
from modulethingy import *
import db
import json
import validators

ydl_opts = {
    "quiet": True,
}

@flaskapp.route("/create", methods=['POST', 'GET'])
def create():
	if request.method != 'POST':
		if request.cookies.get("uid") is None:
			resp = make_response(render_create())
			resp.set_cookie("uid", str(uuid.uuid4()), max_age=None, path='/', secure=True, httponly=True)
			return resp

		return render_create()
		
	if session.get('videos', None) is None:
			session['videos'] = []

	if request.form.get("remove") is not None:
		return remove_video(request.form["remove"])
	
	url = request.form['url']

	if not validators.url(url):
		return render_with_err()

	with YoutubeDL(ydl_opts) as ydl:
		try:
			vid_info = ydl.extract_info(url, download=False)

		except Exception:
			return render_with_err()

	session_vids = session['videos']
	fetched_video: dict = video_data(vid_info["thumbnail"], len(session_vids) + 1, vid_info["title"], url)
	session_vids.append(fetched_video)
	session['videos'] = session_vids

	if session.get("playlist_id") is None:
		session["playlist_id"] = str(uuid.uuid4())

		data_to_store = (
			session["playlist_id"], request.cookies.get("uid"), json.dumps(fetched_video)
		)

		if usingRPi: db.initialize_playlist(data_to_store)

	elif usingRPi:
		db.update_data(
			session["playlist_id"],
			json.dumps(fetched_video),
			len(session_vids)
		)

	return render_create(vids=session_vids, sharevalue=f'https://www.mixedplaylist.com/playlist/{session["playlist_id"]}')

def remove_video(index: int) -> str:
	print(index)

def render_with_err() -> str:
	if session.get("playlist_id") is not None:
		return render_create(vids=session['videos'], error=True, sharevalue=f'https://www.mixedplaylist.com/playlist/{session["playlist_id"]}')
	
	return render_create(vids=session['videos'], error=True)