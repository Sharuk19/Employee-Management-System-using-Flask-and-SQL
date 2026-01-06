from app import app
from models import db, Employee
import random

names = [
    "Arjun", "Rahul", "Karthik", "Vijay", "Suresh", "Ramesh", "Amit",
    "Priya", "Sneha", "Anjali", "Kavya", "Divya", "Meera", "Pooja"
]

departments = ["Engineering", "HR", "Finance", "Operations", "Marketing"]
roles = ["Developer", "Manager", "Analyst", "Engineer", "Coordinator"]

with app.app_context():
    for i in range(1, 101):
        name = random.choice(names)
        employee = Employee(
            name=f"{name} {i}",
            email=f"{name.lower()}{i}@company.com",
            department=random.choice(departments),
            role=random.choice(roles)
        )
        db.session.add(employee)

    db.session.commit()

print("✅ 100 employees added successfully")