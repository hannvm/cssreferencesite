from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def nav():
    return render_template('home.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/css.html')
def css():
    return render_template('css.html')

@app.route('/miniprojects.html')
def projects():
    return render_template('miniprojects.html')

if __name__ == '__main__':
    app.run(debug=True)