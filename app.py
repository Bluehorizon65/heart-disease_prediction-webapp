import pandas as pd

from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)


clf_remake = joblib.load('classifier.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
     
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        restecg = int(request.form['restecg'])
        exang = int(request.form['exang'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        data = {
            'sex': [sex],
            'cp': [cp],
            'restecg': [restecg],
            'exang': [exang],
            'slope': [slope],
            'ca': [ca],
            'thal': [thal]
        }

        input_data = pd.DataFrame(data)

     
        prediction = clf_remake.predict(input_data)[0]
        if prediction:
            prediction1="The person has heart disease !"
        else:
            prediction1="The person does not have heart disease"

        return render_template('heart.html', prediction=prediction1)

    return render_template('heart.html')

if __name__ == '__main__':
    app.run()
