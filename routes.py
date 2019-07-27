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


@app.route('/home', methods=["GET","POST"])
def home():
    if request.method == 'POST':
        if "home" in request.form:
            return redirect(url_for('home'))
        elif "healthtips" in request.form:
            return redirect(url_for('healthtips'))
        elif "accounts" in request.form:
            return redirect(url_for('accounts'))
        elif "friends" in request.form:
            return redirect(url_for('friends'))

    if request.method == 'POST':
        if "gym" in request.form:
            return redirect(url_for('gym'))
        elif "studywork" in request.form:
            return redirect(url_for('studywork'))
        elif "diet" in request.form:
            return redirect(url_for('diet'))
        elif "sleep" in request.form:
            return redirect(url_for('sleep'))

    return render_template('base.html')

@app.route('/healthtips', methods=["GET","POST"])
def healthtips():
    if request.method == 'POST':
        if "home" in request.form:
            return redirect(url_for('home'))
        elif "healthtips" in request.form:
            return redirect(url_for('healthtips'))
        elif "accounts" in request.form:
            return redirect(url_for('accounts'))
        elif "friends" in request.form:
            return redirect(url_for('friends'))
    return render_template('healthtips.html')
    
@app.route('/accounts', methods=["GET","POST"])
def accounts():
    if request.method == 'POST':
        if "home" in request.form:
            return redirect(url_for('home'))
        elif "healthtips" in request.form:
            return redirect(url_for('healthtips'))
        elif "accounts" in request.form:
            return redirect(url_for('accounts'))
        elif "friends" in request.form:
            return redirect(url_for('friends'))
    return render_template('accounts.html')

@app.route('/friends', methods=["GET","POST"])
def friends():
    if request.method == 'POST':
        if "home" in request.form:
            return redirect(url_for('home'))
        elif "healthtips" in request.form:
            return redirect(url_for('healthtips'))
        elif "accounts" in request.form:
            return redirect(url_for('accounts'))
        elif "friends" in request.form:
            return redirect(url_for('friends'))
    return render_template('friends.html')

@app.route('/home/gym', methods=["GET","POST"])
def gym():
    if request.method == 'POST':
        if "home" in request.form:
            return redirect(url_for('home'))
        elif "healthtips" in request.form:
            return redirect(url_for('healthtips'))
        elif "accounts" in request.form:
            return redirect(url_for('accounts'))
        elif "friends" in request.form:
            return redirect(url_for('friends'))
    return render_template('gym.html')