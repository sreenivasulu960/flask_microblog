"""
Flask Application Initialization Module

This module initializes the Flask web application, setting up the core application instance
and importing the route handlers. It serves as the main entry point for the web application,
creating the app object that will be used throughout the application's lifecycle.

The module follows Flask's application factory pattern, where the app is instantiated and
then configured with routes, error handlers, and other application components.

@author: vasulu
@version: 0.1
@date: 2025-aug-09
"""
from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
from app import routes

