from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ ==  '__main__':
    app.run( debug=True, port=8000)
    
    
#tutorial: https://youtu.be/iPMzFz_2B4E?list=PLagErt3C7iltAydvN6SgCVKsOH4xQQKsk    