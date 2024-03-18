from flask import Flask, render_template, request
import joblib
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        review = request.form['review']
    else:
        review = request.args.get('review')
    # review_clean = pp(review)

    model = joblib.load('templates/best_models/knn.pkl')
    

    pred = model.predict([review])
    
    
    if pred == 0:
        sentiment= "This is a NEGATIVE Review"
    else:
        sentiment= "This is a POSITIVE Review"
    
    return render_template('result.html',sentiment=sentiment)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')