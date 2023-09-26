import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env

# application configuration settings
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# cloudinary configuration settings
cloudinary.config(
    cloud_name=os.environ.get("CLOUD_NAME"),
    api_key=os.environ.get("API_KEY"),
    api_secret=os.environ.get("API_SECRET")
)


@app.route("/")
@app.route("/show_vehicles")
def show_vehicles():
    """
    Returns and displays all vehicles from the database, to
    the show vehicles page.
    """
    vehicles = list(mongo.db.vehicles.find())
    return render_template("show_vehicles.html", vehicles=vehicles)


# search functionality
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Searches for matching resuluts from the query input on
    the show vehicles page.
    """
    query = request.form.get("query")
    vehicles = list(mongo.db.vehicles.find({"$text": {"$search": query}}))
    return render_template("show_vehicles.html", vehicles=vehicles)


# registration functionality
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Checks the username against the database for any existing entries.
    User is notified if there is a match, and asked to try again.
    If username is accepted, the username and password are stored and
    a session cookie is created.
    """
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, Username already exists. Please try another")
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
    """
    Checks the existing username and password against the database.
    If either are invalid the user is notified.
    If username and password are valid, the user is signed-in
    to the site.
    """
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


@app.route("/sign_out")
def sign_out():
    """
    The user is signed-out upon request, and notified
    of the action.
    The cookie session is destroyed.
    The user is then returned to the sign-in page.
    """
    flash("You have been successfully signed out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Returns and displays all vehicles for the user in session
    from the database. Displaying on the Profile page.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        vehicles = list(mongo.db.vehicles.find())
        return render_template(
            "profile.html", username=username, vehicles=vehicles)
    return redirect(url_for("profile"))


@app.route("/add_new_vehicle", methods=["GET", "POST"])
def add_new_vehicle():
    """
    The user can add a new vehicle with information, and the users
    own image (using the Cloudinary API), to the database.
    """
    if request.method == "POST":
        current_owner = "yes" if request.form.get("current_owner") else "no"
        show_my_vehicle = "yes" if request.form.get(
            "show_my_vehicle") else "no"

        image = request.files["image"]
        image_upload = cloudinary.uploader.upload(image)

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
            "created_by": session["user"],
            "image_url": image_upload['secure_url'],
            "description": request.form.get("description").strip()
        }
        mongo.db.vehicles.insert_one(vehicle)
        flash("Vehicle Successfully Added")
        return redirect(url_for("show_vehicles"))

    vehicle_types = mongo.db.vehicle_types.find().sort("vehicle_type", 1)
    return render_template("add_new_vehicle.html", vehicle_types=vehicle_types)


@app.route("/edit_vehicle/<vehicle_id>", methods=["GET", "POST"])
def edit_vehicle(vehicle_id):
    """
    The user can edit any vehicle information and the users
    own image (using the Cloudinary API), and save changes
    to the database.
    Returns the user to the show vehicles page.
    """
    if request.method == "POST":
        current_owner = "yes" if request.form.get("current_owner") else "no"
        show_my_vehicle = "yes" if request.form.get(
            "show_my_vehicle") else "no"

        image = request.files["image"]
        image_upload = cloudinary.uploader.upload(image)

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
            "created_by": session["user"],
            "image_url": image_upload['secure_url'],
            "description": request.form.get("description").strip()
        }}
        mongo.db.vehicles.update_one(
            {"_id": ObjectId(vehicle_id)}, edit_vehicle)
        flash("Vehicle Successfully Updated")
        return redirect(url_for("show_vehicles"))

    vehicle = mongo.db.vehicles.find_one({"_id": ObjectId(vehicle_id)})

    vehicle_types = mongo.db.vehicle_types.find().sort("vehicle_type", 1)
    return render_template(
        "edit_vehicle.html", vehicle=vehicle, vehicle_types=vehicle_types)


@app.route("/delete_vehicle/<vehicle_id>")
def delete_vehicle(vehicle_id):
    """
    Upon user confirmation this deletes the vehicle from the database
    with the assocciated vehicle id.
    Notifies the user when action is complete.
    """
    mongo.db.vehicles.delete_one({"_id": ObjectId(vehicle_id)})
    flash("Vehicle Successfully Deleted")
    return redirect(url_for("show_vehicles"))


# manage vehicle types - Admin only
@app.route("/get_vehicle_types")
def get_vehicle_types():
    """
    Returns and displays all vehicle types from the database.
    """
    vehicle_types = list(mongo.db.vehicle_types.find().sort("vehicle_make", 1))
    return render_template("vehicle_types.html", vehicle_types=vehicle_types)


@app.route("/add_vehicle_type", methods=["GET", "POST"])
def add_vehicle_type():
    """
    The Admin user can add a new vehicle type and
    save this to the database.
    """
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
    """
    The Admin user can edit a vehicle type and
    save this to the database.
    """
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
    """
    Upon Admin confirmation to delete.
    This deletes the vehicle type from the database with
    the assocciated vehicle type id.
    Notifies the user when action is complete.
    """
    mongo.db.vehicle_types.delete_one({"_id": ObjectId(vehicle_type_id)})
    flash("Vehicle Type Deleted")
    return redirect(url_for("get_vehicle_types"))


# Error handlers for 404 and 500 page responces
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
