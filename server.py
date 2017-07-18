"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
INSULTS = [
    'you\'re ugly and your mother dresses you funny', 
    'you smell like a hot litter box', 
    'no one uses that front end framework anymore!!']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
              <html>
                <a href='http://localhost:5000/hello'</a>
                Hi! This is the home page.
              </html>
              """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    start = """
            <!doctype html>
              <html>
                <head>
                  <title>Hi There!</title>
                </head>
                <body>
                  <h1>Hi There!</h1>
                    <form action="/greet">
                      What's your name? <input type="text" name="person">
            """

    dropdown = 'Choose a compliment: <select name="compliment"> '

    for compliment in AWESOMENESS:
      dropdown += "<option value='{value}'>{compliment}</option> ".format(value=compliment, compliment=compliment)

    dropdown += "</select>"

    end = """
          <input type="submit" value="Submit">
            </form>
              </body>
            </html>
          """

    return start + dropdown + end


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")


    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)

@app.route('/diss')
def our_insults(): 
     """Get user by name."""

    player = request.args.get("person")
    diss = choice(INSULTS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """.format(player=player, diss=diss)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
