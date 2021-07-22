
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model import Dojo,Ninja


#### ---------------- Dojo controller --------- ######

##------------ This displays "All Users" that we have in the DB in the main URL page -------------------##
@app.route("/dojos")
def dojos():
    # call the get all classmethod to get all users
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojo.html", all_dojos= dojos)


##-------------Staging area to process the for submission and save to the database -------------------##
##-------------Redirects to the main page -------------------##
@app.route("/new-dojo", methods=["POST"])
def add_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"]
    }
    # We pass the data dictionary into the save method from the User class.
    Dojo.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')


@app.route("/dojos/<id>")
def single_dojos(id):
    data = {
        "id" :  id
    }
    # call the get all classmethod to get all users
    dojo= Dojo.get_one(data)
    dojo_data = {
        "dojo_id" : id
    }
    dojo.ninjas =  Ninja.get_all_ninjas_by_dojo_id(dojo_data)
    return render_template("dojodetail.html",dojo= dojo)


#### ---------------- NINJA Controller --------- ######

@app.route("/ninjas")
def ninjas():
    # call the get all classmethod to get all users
    dojos = Dojo.get_all()

    return render_template("ninja.html", all_dojos= dojos)

@app.route("/new-ninja", methods=["POST"])
def add_ninja():
    # First we make a data dictionary from our request.form coming from our template.
    request.form['first_name']
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    # We pass the data dictionary into the save method from the User class.
    Ninja.save(data)

    redirect_me = "/dojos/"+ request.form['dojo_id']
    # Don't forget to redirect after saving to the database.
    return redirect(redirect_me)
