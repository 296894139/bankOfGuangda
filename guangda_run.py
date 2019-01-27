from flask import (
    Flask,
    json,
    request,
    jsonify)

from bank1.bank_guangda import b

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'import_thing'
app.config['JSON_AS_ASCII'] = False
@app.route('/create', methods=['POST'])
def create():
    if b'\xef\xbb\xbf' in request.data:
        print(request.data.decode('utf-8-sig'))
        data = json.loads(request.data.decode('utf-8-sig'))
    else:
        data = json.loads(request.data.decode('utf-8'))
    b.create(data['url'], data['username'], data['password'])
    return "success"

@app.route('/getVerificationCode', methods=['POST'])
def getVerificationCode():
    if b'\xef\xbb\xbf' in request.data:
        data = json.loads(request.data.decode('utf-8-sig').replace("\n", " "))
    else:
        data = json.loads(request.data.decode('utf-8').replace("\n", " "))
    url=b.getBankCaptcha(data['name'],data['id'])
    #result = b.bet(data['kind'], data['multiple'], data['str'])
    return jsonify({'url': url})

@app.route('/getPhoneCaptcha', methods=['POST'])
def getPhoneCaptcha():
    if b'\xef\xbb\xbf' in request.data:
        data = json.loads(request.data.decode('utf-8-sig').replace("\n", " "))
    else:
        data = json.loads(request.data.decode('utf-8').replace("\n", " "))
    responce=b.passBankCaptchaAndgetPhoneCaptcha(data['VerificationCode'])
    #result = b.bet(data['kind'], data['multiple'], data['str'])
    return jsonify({'responce': responce})

@app.route('/getApplicationInformation', methods=['POST'])
def getApplicationInformation():
    if b'\xef\xbb\xbf' in request.data:
        data = json.loads(request.data.decode('utf-8-sig').replace("\n", " "))
    else:
        data = json.loads(request.data.decode('utf-8').replace("\n", " "))
    responce=b.passPhoneCaptcha(data['PhoneVerificationCode'])
    #result = b.bet(data['kind'], data['multiple'], data['str'])
    return jsonify({'responce': responce})

'''@app.route('/info', methods=['GET'])
def info():
    result = b.monitor()
    return result'''
if __name__ == '__main__':
    app.run(port=8081)
