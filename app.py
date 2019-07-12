from flask import Flask, render_template, request

from output_test import make_lilypond

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def guitar():
    return render_template('guitar-chords.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('output-test.html', note1=request.form['note1'],
    note2=request.form['note2'], note3=request.form['note3'],
    note4=request.form['note4'])

if __name__ == '__main__':
    app.run(debug=True)
