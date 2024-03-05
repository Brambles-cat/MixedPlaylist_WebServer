from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    if request.method == 'POST':
        input_string = request.form['input_string']
        # Process the input string (e.g., send it to a Python script)
        # and generate the output
        output = "Output generated from processing: " + input_string
        return render_template('index.html', output=output)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
