from flask import *
import sqlite3
import smtplib
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("Aboutus.html")


@app.route("/kapcsolat")
def kapcs():
    return render_template("kapcsolat.html")


@app.route("/munkatarsaink")
def mun():
    return render_template("Munkatársaink.html")


@app.route("/index")
def ind():
    return render_template("index.html")


@app.route("/Szolgaltatasok")
def szol():
    return render_template("Szolgaltatasok.html")


@app.route("/newsletter")
def news():
    return render_template("newsletter.html")


@app.route("/allsafe")
def safe():
    return render_template("Allsafe.html")


@app.route("/fsociety")
def f():
    return render_template("fsociety.html")


@app.route("/career")
def job():
    return render_template("career.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            with sqlite3.connect("employee.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Sub (name, email) values (?,?)", (name, email))
                con.commit()
                msg = "Employee successfully Added"
        except:
            con.rollback()
            msg = "We can not add the employee to the list"
        finally:
            return render_template("index.html", msg=msg)
            con.close()


MY_EMAIL = "ecorpbusiness1@gmail.com"
PASSWORD = "RcX$C2sn"


@app.route("/kapcsolat", methods=["POST", "GET"])
def mail():
    msg = "msg"
    if request.method == "POST":
        try:
            message = request.form["message"]
            email = request.form["email"]
            subject = request.form["subject"]

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                                    msg=f"Subject:ECorp Business \n\n We receive your email. Our colleagues will respond soon.")
                connection.sendmail(from_addr=MY_EMAIL, to_addrs="snollygoster706@gmail.com",
                                    msg=f"Subject:{subject} \n\n {message}")

        finally:
            return render_template("index.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
