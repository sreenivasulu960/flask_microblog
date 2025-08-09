"""
Microblog Application Entry Point

This script serves as the main entry point for the Microblog Flask application when run
using the Flask command-line interface. By setting the FLASK_APP environment variable to
this file, Flask will use this module to locate and run the application instance.

The script imports the app instance from the app package, which was created and configured
in the application's initialization module. This follows Flask's application factory pattern,
separating the application creation from the code that runs it.
"""
from app import app