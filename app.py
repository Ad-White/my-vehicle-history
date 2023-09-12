import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_vehicles")
def get_vehicles():
    vehicles = mongo.db.vehicles.find()
    return render_template("home.html", vehicles=vehicles)


# registration functionality
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration has been successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check that hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("sign_in"))


@app.route("/sign_out")
def sign_out():
    # remove user from session cookies
    flash("You have been successfully signed out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/add_new_vehicle", methods=["GET", "POST"])
def add_new_vehicle():
    if request.method == "POST":
        current_owner = "yes" if request.form.get("current_owner") else "no"
        show_my_vehicle = "yes" if request.form.get(
            "show_my_vehicle") else "no"
        vehicle = {
            "vehicle_type": request.form.get("vehicle_type"),
            "make": request.form.get("make"),
            "model": request.form.get("model"),
            "capacity": request.form.get("capacity"),
            "year": request.form.get("year"),
            "colour": request.form.get("colour"),
            "current_owner": current_owner,
            "show_my_vehicle": show_my_vehicle,
            "created_by": session["user"]
        }
        mongo.db.cars.insert_one(vehicle)
        flash("Vehicle Successfully Added")
        return redirect(url_for("get_vehicles"))

    vehicles = mongo.db.vehicle_types.find().sort("vehicle_type", 1)
    return render_template("add_new_vehicle.html", vehicles=vehicles)


@app.route("/edit_vehicle/<vehicle_id>", methods=["GET", "POST"])
def edit_vehicle(vehicle_id):
    vehicle = mongo.db.vehicles.find_one({"_id": ObjectId(vehicle_id)})

    vehicles = mongo.db.vehicles.find().sort("vehicle_type", 1)
    return render_template(
        "edit_vehicle.html", vehicle=vehicle, vehicles=vehicles)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
