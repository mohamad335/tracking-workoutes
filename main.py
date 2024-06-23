import requests
from datetime import datetime
GENDER = "type your gender here"
WEIGHT_KG = 70
HEIGHT_CM = 181
AGE = 23
APP_ID="xxxxxxxx"
APP_KEY="xxxxxxxxxxxxx"
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
result=response.json()

today_date=datetime.now().strftime("%d/%m/%Y")
now_time=datetime.now().strftime("%X")
sheety_endpoint="xxxxxxxxxxxxxxxxxxxxx"
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
headers={
    "Authorization":"Basic Ym9vZGk6YWV6YWttaTEyMw=="
}
sheety_response=requests.post(sheety_endpoint, json=sheet_inputs, headers=headers)
print(sheety_response.text)