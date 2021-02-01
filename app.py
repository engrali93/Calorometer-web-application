from flask import Flask, redirect, url_for, request, render_template
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('web.html')


@app.route('/result',methods = ['POST'])
def operation_result():
    val = request.form['nm']
    add = "https://api.edamam.com/api/nutrition-data?app_id=4e2f096a&app_key=50ba9a8185c75c3711eb46bb4b86cba9&ingr=1%20"
    com_Add = add + val
    res = requests.get(com_Add)
    y = json.loads(res.text)
    cal = y['calories']
    calu= (y['totalNutrients']['ENERC_KCAL']['unit'])
    fat_quality = round(y['totalNutrients']['FAT']['quantity'], 2)
    fat_unit = (y['totalNutrients']['FAT']['unit'])

    carb_quality = round(y['totalNutrients']['CHOCDF']['quantity'], 2)
    carb_unit = (y['totalNutrients']['CHOCDF']['unit'])

    protein_quality = round(y['totalNutrients']['PROCNT']['quantity'], 2)
    protein_unit = (y['totalNutrients']['PROCNT']['unit'])

    return render_template('web.html',
                           calo=cal,
                           calou=calu,
                           fatq= fat_quality,
                           fatu= fat_unit,
                           proq= protein_quality,
                           prou= protein_unit,
                           carbq=carb_quality,
                           carbu= carb_unit
                           )


if __name__ == '__main__':
   app.run(debug = True)




