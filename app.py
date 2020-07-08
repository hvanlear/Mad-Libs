from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-secret'
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/story')
def show_story():
    place = request.args['place']
    noun = request.args['noun']
    adjective = request.args['adjective']
    verb = request.args['verb']
    plural_noun = request.args['plural_noun']
    new_story_parts = {'place': place, 'adjective': adjective, 'noun': noun,
                       'verb': verb, 'plural_noun': plural_noun}
    text = story.generate(new_story_parts)
    return render_template('story.html', place=place, noun=noun, verb=verb, plural_noun=plural_noun, adjective=adjective, text=text)
