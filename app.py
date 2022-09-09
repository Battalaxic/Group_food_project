from flask import Flask, render_template, request, redirect, url_for

'''https://pythonbasics.org/flask-login/'''

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    user_already_created = False
    if request.method == "POST":
        new_user_file = f"static/{request.form.get('username')}.txt"
        try:
            create_file = open(new_user_file, "x")
        except:
            user_already_created = True
        return render_template('launch_page.html', user_already_created=user_already_created)
    return render_template('launch_page.html')


if __name__ == '__main__':
    app.run()
