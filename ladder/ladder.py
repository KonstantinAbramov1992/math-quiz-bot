from flask import Flask, render_template
from Rank import get_rank

app = Flask(__name__)


@app.route('/')
def ladder():
    # Here we get our list of dicts and send them to our html
    ladder = get_rank()
    return render_template('ladder.html', ladder=ladder)