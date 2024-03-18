from app import flaskapp
from flask import request, make_response, render_template, session
import uuid
from yt_dlp import YoutubeDL
from modulethingy import *
import db
import json

ydl_opts = {
    "quiet": True,
}

@flaskapp.route("/create", methods=['POST', 'GET'])
def create():
	if request.method != 'POST':
		if request.cookies.get("uid") is None:
			print("makin de cookie")
			resp = make_response(render_template('create.html'))
			resp.set_cookie("uid", str(uuid.uuid4()), max_age=None, path='/', secure=True, httponly=True)
			return resp
		else:
			print(request.cookies)

		return render_template('create.html')
	
	with YoutubeDL(ydl_opts) as ydl:
		if session.get('videos', None) is None:
			session['videos'] = []

		session_videos: list[dict] = session['videos']
		url = request.form['url']

		try:
			info = ydl.extract_info(url, download=False)
		except Exception as e:
			return render_template('create.html', vids=session_videos, error=True)

		video: dict = video_data(info["thumbnail"], len(session_videos) + 1, info["title"], url)
		session_videos.append(video)

		data_to_store = [str(uuid.uuid4()), request.cookies.get("uid")]
		for vid in session_videos:
			data_to_store.append(json.dumps(vid))
		for i in range(10 - len(session_videos)):
			data_to_store.append(None)
		
		db.insert_data(tuple(data_to_store))

	return render_template('create.html', vids=session_videos)