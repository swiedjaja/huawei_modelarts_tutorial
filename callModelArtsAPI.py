import requests

url = "https://e27faf2cc66a42fbad2dce18747962e5.apig.cn-north-4.huaweicloudapis.com/v1/infers/0daea6f3-e118-44aa-8389-bfac7a78fb94"
headers   = { "X-Apig-AppCode": "b125f764043a4617a948a7f58ec140a181f288b710924de6bc7b6652f12759ea" }
dataFiles =  {"images": ("tulip1.jpeg", open("tulip1.jpeg", "rb"), "image/jpeg", {})}
try:
    response = requests.post(url, headers=headers, files=dataFiles)
    print(response.text)
    print(response.status_code)
    jsonResult = response.json()
    result = jsonResult['predicted_label']
    arScores = jsonResult['scores']
    predicted_score = 0
    for score in arScores:
        # print(score)
        if score[0]==result:
            predicted_score = float(score[1])
    print("Result: %s : predicted: %.2f" % (result, predicted_score))
except IOError as e:
    print("Error: ", str(e))