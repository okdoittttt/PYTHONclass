from flask import Flask
import cv2
import face_recognition
import random

# Flask는 기본적으로 5000번 포트에서 실행된다.
app = Flask(__name__)

# 메모리에 올라와 있는 데이터를 사용 하는 중. 만약 쓰기 기능을 사용 하게 되면 값이 초기화 되기에 좋지 않다. 최종적으로 데이터베이스에 저장해야 한다.
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

# 중복되는 코드를 template으로 만들어 쉽게 사용할 함수.
def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')

# <> 자리에 이름을 정하면 함수에 parameter 중 같은 이름의 parameter에 값을 받을 수 있게 해준다.
@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    print(title, body)
    return template(getContents(), f'<h2>{title}</h2>{body}')

app.run(debug=True)
# port 변경하는 방법 -> app.run(port=5001)

