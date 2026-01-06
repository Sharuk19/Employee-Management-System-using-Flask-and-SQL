from flask import Flask, render_template, request, redirect, url_for
from models import db, Employee

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database with app
db.init_app(app)


# -----------------------
# Landing Page (Front UI)
# -----------------------
@app.route("/")
def landing():
    return render_template("landing.html")


# -----------------------
# Dashboard (Employee List)
# -----------------------
@app.route("/dashboard")
def dashboard():
    employees = Employee.query.all()
    return render_template("index.html", employees=employees)


# -----------------------
# Add Employee
# -----------------------
@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        new_employee = Employee(
            name=request.form["name"],
            email=request.form["email"],
            department=request.form["department"],
            role=request.form["role"]
        )

        db.session.add(new_employee)
        db.session.commit()

        return redirect(url_for("dashboard"))

    return render_template("add_employee.html")

@app.route("/edit/<int:emp_id>", methods=["GET", "POST"])
def edit_employee(emp_id):
    employee = Employee.query.get_or_404(emp_id)

    if request.method == "POST":
        employee.name = request.form["name"]
        employee.email = request.form["email"]
        employee.department = request.form["department"]
        employee.role = request.form["role"]

        db.session.commit()
        return redirect(url_for("dashboard"))

    return render_template("edit_employee.html", employee=employee)

# -----------------------
# App Entry Point
# -----------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)