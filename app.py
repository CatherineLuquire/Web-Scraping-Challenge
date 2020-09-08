from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars_info = mongo.db.mars_collection.find_one()
    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scrape():
    # mars = mongo.db.mars
    data = scrape_mars.scrape()
    mongo.db.mars_collection.update({}, data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
