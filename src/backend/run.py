# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # the flask app run in 5000 port by default 
