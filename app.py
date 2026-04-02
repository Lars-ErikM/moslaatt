from flask import Flask
from views import views

app=Flask(__name__)
app.register_blueprint(views) # url_prefix="/views" Inkluderer /views i url. Nyttig hvis man har flere blueprints

# @app.route('/')
# def index():
#     return 'Hi dude'

# @app.route('/<name>')
# def print_name(name):
#     return 'Hi, Mr. {}'.format(name)

if __name__ == '__main__':
    # app.run(debug=True, port=8000) #Dev mode - Run in terminal with "python app.py"
    app.run(debug=False, port=8000) #Prod mode