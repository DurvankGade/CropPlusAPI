import requests

files = {'image': open('healthy_tea_leaf202.jpg', 'rb')}
response = requests.post('http://192.168.162.121:8000/predict_tea_disease', files=files)

print(response.json())