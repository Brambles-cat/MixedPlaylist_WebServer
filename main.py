from flask import Flask, redirect, url_for, request, send_from_directory, render_template
from yt_dlp import YoutubeDL

from modulethingy import *

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True

#Session(app)

videos = []

ydl_opts = {
    "quiet": False,
}

@app.route('/playlist/<id>')
def playlist(id: str):
	pass

@app.route("/create", methods=['POST', 'GET'])
def create():
	if request.method != 'POST':
		return render_template('create.html')
	
	with YoutubeDL(ydl_opts) as ydl:
		url = request.form['url']

		try:
			info = ydl.extract_info(url, download=False)
		except Exception as e:
			return render_template('create.html', vids=videos, error=True)

		video = Video(info["thumbnail"], len(videos) + 1, info["title"], url)
		videos.append(video)
		print(video.title)

	return render_template('create.html', vids=videos) #https://www.youtube.com/watch?v=UEJPpJPkFbQ

@app.route("/")
def enter():
	return render_template('create.html')



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)