"""This is a new trial on GUI development for Windows app.
The tool is WxPython.
End of the comment."""

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World'
if __name__ == '__main__':
    app.run()
