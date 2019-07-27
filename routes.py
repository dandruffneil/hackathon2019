from flask import render_template, request, redirect, url_for, abort
from server import app

'''
Error page
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

@app.route('/', methods=["GET","POST"])
def welcome():
    # id = idgenerator.next()
    # print(id)
    # system.createOrder(id)
    # print(system)
    if request.method == 'POST':
        if "home" in request.form:
            return redirect(url_for('home'))
        elif "healthtips" in request.form:
            return redirect(url_for('healthtips'))
        elif "accounts" in request.form:
            return redirect(url_for('accounts'))
        elif "friends" in request.form:
            return redirect(url_for('friends'))

    return render_template('welcome.html')

