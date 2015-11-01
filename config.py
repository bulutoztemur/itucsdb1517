from flask import Flask
import admin.server as admin
app = Flask(__name__)
app.register_blueprint(admin.bp, url_prefix='/admin')