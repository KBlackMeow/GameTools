from flask import Flask, request

app = Flask(__name__)

@app.route('/abc', methods=['POST'])
def upload_file():
    file = request.files['file']  # 获取上传的文件
    file.save('uploaded_file.txt')  # 保存文件到服务器
    return '文件上传成功！'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=44444)