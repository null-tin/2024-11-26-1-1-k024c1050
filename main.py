from flask import Flask, request
app = Flask(__name__)

# サーバールートへアクセスがあった時 --- (*1)
@app.route('/')
def index():
    # フォームを表示する --- (*2)
    return """
        <html><body>
        <form action="/hello" method="GET">
          名前: <input type="text" name="name">
          ひとこと: <input type="text" name="one_word">
          <input type="submit" value="送信">
        </form>
        </body></html>
    """

# /hello へアクセスがあった時 --- (*3)
@app.route('/hello')
def hello():
    # nameのパラメータを得る --- (*4)
    name = request.args.get('name')
    one_word = request.args.get('one_word')
    if name is None: name = '名無し'
    if one_word is None: one_word = 'ひとことコメントを入力してみて下さい'
    # 自己紹介を自動作成
    return """
    <h1>{0}さん、こんにちは！</h1>
    <p>ひとこと: {1}</p>
    """.format(name, one_word)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

