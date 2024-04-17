from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        # Get the English text from the form
        english_text = request.form['english-text']

        # Write the English text to a file
        with open('input.txt', 'w') as f:
            f.write(english_text)

        # Call the translation script
        subprocess.run(['python', 'translate.py'])

        return render_template('translation_result.html')

    return render_template('respidior.html')

if __name__ == '__main__':
    app.run(debug=True)

