from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def index():
    url = "https://raw.githubusercontent.com/Val-istar-Guo/article/master/articles/%E4%B8%BA%E8%84%8F%E6%95%B0%E6%8D%AE%E6%B6%88%E6%AF%92.md"
    return requests.get(url).text

if __name__ == '__main__':
    app.run(debug = True,port = 8080)