from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def car():
    name = request.form.get('marka')
    color = request.form.get('color')
    return render_template('result.html', marka=name, color=color)

if __name__ == '__main__':
    app.run(debug=True)