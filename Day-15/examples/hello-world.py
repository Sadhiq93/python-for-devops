from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run("0.0.0.0")

-------------------
# or

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello world'
app.run('0.0.0.0', 5001)

--------------------
note: flask automatically open servive for access
browse:
for <ip>:5001/
hello world


for others as ip:5001/app

Not Found

The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
------------------------


1. Import Flask


from flask import Flask
* This line imports the Flask class from the flask package.
* Flask is the main class used to create a web application.

2. Create a Flask Application Instance


app = Flask(__name__)
* This creates an instance of the Flask application.
* The argument __name__ tells Flask where to look for resources like templates and static files.
* Basically, it helps Flask know the location of your app.

3. Define a Route


@app.route('/')
def hello_world():
    return 'Hello, World!'
* @app.route('/') is a decorator that tells Flask: “When someone visits the root URL (/), run the function below.” 
* The function hello_world() runs whenever someone goes to your homepage.
* Whatever the function returns (in this case, the string 'Hello, World!') is what the user’s browser will display.

4. Run the App


if __name__ == '__main__':
    app.run("0.0.0.0")
* This means: only run the app if this file is executed directly (not imported as a module).
* app.run("0.0.0.0") starts the built-in Flask development server.
    * "0.0.0.0" tells Flask to make the app accessible on all network interfaces (so you can access it from your browser or even another device on the same Wi-Fi).
    * By default, it runs on port 5000 — so your app will be at:  

http://127.0.0.1:5000
or if you’re on the same network:


    * http://<your-computer’s-IP>:5000
    *   

🧠 Optional Tip: Run the App
If your file is named myapp.py, run:


python3 myapp.py
Then open a browser and visit:


http://127.0.0.1:5000
You’ll see:


Hello, World!

