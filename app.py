from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
  username = os.getenv('USERNAME')
  email = os.getenv('EMAIL')
  password = os.getenv('PASSWORD')

  print(username,email,password) 

  return '<h1>Mi prima applicacion Flask deployeada en Render<br>{}<br>{}<br>{}<br></h1>'.format(username,email,password) ,200




def status_404():
  return '<h1>404 not found</h1>'

app.register_error_handler(404, status_404)

if __name__ == '__main__':
  app.run(debug=True)