from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)
url = "https://e27faf2cc66a42fbad2dce18747962e5.apig.cn-north-4.huaweicloudapis.com/v1/infers/0daea6f3-e118-44aa-8389-bfac7a78fb94"
headers   = { "X-Apig-AppCode": "b125f764043a4617a948a7f58ec140a181f288b710924de6bc7b6652f12759ea" }

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/recognize', methods = ['POST'])
def call_modelArts():
    f = request.files['imgFilename']
    print('recognize: '+f.filename)
    files = {"images": (f.filename, f.read(), f.content_type)}
    resp = requests.post(url, headers=headers, files=files)
    print('Result: '+resp.text)
    jsonResult = resp.json()
    result = jsonResult['predicted_label']
    arScores = jsonResult['scores']
    predicted_score = 0
    for score in arScores:
        if score[0]==result:
            predicted_score = float(score[1])
    print("Result: %s : predicted: %.2f" % (result, predicted_score))

    if resp.status_code == 200:     
        strStatus = "Success"
    else:
        strStatus = "Failed"
    return render_template("result.html", flower=result, status=strStatus, confidence=predicted_score)

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000, debug=True)
