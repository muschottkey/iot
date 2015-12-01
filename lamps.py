import time
from itertools import cycle
from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
state_cycle = cycle(['on', 'off'])

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

locations = {
 
}

@app.route("/")
@app.route("/<state>")
@app.route("/<location>/<state>")
def update_lamp(location='porch', state=None):
    if state == 'on':
        GPIO.output(11, 1)
    if state == 'off':
        GPIO.output(11, 0)
    if state == 'toggle':
        state = next(state_cycle)
        update_lamp(state)
    template_data = {
        'title' : state,
	'location': location
    }
    return render_template('main.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
