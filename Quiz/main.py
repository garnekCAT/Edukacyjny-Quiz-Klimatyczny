from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET",'POST'])
def index():
    return render_template('index.html')

@app.route('/pyt1', methods=['POST'])
def lights2():
    aktualny_wynik = request.form.get('score')
    return render_template('lights1.html', score=aktualny_wynik)

@app.route('/pyt2', methods=['POST'])
def lights3():
    aktualny_wynik = request.form.get('score')
    return render_template('lights2.html', score=aktualny_wynik)

@app.route('/pyt3', methods=['POST'])
def lights4():
    aktualny_wynik = request.form.get('score')
    return render_template('lights3.html', score=aktualny_wynik)

@app.route('/pyt4', methods=['POST'])
def lights5():
    aktualny_wynik = request.form.get('score')
    return render_template('lights4.html', score=aktualny_wynik)

@app.route('/pyt5', methods=['POST'])
def lights6():
    aktualny_wynik = request.form.get('score')
    return render_template('lights5.html', score=aktualny_wynik)

@app.route('/pyt6', methods=['POST'])
def lights7():
    aktualny_wynik = request.form.get('score')
    return render_template('lights6.html', score=aktualny_wynik)

@app.route('/pyt7', methods=['POST'])
def lights8():
    aktualny_wynik = request.form.get('score')
    return render_template('lights7.html', score=aktualny_wynik)

@app.route('/pyt8', methods=['POST'])
def lights9():
    aktualny_wynik = request.form.get('score')
    return render_template('lights8.html', score=aktualny_wynik)

@app.route('/pyt9', methods=['POST'])
def lights10():
    aktualny_wynik = request.form.get('score')
    return render_template('lights9.html', score=aktualny_wynik)

@app.route('/pyt10', methods=['POST'])
def lights11():
    aktualny_wynik = request.form.get('score')
    return render_template('lights10.html', score=aktualny_wynik)

@app.route('/wynik', methods=['POST'])
def lights12():
    aktualny_wynik = request.form.get('score')
    return render_template('wynik.html', score=aktualny_wynik)

app.run(debug=True)
