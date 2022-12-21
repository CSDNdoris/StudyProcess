from flask import Flask #导入Flask并创建Flask对象的实例

app = Flask(__name__)
from flask_cors import CORS
CORS(app, supports_credentials=True)

@app.route('/api')

def index():
    return "Hello, Flask!"

if __name__=='__main__':
    app.run(debug=True)