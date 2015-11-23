from flask import Flask
import admin.server as admin
app = Flask(__name__)
app.register_blueprint(admin.admin, url_prefix='/admin')