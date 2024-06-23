import requests
import os
from datetime import datetime
GENDER = "type your gender here"
WEIGHT_KG =75
HEIGHT_CM = 181
AGE = 23
APP_ID=os
APP_KEY= os.environ["APP_KEY"]
MY_TOKEN=os.environ["MY_TOKEN"]
natural_language_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT=os.environ["SHEETY_ENDPOINT"]
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
    "Authorization": f"Basic {MY_TOKEN}"
}
sheety_response=requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=headers)
print(sheety_response.text)