from flask import Flask,render_template


app=Flask(__name__)



@app.route("/homePage")
@app.route("/")
def getStart():
    return render_template('homePage.html',title='Home')


@app.route("/")
@app.route("/loginPage")
def login():
    return render_template('loginPage.html',title='Login')

@app.route("/loginPage")
@app.route("/mainMenu")
def mainMenu():
    return render_template('mainmenu.html',title='Main Menu')
  


@app.route("/") 
@app.route("/quizmenu")
def quizMenu():
    return render_template('quizmenu.html',title='Quiz Menu')

@app.route("/") 
@app.route("/createQuestion")
def createQuizQuestion():
    return render_template('createQuestion.html',title='Create Quiz Question')

@app.route("/") 
@app.route("/questionSummary")
def questionSummary():
    return render_template('questionSummary.html',title='Question Summary')

@app.route("/") 
@app.route("/reportSummary")
def reportSummary():
    return render_template('reportSummary.html',title='Report Summary')

if __name__=='__main__':
    app.run(debug=True) 
