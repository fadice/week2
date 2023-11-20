
from flask import Flask, render_template, request
import numpy as np
import pickle
#import joblib
app = Flask(__name__)
filename = 'file_cancer.pkl'
model = pickle.load(open(filename, 'rb'))    # load the model
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])  # The user input is processed here
def predict():
    uniformity_cell_size = request.form['uniformity_cell_size']
    uniformity_cell_shape = request.form['uniformity_cell_shape']
    marginal_adhesion = request.form['marginal_adhesion']
    bland_chromatin = request.form['bland_chromatin']
    normal_nucleoli= request.form['normal_nucleoli']
    pred = model.predict(np.array([[2, 3, 4, 5, 2 ]]).astype(float))[0]
    #print(pred)
    return render_template('index.html', predict=str(pred))
if __name__ == '__main__':
    app.run(debug=True)
