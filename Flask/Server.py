from flask import Flask
import random

# Flask는 기본적으로 5000번 포트에서 실행된다.
app = Flask(__name__)

@app.route('/')
def index():
    return 'random : <strong>' + str(random.random()) + '</strong>'

app.run(debug=True)
# port 변경하는 방법 -> app.run(port=5001)