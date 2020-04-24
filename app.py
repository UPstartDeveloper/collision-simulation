
from flask import Flask, render_template, redirect, url_for, request
import os
import math
import numpy as np


app = Flask(__name__)


def calculate_initial_momentum(m1, m2, init_v1, init_v2):
    '''Return initial momentum of the system.'''
    total_momentum_initial = (m1 * init_v1) + (m2 * init_v2)
    return total_momentum_initial


def calculate_initial_kinetic(m1, m2, init_v1, init_v2):
    '''Return initial kinetic energy of the system.'''
    total_kinetic_initial = (
        (.5 * (m1 * math.pow(init_v1, 2))) + (.5 * (m2 * math.pow(init_v2, 2)))
    )
    return total_kinetic_initial


def calculate_final_v2(total_momentum_initial, m1, m2,
                       total_kinetic_initial, init_v2):
    """Credit to Professor Koh of Dominican Univeristy of California for the
       algorithm used in this function!
    """
    b = (2 * total_momentum_initial * m2) / m1
    d_part1 = ((-4 * math.pow(total_momentum_initial, 2) * m2) / m1)
    d_part2 = 8 * m2 * total_kinetic_initial
    d_part3 = ((8 * math.pow(m2, 2) * total_kinetic_initial) / m1)
    d = d_part1 + d_part2 + d_part3
    a = m2 + (math.pow(m2, 2) / m1)
    sol1 = round((b+math.sqrt(d))/(2*a), 4)
    sol2 = round((b-math.sqrt(d))/(2*a), 4)
    # return the value NOT equal to init_v2
    if sol1 == init_v2:
        return sol2
    else:
        return sol1


def calculate_final_v1(total_momentum_initial, m1, m2, v2):
    """Credit to Professor Koh of Dominican Univeristy of California for the
       algorithm used in this function!
    """
    return (total_momentum_initial - (m2 * v2)) / m1


def calculation(m1, m2, init_v1, init_v2, elastic):
    '''Returns the final velocities of two objects after a collision.'''
    # calculate momentum of the system in its initial state
    total_momentum_initial = (
        calculate_initial_momentum(m1, m2, init_v1, init_v2))
    if elastic == "Elastic Collision":
        # calculate total kinetic energy of the system in its initial state
        total_kinetic_initial = (
            calculate_initial_kinetic(m1, m2, init_v1, init_v2)
        )
        # solve for v1 and v2
        final_v2 = calculate_final_v2(total_momentum_initial, m1, m2,
                                      total_kinetic_initial, init_v2)
        final_v1 = calculate_final_v1(total_momentum_initial, m1, m2, final_v2)
        # format in readable text
        return (
            f'You Selected: {elastic}. The resulting final velocities are: ' +
            f'v1 = {final_v1} meters per second and ' +
            f'v2 = {final_v2} meters per second.'
        )
    elif elastic == "Perfectly Inelastic Collision":
        # final velocity = total init momentum of system / sum of masses
        mass_system = m1 + m2
        final_v = round((total_momentum_initial / mass_system), 3)
        return (
            f'You Selected: {elastic}. The ' +
            f'resulting final velocity is: {final_v} meters per second.'
        )


@app.route('/', methods=['GET', 'POST'])
def simulation():
    '''Display a form to input values, and displays result of calculation.'''
    m1 = request.form.get('mass1')
    m2 = request.form.get('mass2')
    init_v1 = request.form.get('velocity1')
    init_v2 = request.form.get('velocity2')
    elastic = request.form.get('type')
    # calculate the results
    if m1 is not None:
        results = calculation(float(m1), float(m2), float(init_v1),
                              float(init_v2), elastic)
    else:
        results = ''
    return render_template('index.html', results=results)
    # after form submission
    if request.method == 'POST':
        return redirect(url_for('simulation'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
