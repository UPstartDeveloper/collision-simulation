
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


def calculation(m1, m2, init_v1, init_v2, elastic=False):
    '''Returns the final velocities of two objects after a collision.'''
    if elastic is True:
        pass
    else:
        # final velocity = total init momentum of system / sum of masses
        total_momentum_initial = (m1 * init_v1) + (m2 * init_v2)
        mass_system = m1 + m2
        final_v = total_momentum_initial / mass_system
        return final_v


@app.route('/', methods=['GET', 'POST'])
def simulation():
    '''Display a form to input values, and displays result of calculation.'''
    return 'Hello World!'

    # templates
    #


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
