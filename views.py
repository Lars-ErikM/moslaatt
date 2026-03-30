from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views= Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Lars")

# @views.route("/profile") #Returnerer profil ved (../profile?name=<name>)
# def profile():
#     #args=request.args
#     #name=args.get('name')
#     #return render_template("index.html", name=name)
#     return render_template("profile.html")

# @views.route("/json") #Returnerer Json 
# def get_json():
#     return jsonify({'name':'Lars-Erik', 'born': 1989})

# @views.route("/data")
# def get_data():
#     data=request.json
#     return jsonify(data)

# @views.route("/go_to_home")
# def go_to_home():
#     return redirect(url_for("views.home"))