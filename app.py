from flask import Flask, request, render_template
from  src.componets.predict_pipeline import UserData,PredictPipeline
from src.pipelines.exception import CustomException
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
        age = int(request.form["age"])
        sex = request.form["sex"]
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = request.form["smoker"]
        region = request.form["region"]

        user_data=UserData(age=age,sex=sex,bmi=bmi,children=children,smoker=smoker,region=region)

        dataframe=user_data.create_data_frame()
        pred_obj=PredictPipeline()
        prediction=pred_obj.predict_data(dataframe)

        result=round(prediction[0],2)

        return render_template("index.html",prediction_text=f"Predicted Insurance Charges: {result}")

if __name__=="__main__":
      app.run(debug=True)










