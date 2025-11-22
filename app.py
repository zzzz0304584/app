from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>學號：S1121532<br>姓名：劉紫玲<br>伺服器時間：{now}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
