from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/dbqd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Country(db.Model):
    cname = db.Column(db.String(50), primary_key = True)
    population = db.Column(db.Integer)

    def __init__(self, cname, population):
        self.cname = cname
        self.population = population



@app.route('/')

def Index():
    all_data = Country.query.all()
    return render_template("index.html", country = all_data)



@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        cname1 = request.form['cname']
        population1 = request.form['population']

        my_data = Country(cname1, population1)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('Index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():
    
        if request.method == 'POST':
       
                my_data= Country.query.get(request.form.get('cname'))      
                my_data.cname = request.form['cname']
                my_data.population = request.form['population']          
                db.session.commit()
                flash('Country updated succesfully')

                return redirect(url_for('Index'))

@app.route('/delete/<cname>/', methods = ['GET', 'POST'])
def delete(cname):
    my_data = Country.query.get(cname)
    db.session.delete(my_data)
    db.session.commit()
    flash("Country was deleted successfully")
    return redirect(url_for('Index'))


    ############################





if __name__ =="__main__":
    app.run(debug = True)

