from flask import Flask, render_template, request

from output_test import make_lilypond, what_is_note, has_accidental

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def guitar():
    return render_template('guitar-chords.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    notes = [request.form['note1'], request.form['note2'], request.form['note3'],
    request.form['note4']]
    make_lilypond(notes)
    return render_template('output_test.html', notes = notes)

if __name__ == '__main__':
    app.run(debug=True)
