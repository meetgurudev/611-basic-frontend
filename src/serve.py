from flask import Flask, render_template, jsonify, request

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def home_page():
    print("LOG: home page loaded")
    if request.method == 'POST':
        if(request.form.get('login_page_redirect')):
            return login_page()

        elif(request.form.get('registration_page_redirect')):
            return registration_page()

        elif(request.form.get('profile_page_redirect')):
            return profile_page()

        elif(request.form.get('quiz_page_redirect')):
            return quiz_page()
        
        elif(request.form.get('admin_page_redirect')):
            return admin_page()
            
        elif(request.form.get('video_add_edit_page_redirect')):
            return video_add_edit_page()

        elif(request.form.get('quiz_analytics_page_redirect')):
            return quiz_analytics_page()

        elif(request.form.get('video_analytics_page_redirect')):
            return video_analytics_page()

    return render_template('home_page.html')


@application.route('/login', methods=['GET', 'POST'])
def login_page():
    print("LOG: login page loaded")
    if request.method == 'POST':
        if(request.form.get('home_page_redirect')):
            return home_page()

    return render_template('login_page.html')


@application.route('/registration', methods=['GET', 'POST'])
def registration_page():
    print("LOG: registration page loaded")
    if request.method == 'POST':
        if(request.form.get('home_page_redirect')):
            return home_page()
    return render_template('registration_page.html')


@application.route('/profile', methods=['GET', 'POST'])
def profile_page():
    print("LOG: profile page loaded")
    if request.method == 'POST':
        if(request.form.get('home_page_redirect')):
            return home_page()
    return render_template('profile_page.html')


@application.route('/quiz', methods=['GET', 'POST'])
def quiz_page():
    print("LOG: profile page loaded")
    if request.method == 'POST':
        if(request.form.get('home_page_redirect')):
            return home_page()
    return render_template('quiz_page.html')


@application.route('/admin', methods=['GET', 'POST'])
def admin_page():
    print("LOG: admin page loaded")
    if request.method == 'POST':
        if(request.form.get('home_page_redirect')):
            return home_page()
    return render_template('admin_page.html')

@application.route('/video_add_edit', methods=['GET', 'POST'])
def video_add_edit_page():
    print("LOG: video_add_edit page loaded")
    if request.method == 'POST':
        if(request.form.get('home_page_redirect')):
            return home_page()
    return render_template('video_add_edit_page.html')


@application.route('/quiz_analytics', methods=['GET', 'POST'])
def quiz_analytics_page():
    print("LOG: quiz_analytics page loaded")
    if request.method == 'POST':
        if(request.form.get('home_page_redirect')):
            return home_page()
    return render_template('quiz_analytics_page.html')


@application.route('/video_analytics', methods=['GET', 'POST'])
def video_analytics_page():
    print("LOG: video_analytics page loaded")
    if request.method == 'POST':
        if(request.form.get('home_page_redirect')):
            return home_page()
    return render_template('video_analytics_page.html')

    


## Change this during aws deployment
application.run(host="localhost", port="5000")