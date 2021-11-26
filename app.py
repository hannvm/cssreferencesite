from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def nav():
    return render_template('home.html')

@app.route('/styles.html')
def about():
    return render_template('styles.html')

@app.route('/layoutcss.html')
def layout():
    return render_template('layoutcss.html')

@app.route('/animations.html')
def animations():
    return render_template('animations.html')


if __name__ == '__main__':
    app.run(debug=True)