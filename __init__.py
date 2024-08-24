from flask import Flask, render_template

app = Flask(__name__)

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/experience')
def exp():
    return render_template('exp.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
