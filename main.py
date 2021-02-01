from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import requests
import json





fruit = "apple"
add= "https://api.edamam.com/api/nutrition-data?app_id=4e2f096a&app_key=50ba9a8185c75c3711eb46bb4b86cba9&ingr=1%20"
com_Add= add+fruit
print(com_Add)
res = requests.get(com_Add)
print (res)
y =  json.loads(res.text)

fat_quality = round(y['totalNutrients']['FAT']['quantity'],2)
fat_unit =(y['totalNutrients']['FAT']['unit'])

carb_quality = round(y['totalNutrients']['CHOCDF']['quantity'],2)
carb_unit =(y['totalNutrients']['CHOCDF']['unit'])

protein_quality = round(y['totalNutrients']['PROCNT']['quantity'],2)
protein_unit =(y['totalNutrients']['PROCNT']['unit'])

print('Calories',y['calories'])
print('FAT:',fat_quality , fat_unit)
print('CARBS:',carb_quality , carb_unit)
print('PROTEIN:',protein_quality , protein_unit)
