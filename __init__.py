from flask import Flask
import admin.server
app = Flask(__name__)
app.register_blueprint(admin.server.bp, url_prefix='/admin')