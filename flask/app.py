import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER=os.environ.get('POSTGRES_USER'),
        DB_PASS=os.environ.get('POSTGRES_PASSWORD'),
        DB_ADDR=os.environ.get('POSTGRES_ADDRESS'),
        DB_NAME=os.environ.get('POSTGRES_DB')
    )

db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
    
    return render_template('index.html', users = User.query.all())


if __name__ == "__main__":
    app.run(debug=True)
