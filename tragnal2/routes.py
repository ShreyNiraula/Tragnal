from flask import render_template, redirect, url_for, flash, request,Response, jsonify, json
from tragnal2 import app,db, bcrypt# no more from flask , causes error due to package issues
from tragnal2.forms import RegistrationForm, LoginForm
from tragnal2.models import User
from flask_login import login_user, current_user, logout_user, login_required
from tragnal2.webcam import WebcamStream
import cv2

import koteshworSeqGenerator, jadibutiSeqGenerator, lokanthaliSeqGenerator

def encode(phase):
    vali = '@#$'

    if (phase['t1'][0] == 1 and phase['t1'][1] == 0 and phase['t1'][2] == 0 and phase['t1'][3] == 0):
        key = '1'
    elif (phase['t1'][0] == 0 and phase['t1'][1] == 1 and phase['t1'][2] == 0 and phase['t1'][3] == 0):
        key = '2'
    elif (phase['t1'][0] == 0 and phase['t1'][1] == 0 and phase['t1'][2] == 1 and phase['t1'][3] == 0):
        key = '3'
    elif (phase['t1'][0] == 0 and phase['t1'][1] == 0 and phase['t1'][2] == 0 and phase['t1'][3] == 1):
        key = '4'
    elif (phase['t1'][0] == 0 and phase['t1'][1] == 0 and phase['t1'][2] == 1 and phase['t1'][3] == 1):
        key = '5'

    vali += key
    vali += str(int(phase['t1'][4] / 10))
    vali += str(int(phase['t1'][4] % 10))

    if (phase['t2'][0] == 1 and phase['t2'][1] == 0 and phase['t2'][2] == 0 and phase['t2'][3] == 0):
        key = '1'
    elif (phase['t2'][0] == 0 and phase['t2'][1] == 1 and phase['t2'][2] == 0 and phase['t2'][3] == 0):
        key = '2'
    elif (phase['t2'][0] == 0 and phase['t2'][1] == 0 and phase['t2'][2] == 1 and phase['t2'][3] == 0):
        key = '3'
    elif (phase['t2'][0] == 0 and phase['t2'][1] == 0 and phase['t2'][2] == 0 and phase['t2'][3] == 1):
        key = '4'
    elif (phase['t2'][0] == 0 and phase['t2'][1] == 0 and phase['t2'][2] == 1 and phase['t2'][3] == 1):
        key = '5'

    vali += key
    vali += str(int(phase['t2'][4] / 10))
    vali += str(int(phase['t2'][4] % 10))

    if (phase['t3'][0] == 1 and phase['t3'][1] == 0 and phase['t3'][2] == 0 and phase['t3'][3] == 0):
        key = '1'
    elif (phase['t3'][0] == 0 and phase['t3'][1] == 1 and phase['t3'][2] == 0 and phase['t3'][3] == 0):
        key = '2'
    elif (phase['t3'][0] == 0 and phase['t3'][1] == 0 and phase['t3'][2] == 1 and phase['t3'][3] == 0):
        key = '3'
    elif (phase['t3'][0] == 0 and phase['t3'][1] == 0 and phase['t3'][2] == 0 and phase['t3'][3] == 1):
        key = '4'
    elif (phase['t3'][0] == 0 and phase['t3'][1] == 0 and phase['t3'][2] == 1 and phase['t3'][3] == 1):
        key = '5'

    vali += key
    vali += str(int(phase['t3'][4] / 10))
    vali += str(int(phase['t3'][4] % 10))

    return vali

def encodeJadibuti(phase):
    vali = '@#$'

    if (phase['t1'][0] == 1 and phase['t1'][1] == 0 and phase['t1'][2] == 0 and phase['t1'][3] == 0):
        key = '1'
    elif (phase['t1'][0] == 0 and phase['t1'][1] == 1 and phase['t1'][2] == 0 and phase['t1'][3] == 0):
        key = '2'
    elif (phase['t1'][0] == 0 and phase['t1'][1] == 0 and phase['t1'][2] == 1 and phase['t1'][3] == 0):
        key = '3'
    elif (phase['t1'][0] == 0 and phase['t1'][1] == 0 and phase['t1'][2] == 0 and phase['t1'][3] == 1):
        key = '4'
    elif (phase['t1'][0] == 0 and phase['t1'][1] == 0 and phase['t1'][2] == 1 and phase['t1'][3] == 1):
        key = '5'

    vali += key
    vali += str(int(phase['t1'][4] / 10))
    vali += str(int(phase['t1'][4] % 10))

    if (phase['t2'][0] == 1 and phase['t2'][1] == 0 and phase['t2'][2] == 0 and phase['t2'][3] == 0):
        key = '1'
    elif (phase['t2'][0] == 0 and phase['t2'][1] == 1 and phase['t2'][2] == 0 and phase['t2'][3] == 0):
        key = '2'
    elif (phase['t2'][0] == 0 and phase['t2'][1] == 0 and phase['t2'][2] == 1 and phase['t2'][3] == 0):
        key = '3'
    elif (phase['t2'][0] == 0 and phase['t2'][1] == 0 and phase['t2'][2] == 0 and phase['t2'][3] == 1):
        key = '4'
    elif (phase['t2'][0] == 0 and phase['t2'][1] == 0 and phase['t2'][2] == 1 and phase['t2'][3] == 1):
        key = '5'

    vali += key
    vali += str(int(phase['t2'][4] / 10))
    vali += str(int(phase['t2'][4] % 10))

    if (phase['t3'][0] == 1 and phase['t3'][1] == 0 and phase['t3'][2] == 0 and phase['t3'][3] == 0):
        key = '1'
    elif (phase['t3'][0] == 0 and phase['t3'][1] == 1 and phase['t3'][2] == 0 and phase['t3'][3] == 0):
        key = '2'
    elif (phase['t3'][0] == 0 and phase['t3'][1] == 0 and phase['t3'][2] == 1 and phase['t3'][3] == 0):
        key = '3'
    elif (phase['t3'][0] == 0 and phase['t3'][1] == 0 and phase['t3'][2] == 0 and phase['t3'][3] == 1):
        key = '4'
    elif (phase['t3'][0] == 0 and phase['t3'][1] == 0 and phase['t3'][2] == 1 and phase['t3'][3] == 1):
        key = '5'

    vali += key
    vali += str(int(phase['t3'][4] / 10))
    vali += str(int(phase['t3'][4] % 10))

    return vali

@app.route('/home')
def home():
    return render_template('w3_home.html', title = 'Home Page')  # students on left = used in templates


@app.route('/register', methods = ['GET', "POST"])
def register():
    # if user is loggedin , redirect instead to home
    if current_user.is_authenticated:  # if this is done, also modify the html
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # make hashed form of password being typed in registration form and also decode to string from byte
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # do similar task to generate database object
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, age=form.age.data,)
        # add to database and commit
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data}!, your account is created. Now, login from below', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = "Register Page", form = form)


@app.route('/', methods = ['GET', "POST"])
@app.route('/login', methods = ['GET', "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            # when we access account page without loggin, there are certaing query string
            # request.args.get('next') will get whatever is there after that
            # be sure to use .get, not like ['next'] , because  using later  approach causes error if there is no query string
            # return using ternary condition such that if it exists, return next_page else redirect to home
            # this is done, since, when not logged in go to account page, it directs us to login page,
            # then after login it will redirect to home page and from there, we have to visit account page
            # to prevent this and directly visit account page after login, we have done this
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash('Unsuccessful, check email and password !!', 'danger')
    return render_template('login.html', title = 'Login Page', form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# this function will be accessible only after log in
# login_required is required so that page is only visible after logged in
# here, the order of the decorator matters
# 1st route then tell that it is login required page
# then it goes to init.py and see login_view which tells to go to login page before viewing account page
@app.route('/account')
@login_required
def account():
    return render_template('w3_junction.html', title = 'Next Phase Page')

@app.route('/team')
@login_required
def team():
    return render_template('w3_team.html', title = 'Team Page')

@app.route('/profile')
@login_required
def profile():
    return render_template('w3_profile.html', title = 'Profile Page')

@app.route('/contact')
@login_required
def contact():
    return render_template('w3_contact.html', title = 'Contact Page')



@app.route('/koteshwor')
@login_required
def koteshwor():
    # average day data
    label_day = ['8:00', '10:00', '12:00',
                 '2:00', '4:00', '6:00', '8:00']
    data_day = [3905, 5311,4576 ,3230,4938, 4947, 3065]

    # data for sunday to friday peak volume
    label_week =['Sun', "Mon", 'Tue','Wed', 'Thu', 'Fri', 'Sat']
    data_week = [2221, 2331, 2450, 2053, 2005, 2111, 992]
    return render_template('w3_kot.html', title = 'Koteshwor Juntion',
                           labels_days=label_day, datas_days=data_day,
                           labels_weeks=label_week, datas_weeks=data_week)

@app.route('/jadibuti')
@login_required
def jadibuti():
    label_day = ['8:00', '10:00', '12:00',
              '2:00', '4:00', '6:00', '8:00']
    data_day = [4083,5491,3407,3349,3646,4947,4172]

    # data for sunday to friday peak volume
    label_week =['Sun', "Mon", 'Tue','Wed', 'Thu', 'Fri', 'Sat']
    data_week = [2081, 2118, 2119, 2167, 2236, 2039, 966]
    return render_template('w3_jadi.html', title = 'Jadibuti Juntion',
                           labels_days=label_day, datas_days=data_day,
                           labels_weeks=label_week, datas_weeks=data_week)

@app.route('/lokanthali')
@login_required
def lokanthali():
    label_day = ['8:00', '10:00', '12:00',
                 '2:00', '4:00', '6:00', '8:00']
    data_day = [4008, 5112, 4105, 3345, 4878, 4839, 4222]

    # data for sunday to friday peak volume
    label_week =['Sun', "Mon", 'Tue','Wed', 'Thu', 'Fri', 'Sat']
    data_week = [2100,2120,2230,2354,2340,2050,891]
    return render_template('w3_lok.html', title = 'Lokanthali Juntion',
                           labels_days=label_day, datas_days=data_day,
                           labels_weeks=label_week, datas_weeks=data_week)

# for Ip camera
@app.route('/video')
def index():
    """Video streaming home page."""
    return render_template('video.html')


def gen(camera):
    """Video streaming generator function."""
    while 1:
        if camera.stopped:
         break
        frame = camera.read()
        ret, jpeg = cv2.imencode('.jpg', frame)

        # print("after get_frame")
        if jpeg is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        else:
            print("frame is none")


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(WebcamStream().start()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/rashik', methods = ['GET', "POST"])
def rashik():
    #return encode(seqGenerator.phase)
    return "@#$123123999"

@app.route('/hardwareJadibuti', methods = ['GET', "POST"])
def hardwareJadibuti():
    return encodeJadibuti(jadibutiSeqGenerator.phase)
    # return "@#$123123999"


@app.route("/_imgKoteshwor")
def _imgKoteshwor():
    return jsonify(t1=koteshworSeqGenerator.phase['t1'],
                   t2=koteshworSeqGenerator.phase['t2'],
                   t3=koteshworSeqGenerator.phase['t3'],
                   phase_number = koteshworSeqGenerator.phase_number,
                   )

@app.route("/_imgJadibuti")
def _imgJadibuti():
    return jsonify(t1=jadibutiSeqGenerator.phase['t1'],
                   t2=jadibutiSeqGenerator.phase['t2'],
                   t3=jadibutiSeqGenerator.phase['t3'],
                   phase_number = jadibutiSeqGenerator.phase_number,
                   )
@app.route("/_imgLokanthali")
def _imgLokanthali():
    return jsonify(t1=lokanthaliSeqGenerator.phase['t1'],
                   t2=lokanthaliSeqGenerator.phase['t2'],
                   t3=lokanthaliSeqGenerator.phase['t3'],
                   phase_number = lokanthaliSeqGenerator.phase_number,
                   )

@app.route("/_button_K")
def _button_K():
    global traffic_phase_state_K
    state = request.args.get('state')
    state = int(state)
    koteshworSeqGenerator.traffic_phase_state_K= state
    koteshworSeqGenerator.isPhaseRessetted_K= True
    state+=1
    if state>3:
        state = 1
    return jsonify(
                    phase_number=state,
                   )
@app.route("/_button_J")
def _button_J():
    global traffic_phase_state_J
    state = request.args.get('state')
    state = int(state)
    jadibutiSeqGenerator.traffic_phase_state_J= state
    jadibutiSeqGenerator.isPhaseRessetted_J= True
    state+=1
    if state>3:
        state = 1
    return jsonify(
                    phase_number=state,
                   )

@app.route("/_button_L")
def _button_L():
    global traffic_phase_state_L
    state = request.args.get('state')
    state = int(state)
    jadibutiSeqGenerator.traffic_phase_state_L= state
    jadibutiSeqGenerator.isPhaseRessetted_L= True
    state+=1
    if state>3:
        state = 1
    return jsonify(
                    phase_number=state,
                   )

# # routes associated with charts
# @app.route("/koteshwor")
# def chart():
#     legend = 'Average Traffic Volume Throughout a Day'
#     traffic_volume = [12, 15, 14, 13, 12, 9, 10, 11, 13, 13, 15, 15, 11]
#     time_of_day = ['8:00AM', '9:00AM', '10:00AM', '11:00AM', '12:00PM', '1:00PM',
#              '2:00PM', '3:00PM', '4:00PM', '5:00PM', '6:00PM', '7:00PM',
#              '8:00PM']
#     return render_template('w3_kot.html', values=traffic_volume, labels=time_of_day, legend=legend)

# @app.route('/_get_chartdata')
# def _get_chartdata():
#     legend = 'Average Traffic Volume Throughout a Day'
#     time_of_day = ['8:00AM', '9:00AM', '10:00AM', '11:00AM', '12:00PM', '1:00PM',
#                    '2:00PM', '3:00PM', '4:00PM', '5:00PM', '6:00PM', '7:00PM',
#                    '8:00PM']
#     traffic_volume = [12, 15, 14, 13, 12, 9, 10, 11, 13, 13, 15, 15, 11]
#     return jsonify(
#         values=traffic_volume,
#         labels=time_of_day,
#         legend=legend)

# @app.route('/get_chartdata')
# def get_chartdata():
#   labels = ["Africa", "Asia", "Europe", "Latin America", "North America"]
#   data = [5578,5267,734,784,433]
#   return jsonify({'payload':json.dumps({'values':data, 'labels':labels})})

# @app.route("/koteshwor")
# def result():
#     labels= ["Africa", "Asia", "Europe", "Latin America", "North America"]
#     data = [5578,5267,734,784,433]
#     return render_template("w3_kot.html", jsonify(labels=labels, data=data))