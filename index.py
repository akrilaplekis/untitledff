from flask import *


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home_page():
    response = render_template('index.html')

    return response


@app.route('/about', methods=['GET'])
def get_about_page():
    response = render_template('about.html')

    return response


@app.route('/articles', methods=['GET'])
def get_articles_page():
    response = render_template('articles.html')

    return response


@app.route('/library', methods=['GET'])
def get_library_page():
    response = render_template('library.html')

    return response


@app.route('/login', methods=['GET'])
def login_page():
    response = render_template('login.html')

    return response


if __name__ == '__main__':
    app.run(port=5000)
