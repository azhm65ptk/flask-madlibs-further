from flask import Flask, render_template, request
from stories import stories

app=Flask(__name__)

@app.route('/')
def select_story():
     return render_template("select-story.html", stories = stories.values())

@app.route('/question')
def ask_question():
    id=request.args['story_id']
    story=stories[id]
    
    prompts=story.prompts

    return render_template('question.html',prompts=prompts, story_id=id,
                            title=story.title)


@app.route("/story")
def show_story():
    """Show story result."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html",
                           title=story.title,
                           text=text)