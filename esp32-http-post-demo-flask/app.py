from flask import Flask, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_fft', methods=['POST'])
def post_fft():
    data = request.get_json()
    print("收到 FFT 資料：", data)
    socketio.emit('new_fft', data)  # 推送到前端
    return "已接收", 200

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)