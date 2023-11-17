from flask import Flask
from flask import render_template

import json
import random

app = Flask(__name__)

file = open('words.json', encoding='utf8')
words = json.load(file)
words_keys = list(words.keys())
print(words_keys)
print()
@app.route('/')
def main_page():
    word = random.choice(words_keys)
    data = words[word]
    data['options'] = set(data['options'])

    return render_template('index.html', word=word, data=data)

app.run()