from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/principal')
def principal():
    return render_template('principal.html')


if __name__ == '__main__':
    app.run(debug=True)


