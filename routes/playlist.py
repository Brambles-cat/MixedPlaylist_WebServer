from flask import render_template, session, request, redirect
from app import flaskapp, address, usingRPi
import db
import json

@flaskapp.route('/playlist/<id>') #id. oid
def playlist(id: str):
	db_entry = db.get_playlist(id) if usingRPi else None

	if db_entry == None:
		return render_template('playlist.html')
	
	video_list = db_entry[2:]
	video_list = [json.loads(vid) for vid in video_list if vid is not None]

	uid = request.cookies.get("uid")

	if uid is not None and uid == db_entry[1]:
		session["videos"] = video_list
		session["playlist_id"] = db_entry[0]
		return redirect(f'{address}/create')
	
	return render_template('playlist.html', vids = video_list)
