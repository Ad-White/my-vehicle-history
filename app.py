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
    vehicles = list(mongo.db.vehicles.find())
    return render_template("home.html", vehicles=vehicles)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    vehicles = list(mongo.db.vehicles.find({"$text": {"$search": query}}))
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
        vehicles = list(mongo.db.vehicles.find())
        return render_template(
            "profile.html", username=username, vehicles=vehicles)
    return redirect(url_for("profile"))


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
            "litre_cc": request.form.get("litre_cc"),
            "year": request.form.get("year"),
            "colour": request.form.get("colour"),
            "current_owner": current_owner,
            "show_my_vehicle": show_my_vehicle,
            "created_by": session["user"]
        }
        mongo.db.vehicles.insert_one(vehicle)
        flash("Vehicle Successfully Added")
        return redirect(url_for("get_vehicles"))

    vehicle_types = mongo.db.vehicle_types.find().sort("vehicle_type", 1)
    return render_template("add_new_vehicle.html", vehicle_types=vehicle_types)


@app.route("/edit_vehicle/<vehicle_id>", methods=["GET", "POST"])
def edit_vehicle(vehicle_id):
    if request.method == "POST":
        current_owner = "yes" if request.form.get("current_owner") else "no"
        show_my_vehicle = "yes" if request.form.get(
            "show_my_vehicle") else "no"

        edit_vehicle = {"$set": {
            "vehicle_type": request.form.get("vehicle_type"),
            "make": request.form.get("make"),
            "model": request.form.get("model"),
            "capacity": request.form.get("capacity"),
            "litre_cc": request.form.get("litre_cc"),
            "year": request.form.get("year"),
            "colour": request.form.get("colour"),
            "current_owner": current_owner,
            "show_my_vehicle": show_my_vehicle,
            "created_by": session["user"]
        }}
        mongo.db.vehicles.update_one(
            {"_id": ObjectId(vehicle_id)}, edit_vehicle)
        flash("Vehicle Successfully Updated")
        return redirect(url_for("get_vehicles"))

    vehicle = mongo.db.vehicles.find_one({"_id": ObjectId(vehicle_id)})

    vehicle_types = mongo.db.vehicle_types.find().sort("vehicle_type", 1)
    return render_template(
        "edit_vehicle.html", vehicle=vehicle, vehicle_types=vehicle_types)


@app.route("/delete_vehicle/<vehicle_id>")
def delete_vehicle(vehicle_id):
    mongo.db.vehicles.delete_one({"_id": ObjectId(vehicle_id)})
    flash("Vehicle Successfully Deleted")
    return redirect(url_for("get_vehicles"))


@app.route("/get_vehicle_types")
def get_vehicle_types():
    vehicle_types = list(mongo.db.vehicle_types.find().sort("vehicle_make", 1))
    return render_template("vehicle_types.html", vehicle_types=vehicle_types)


@app.route("/add_vehicle_type", methods=["GET", "POST"])
def add_vehicle_type():
    if request.method == "POST":
        vehicle_type = {
            "vehicle_type": request.form.get("vehicle_type")
        }
        mongo.db.vehicle_types.insert_one(vehicle_type)
        flash("New Vehicle Type Added")
        return redirect(url_for("get_vehicle_types"))

    return render_template("add_vehicle_types.html")


@app.route("/edit_vehicle_type/<vehicle_type_id>", methods=["GET", "POST"])
def edit_vehicle_type(vehicle_type_id):
    if request.method == "POST":
        edit_type = {"$set": {
            "vehicle_type": request.form.get("vehicle_type")
        }}
        mongo.db.vehicle_types.update_one(
            {"_id": ObjectId(vehicle_type_id)}, edit_type)
        flash("Vehicle Type Updated")
        return redirect(url_for("get_vehicle_types"))

    vehicle_type = mongo.db.vehicle_types.find_one(
        {"_id": ObjectId(vehicle_type_id)})
    return render_template("edit_vehicle_type.html", vehicle_type=vehicle_type)


@app.route("/delete_vehicle_type/<vehicle_type_id>")
def delete_vehicle_type(vehicle_type_id):
    mongo.db.vehicle_types.delete_one({"_id": ObjectId(vehicle_type_id)})
    flash("Vehicle Type Deleted")
    return redirect(url_for("get_vehicle_types"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
