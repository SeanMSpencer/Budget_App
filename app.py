from src import create_app

#prevents the user from invoking a script on import if they don't mean too.
if __name__ == "__main__":   
    app = create_app()
    #Anytime you make a change to codebase it'll restart server while set to true
    app.run(debug = True)

