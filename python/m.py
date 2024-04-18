from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def about():
    return render_template('upload.html')

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('upload'))

if __name__ == '__main__':
    app.run(debug=True)
