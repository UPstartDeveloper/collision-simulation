
from flask import Flask, render_template, redirect, url_for, request
import os


app = Flask(__name__)


def calculation(m1, m2, init_v1, init_v2, elastic):
    '''Returns the final velocities of two objects after a collision.'''
    if elastic == "Elastic Collision":
        pass
    elif elastic == "Perfectly Inelastic Collision":
        # final velocity = total init momentum of system / sum of masses
        total_momentum_initial = (m1 * init_v1) + (m2 * init_v2)
        mass_system = m1 + m2
        final_v = round((total_momentum_initial / mass_system), 3)
        return (
            f'You Selected: {elastic}. The ' +
            f'resulting final velocity is: {final_v} meters per second.'
        )


@app.route('/', methods=['GET', 'POST'])
def simulation():
    '''Display a form to input values, and displays result of calculation.'''
    # initial load of the page
    # if request.method == 'GET':
    # processing the form data
    m1 = float(request.form.get('mass1'))
    m2 = float(request.form.get('mass2'))
    init_v1 = float(request.form.get('velocity1'))
    init_v2 = float(request.form.get('velocity2'))
    elastic = request.form.get('type')
    # calculate the results
    results = calculation(m1, m2, init_v1, init_v2, elastic)
    print(f'Results: {results}')
    return render_template('index.html', results=results)
    # after form submission
    if request.method == 'POST':
        return redirect(url_for('simulation'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
