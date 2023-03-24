from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'secret_key' 


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        return redirect(url_for('result'))
    return render_template('form.html')


@app.route('/result')
def result():
    name = session.get('name', None)
    location = session.get('location', None)
    if name is None or location is None:
        return redirect(url_for('index'))
    return render_template('result.html', name=name, location=location)


if __name__ == '__main__':
    app.run(debug=True)
