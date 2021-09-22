from flask import Flask
import dbCreate

# the all-important app variable:
app = Flask(__name__)

@app.route("/<name>")
def create_database(name):
    out=dbCreate.createDB(name)
    print (out)
    return out

@app.route("/")
def start():
    dbCreate.createDB("test2")
    return """
    <h1 style='text-align: center; color: blue;'>Welcome to Python Script</h1>
    <p>The script helps in creating Datasbase in postgres SQL.</p>
    <p>URL should be followed by Database Name <em>http://localhost/testDB</em></code>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
