import requests
GENDER = "type your gender here"
WEIGHT_KG = 0
HEIGHT_CM = 0
AGE = 0
APP_ID="2c86f591"
APP_KEY="2860f3e210b7f55271645b7bc1c9f088"
natural_language_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
headers={
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    "Content-Type":"application/json"
}
params={
    "query":input("Tall me witch exercises you did:")
    ,"gender":GENDER
    ,"weight_kg":WEIGHT_KG
    ,"height_cm":HEIGHT_CM
    ,"age":AGE
}
response=requests.post(url=natural_language_endpoint,json=params,headers=headers)
print(response.text)