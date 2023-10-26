from flask import Flask

app = Flask( __name__ )

@app.route("/")
def home():
    a = "this is a deploy trial"
    return a

if __name__ == "__main__":
    app.run(debug=True)