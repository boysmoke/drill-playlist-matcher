
from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    spotify_url = request.form.get('spotify_url')
    audio_file = request.files.get('audio_file')

    if spotify_url:
        result = {
            'source': 'Spotify Link',
            'link': spotify_url,
            'analysis': {
                'tempo': '143 BPM',
                'key': 'G minor',
                'genre': 'Drill',
                'mood': 'Energetic, Gritty',
                'energy': 'High'
            },
            'playlists': [
                {'name': 'UK Drill 🔥', 'followers': 15000, 'contact': '@ukdrillplug'},
                {'name': 'Dark Trap Vibes', 'followers': 8700, 'contact': 'darktrapcurator@gmail.com'}
            ]
        }
    elif audio_file:
        filepath = os.path.join(UPLOAD_FOLDER, audio_file.filename)
        audio_file.save(filepath)
        result = {
            'source': 'Audio File',
            'filename': audio_file.filename,
            'analysis': {
                'tempo': '140 BPM',
                'key': 'F# minor',
                'genre': 'Drill',
                'mood': 'Dark, Aggressive',
                'energy': 'High'
            },
            'playlists': [
                {'name': 'Naija Drill 💥', 'followers': 6200, 'contact': '@naijadrillmusic'},
                {'name': 'Aggro Beats', 'followers': 5000, 'contact': None}
            ]
        }
    else:
        return "Please provide a Spotify link or upload an audio file.", 400

    return render_template('results.html', result=result)
