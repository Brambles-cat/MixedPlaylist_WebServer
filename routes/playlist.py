from flask import render_template
from app import flaskapp
import db
import json

@flaskapp.route('/playlist/<id>')
def playlist(id: str):
	db_entry = db.get_playlist(id)

	video_list = db_entry[2:]
	video_list = [json.loads(vid) for vid in video_list if vid is not None]

	return render_template('playlist.html', vids = video_list)
