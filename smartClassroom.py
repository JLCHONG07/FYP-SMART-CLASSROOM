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

if __name__=='__main__':
    app.run(debug=True) 
