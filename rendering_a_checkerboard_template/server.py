from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', x=int(8), y=int(8))

@app.route('/<int:y>')
def display(y):
    return render_template('index.html', x=int(8), y=y)

@app.route('/<int:x>/<int:y>')
def displaydim(x, y):
    return render_template('index.html', x=x, y=y)


@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def changeSquares(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)