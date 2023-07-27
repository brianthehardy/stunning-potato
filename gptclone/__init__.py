'''
TODO:

- Exception handling in dalle.py
- Fix screen sizing issues
    - Safari sizing issues
- Progressive Web Application
- Chat history
- Dalle history that autoforwards to dump
- Add authentication
- Email or text based system
- Side-by-side comparison


'''


from flask import Flask, request, render_template, session
from dotenv import load_dotenv
import openai, os

load_dotenv()
openai.apiKey = os.getenv('OPENAI_API_KEY')

# Create and configure the app
# This is the application factory function
def create_app( test_config = None ):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = os.getenv("SECRET_KEY")

    # For testing
    # if test_config is None:
    #     # Load the instance config, if it exists, when not testing
    #     app.config.from_pyfile( 'config.py', silent = True )
    # else:
    #     # Load testing config if passed
    #     app.config.from_mapping( test_config )

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # A simple page that says hello
    @app.route ('/hello' )
    def hello():
        return 'Hello, world!'

    from . import dalle
    app.register_blueprint(dalle.bp)

    from . import chat
    app.register_blueprint(chat.bp)

    from . import comparison
    app.register_blueprint(comparison.bp)

    app.add_url_rule('/', endpoint='index')
    # Adds the endpoint 'index' for navigation to '/'.  Not necessary, if we want these to be different
    # This is done because the chat feature is the main feature of our website



    return app