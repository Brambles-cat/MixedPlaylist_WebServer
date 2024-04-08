from app import flaskapp, usingRPi, render_create, ensure_cookies
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
	if session.get('videos') is None:
		session['videos'] = []

	if request.method != 'POST':
		resp = make_response(render_create(vids=session.get('videos')))
		ensure_cookies(resp)
		return resp

	if request.form.get("remove") is not None:
		return remove_video(request.form["remove"])
	
	if (len(session['videos'])) >= 10:
		return render_with_err('Only a Max of 10 Videos Allows')

	url = request.form['url']

	if not validators.url(url):
		return render_with_err('Invalid URL')
	
	session_vids = session['videos']

	for video in session_vids:
		if video['url'] == url:
			return render_with_err('Video Already in Playlist')

	with YoutubeDL(ydl_opts) as ydl:
		try:
			vid_info = ydl.extract_info(url, download=False)

		except Exception:
			return render_with_err('Invalid URL')

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
		db.set_video(
			session["playlist_id"],
			json.dumps(fetched_video),
			len(session_vids)
		)

	return render_create(vids=session_vids, sharevalue=f'https://www.mixedplaylist.com/playlist/{session["playlist_id"]}')

def remove_video(index: str) -> str:
	playlist: list = session["videos"]

	if len(playlist) == 1:
		if usingRPi: db.delete_row(session["playlist_id"])
		session["videos"] = []
		session["playlist_id"] = None
		return render_create()
	
	index: int = int(index) - 1

	try:
		playlist.pop(index)
	except Exception as e:
		if not usingRPi: return render_create() # worry about this later

		playlist_sync = db.get_playlist(session["playlist_id"])

		if playlist_sync == None:
			return render_create()
		
		playlist_sync = playlist_sync[2:]
		print(playlist_sync)
		session["videos"] = [json.loads(vid) for vid in playlist_sync if vid is not None]
		return render_create(vids=session["videos"])
	
	for i in range(len(playlist)):
		playlist[i]['index'] = i + 1

	if usingRPi: db.set_videos(session["playlist_id"], playlist)

	session['videos'] = playlist

	return render_create(vids=session['videos'], sharevalue=f'https://www.mixedplaylist.com/playlist/{session["playlist_id"]}')

def render_with_err(error_msg: str) -> str:
	if session.get("playlist_id") is not None:
		return render_create(vids=session['videos'], error=error_msg, sharevalue=f'https://www.mixedplaylist.com/playlist/{session["playlist_id"]}')
	
	return render_create(vids=session['videos'], error=error_msg)