# improt the flask library
# Create the application instance
# URL route "/" as default route
# function index() is called when the URL is accessed
# Entry point for the application
# Start the app server
# The only information going back to the browser is what is returned from the function --


from flask import Flask
app = Flask(__name__) 

@ app.route("/")
def index():
    return "<h1> Dynamically Generated Home Page </h1> <p> First Flask App </p>"

# /greet rout - pass name as parameter
# be sure to use return 'f' to return the function output instead of a string
@ app.route('/greet/<name>')
def greet(name):                        
    return f"<h1> Greetings {name} </h1> <p> You are probably a turd </p>"


    ########## Entry point for the application ##########
    
if __name__ == "__main__":
    app.run()

    ####### Start Python app with the above code #######