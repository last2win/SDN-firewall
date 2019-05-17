from sklearn.externals import joblib


# 加载模型
mlp = joblib.load("new.mlp-module.m")
vectorizer = joblib.load("new.vectorizer.pkl")
# 判断


def judge_payload(payload):
    if payload[0] != '/':
        payload = '/'+payload
    payload = [payload]
    x = vectorizer.transform(payload)
    predicted = mlp.predict(x)
 #   print(predicted)
    if predicted[0] == 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    payload = "/search.pl?form=../../../../../../etc/passwd\x00"
    if judge_payload(payload) == 1:
        print("it is an evil payload")
    else:
        print("it is a normal payload")
