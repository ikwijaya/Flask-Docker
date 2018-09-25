# importing depedencies
from flask import Flask

# variable register void()
app = Flask(__name__)

# App Run ================================================================================================================================
if __name__ == '__main__':
  app.run(debug=True,port=8088)
