from flask import Flask, render_template, request, redirect, url_for, jsonify
import pickle
import os


app = Flask(__name__)
# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "linear.pkl")

# Load the model using the absolute file path
with open("linear.pkl", "rb") as f:
    model2 = pickle.load(f)

@app.route("/")
def home():
    return render_template("AQI.html")


@app.route('/predict', methods=["POST"])
def predict():
    try:
        PM25 = request.form['PM2.5']
        PM10 = request.form['PM10']
        NO = request.form['NO']
        NO2 = request.form['NO2']
        NOx = request.form['NOx']
        NH3 = request.form['NH3']
        CO = request.form['CO']
        SO2 = request.form['SO2']
        O3 = request.form['O3']
        Benzene = request.form['Benzene']
        Toluene = request.form['Toluene']
        Xylene = request.form['Xylene']

        #Predict using the loaded model 
        result = model2.predict([PM25,PM10,NO,NO2,NOx,NH3,CO,SO2,O3,Benzene,Toluene,Xylene])

        return jsonify({"prediction:prediction[0]"})

        return render_template("AQI.html", result='{}'.format(result))
    except Exception as e:
        return jsonify({"error":str(e)})


if __name__ == "__main__":
    app.run(debug=True)