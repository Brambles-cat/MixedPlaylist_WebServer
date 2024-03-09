from flask import Flask, redirect, url_for, request, send_from_directory, render_template
from yt_dlp import YoutubeDL

from modulethingy import *

app = Flask(__name__)

videos = []

ydl_opts = {
    "quiet": False,
}

ydl = YoutubeDL(ydl_opts) #ydl.close()

@app.route('/playlist/<id>')
def playlist(id: str):
	pass

@app.route("/create", methods=['POST', 'GET'])
def create():
	if request.method != 'POST':
		return render_template('create.html')
	
	with YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(request.form['url'], download=False)
		video = Video()
		video.thumbnail = info["thumbnail"];
		video.index = len(videos) + 1
		videos.append(video)

	return render_template('create.html', vids=videos) #https://www.youtube.com/watch?v=UEJPpJPkFbQ



if __name__ == '__main__':
	
	#if "entries" in info:
	#			info = info["entries"][0]
	#			print(info)
	#		else:
	#			print(info.keys())
	#			print(info["thumbnail"])

	app.run(host='localhost', port=5000, debug=True)



# not impotant
	
@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name

@app.route('/')
def enter():
	return send_from_directory('templates', 'index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
	print("meodrt\n\n\nfy")
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('success', name=user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success', name=user))
