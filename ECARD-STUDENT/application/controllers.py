from flask import Flask, render_template, redirect, request
from flask import current_app as app #it refers to the app object created

from .models import * #both resides in same folder

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        this_user = User.query.filter_by(username=username).first()
        if this_user:
            if this_user.password == pwd:
                if this_user.type == "admin":
                    return render_template("admin_dash.html", this_user=this_user)
                else:
                    return render_template("user_dash.html", this_user=this_user)
            else:
                return "password is incorrect"
        else:
            return "user does not exist"
        return "logged in successfully"
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        pwd=request.form.get("pwd")
        this_user = User.query.filter_by(username=username).first()
        if this_user:
            return "user already exists"
        else:
            new_user = User(username=username, email=email, password=pwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")
    
    return render_template("register.html")

@app.route("/register_card/<int:user_id>", methods=["GET", "POST"])
def request_card(user_id):
    if request.method == "POST":
        card = request.form.get("card")
        return redirect(f"/request/{card}/{user_id}")
        # if card == "adhar":
        #     return render_template("adhar.html", user_id=user_id)
    return render_template("select.html", user_id=user_id)

@app.route("/request/<card>/<int:user_id>")
def card_details(card,user_id):
    this_user= User.query.filter_by(id=user_id).first()
    if card == adhar:
        if request.method == "POST":
            fullname = request.form.get("fullname")
            f_name = request.form.get("f_name")
            gender = request.form.get("gender")
            dob = request.form.get("dob")
            address = request.form.get("address")
            image = request.form.get("image")
            info1 = Info(atr_name="fullname", atr_value=fullname, c_name=card, user_id=user_id)
            info2 = Info(atr_name="f_name", atr_value=f_name, c_name=card, user_id=user_id)
            info3 = Info(atr_name="gender", atr_value=gender, c_name=card, user_id=user_id)
            info4 = Info(atr_name="dob", atr_value=dob, c_name=card, user_id=user_id)
            info5 = Info(atr_name="address", atr_value=address, c_name=card, user_id=user_id)
            info6 = Info(atr_name="image", atr_value=image, c_name=card, user_id=user_id)
            info7 = Info(atr_name=="status", atr_value="requested", c_name=card, user_id=user_id)
            db.session.add_all([info1, info2, info3, info4, info5, info6, info7])
            db.session.commit()
            return render_template("user_dash.html", this_user=this_user)
        return render_template("adhar.html", user_id=user_id)

    elif card== "pan":
        if request.method=="POST":
            fullname = request.form.get("fullname")
            f_name = request.form.get("f_name")
            dob = request.form.get("dob")
            address = request.form.get("address")
            info1 = Info(atr_name="fullname", atr_value=fullname, c_name=card, user_id=user_id)
            info2 = Info(atr_name="f_name", atr_value=f_name, c_name=card, user_id=user_id)
            info3 = Info(atr_name="dob", atr_value=dob, c_name=card, user_id=user_id)
            info4 = Info(atr_name="address", atr_value=address, c_name=card, user_id=user_id)
            info5 = Info(atr_name=="status", atr_value="requested", c_name=card, user_id=user_id)
            db.session.add_all([info1, info2, info3, info4, info5])
            db.session.commit()
            return render_template("user_dash.html", this_user=this_user)

        return render_template("pan.html", user_id=user_id)
    elif card=="driving":
        if request.method=="POST":
            fullname = request.form.get("fullname")
            f_name = request.form.get("f_name")
            dob = request.form.get("dob")
            address = request.form.get("address")
            pin = request.formget("pin")
            image = request.form.get("image")

            info1 = Info(atr_name="fullname", atr_value=fullname, c_name=card, user_id=user_id)
            info2 = Info(atr_name="f_name", atr_value=f_name, c_name=card, user_id=user_id)
            info3 = Info(atr_name="dob", atr_value=dob, c_name=card, user_id=user_id)
            info4 = Info(atr_name="address", atr_value=address, c_name=card, user_id=user_id)
            info5 = Info(atr_name="status", atr_value="requested", c_name=card, user_id=user_id)
            info6 = Info(atr_name="image", atr_value=image, c_name=card, user_id=user_id)
            info7 = Info(atr_name="pin", atr_value=pin, c_name=card, user_id=user_id)

            db.session.add_all([info1, info2, info3, info4, info5, info6, info7])
            db.session.commit()
            return render_template("user_dash.html", this_user=this_user)

        return render_template("driving.html", user_id=user_id)
    
    elif card=="election":
        if request.method=="POST":
            fullname = request.form.get("fullname")
            w_name = request.form.get("w_name")
            dob = request.form.get("dob")
            gender = request.form.get("gender")
            pin = request.formget("pin")
            image = request.form.get("image")
            info1 = Info(atr_name="fullname", atr_value=fullname, c_name=card, user_id=user_id)
            info2 = Info(atr_name="w_name", atr_value=w_name, c_name=card, user_id=user_id)
            info3 = Info(atr_name="dob", atr_value=dob, c_name=card, user_id=user_id)
            info4 = Info(atr_name="gender", atr_value=gender, c_name=card, user_id=user_id)
            info5 = Info(atr_name="status", atr_value="requested", c_name=card, user_id=user_id)
            info6 = Info(atr_name="image", atr_value=image, c_name=card, user_id=user_id)
            info7 = Info(atr_name="pin", atr_value=pin, c_name=card, user_id=user_id)

            db.session.add_all([info1, info2, info3, info4, info5, info6, info7])
            db.session.commit()
            return render_template("user_dash.html", this_user=this_user)
        return render_template("voter.html", user_id=user_id)
    
