#!/usr/bin/env python
from flask import Flask
from flask import flash
from flask import abort
from flask import jsonify
from flask import request
from validate import Validator, ValidateError
from avg_act import average_activity
from dose_rate import dose_rate

app = Flask(__name__)

vtor = Validator()


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/doserate", methods=['GET', 'POST'])
def doserate():
    if request.json is None:
        data = request.args
    else:
        data = request.json

    starting_activity = data.get('starting_activity', '100.0')
    distance = data.get('distance', '1.0')
    time_per_run = data.get('time_per_run', '30')
    number_of_runs = data.get('number_of_runs', '10')
    isotope_halflife = data.get('isotope_halflife', '110')
    days_per_week = data.get('days_per_week', '5')

    try:
        starting_activity = vtor.check('float', starting_activity)
        distance = vtor.check('float', distance)
        time_per_run = vtor.check('float', time_per_run)
        number_of_runs = vtor.check('float', number_of_runs)
        isotope_halflife = vtor.check('float', isotope_halflife)
        days_per_week = vtor.check('float', days_per_week)
    except ValidateError:
        #flash('Invalid entry, all values must be floats or ints!')
        abort(404)

    avg_act = average_activity(starting_activity,
                               isotope_halflife,
                               0, time_per_run)
    app.logger.debug("Avg Activity: %f" % avg_act)
    app.logger.debug("Hrs/Week/Run: %f", time_per_run / 60.0 / 40.0)
    app.logger.debug("Distance: %f" % distance)
    dose = dose_rate(avg_act,
                     time_per_run / 60.0 / 40.0,
                     distance)
    app.logger.debug("Dose: %f" % dose)
    dose = dose * number_of_runs * days_per_week
    results = {"dose": dose,
               "dose units": "mrem/week",
               "avgerage activity": avg_act,
               "activity units": "mCi"}
    return jsonify(**results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
