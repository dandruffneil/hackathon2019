from flask import Flask
#from init import bootstrap_system

app = Flask(__name__)
app.secret_key = 'slackathon'  # Used to add entropy
