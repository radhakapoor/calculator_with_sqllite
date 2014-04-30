from flask import Flask, render_template
import flask
from flask.ext.sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    value_a = db.Column(db.Float)
    calculation = db.Column(db.String)
    value_b = db.Column(db.Float)
    answer = db.Column(db.Float)
    
    def __init__(self, value_a, calculation, value_b, answer):
        self.value_a = value_a
        self.calculation = calculation
        self.value_b = value_b
        self.answer = answer
    
    def __repr__(self):
        return '<Calculation {} {} {} = {}>'.format(self.value_a, self.calculation, self.value_b, self.answer)    
 
@app.route('/', methods=['GET', 'POST'])
def home():         
    if flask.request.method == 'POST':
        value_a = (flask.request.form['value_a'])              
        value_b = (flask.request.form['value_b'])
        if value_a and value_b:
            if flask.request.form['calculate'] == 'add':
                answer = float(value_a) + float(value_b)
                return 'The answer is '+ '{}'.format(answer)              
            elif flask.request.form['calculate'] == 'subtract':
                answer = float(value_a) - float(value_b)
                return 'The answer is ' + '{}'.format(answer)
            elif flask.request.form['calculate'] == 'multiply':
                answer = float(value_a) * float(value_b)
                return 'The answer is ' + '{}'.format(answer)
            elif flask.request.form['calculate'] == 'divide':
                answer = float(value_a) / float(value_b)                 
                return 'The answer is ' + '{}'.format(answer)              
                
            calculation = Calculation(value_a=value_a, calculation=calculation, value_b=value_b, answer=answer)
            db.session.add(calculation)
            db.session.commit()                
        else:
            raise Exception("Please enter two numbers")
            #ValueError does not pick up scenario where user does not select +,-,*,/ or where user enters two non-numbers
                               
    else:
        calculations = Calculation.query.all()       
        return render_template('home.html', calculations=calculations)
#Is it enough to pass in the variable "calculations or do i also need to pass in value_a, value_b etc?"
 
 #db.session.add(is not picking up the relevant calculation)   
   
    
    
    

    
        
        
        
 
if __name__ == '__main__':
    app.run(debug=True)