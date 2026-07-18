from flask import Blueprint, request, jsonify

from models import db, Employee

employee_bp = Blueprint("employee", __name__)


# Create
@employee_bp.route("/employees", methods=["POST"])
def create_employee():

    data = request.get_json()

    employee = Employee(
        name=data["name"],
        email=data["email"],
        department=data["department"],
        salary=data["salary"]
    )

    db.session.add(employee)

    db.session.commit()

    return jsonify(employee.to_dict()), 201


# Read All
@employee_bp.route("/employees", methods=["GET"])
def get_employees():

    employees = Employee.query.all()

    return jsonify([emp.to_dict() for emp in employees])


# Read One
@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):

    employee = Employee.query.get_or_404(id)

    return jsonify(employee.to_dict())


# Update
@employee_bp.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    employee = Employee.query.get_or_404(id)

    data = request.get_json()

    employee.name = data.get("name", employee.name)
    employee.email = data.get("email", employee.email)
    employee.department = data.get("department", employee.department)
    employee.salary = data.get("salary", employee.salary)

    db.session.commit()

    return jsonify(employee.to_dict())


# Delete
@employee_bp.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)

    db.session.commit()

    return jsonify({"message": "Employee deleted successfully"})
