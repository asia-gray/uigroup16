from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tripDetails')
def tripDetails():
    return render_template('tripDetails.html')

@app.route('/profilePage')
def profilePage():
    return render_template('profilePage.html')

@app.route('/viewItinerary')
def viewItinerary():
    return render_template('viewItinerary.html')

@app.route('/voteItinerary')
def voteItinerary():
    return render_template('voteItinerary')

@app.route('/chooseActivities.html')
def chooseActivities():
    return render_template('chooseActivities.html')

if __name__ == '__main__':
    app.run(debug=True)