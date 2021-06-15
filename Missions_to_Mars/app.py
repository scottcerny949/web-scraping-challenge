from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_info = mongo.db.listings.find_one()
    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scrape():
    mars_info = scrape_mars.scrape()
    mongo.db.collection.update({}, mars_info, upsert=True)
    return redirect("/")

@app.route("/scraper")
def scraper():
    mars_info= mongo.db.mars_info
    mars_data = scrape_mars.scrape()
    mars_info.update({}, mars_data, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)