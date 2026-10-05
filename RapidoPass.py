import random
from datetime import date

# ---------------- Parent Class ----------------
class Person:
    def __init__(self, name, age, phone, is_student):
        self.name = name
        self.age = age
        self.phone = phone
        self.is_student = is_student


# ---------------- Child Class ----------------
class RapidoPass(Person):
    def __init__(self, name, age, phone, is_student, vehicle_type, plan_type):
        # Explicit call to parent constructor (NO super())
        Person.__init__(self, name, age, phone, is_student)

        self.vehicle_type = vehicle_type
        self.plan_type = plan_type
        self.user_id = self.generate_user_id()
        self.amount = self.calculate_amount()

    def generate_user_id(self):
        return "RPD" + str(random.randint(100000, 999999))

    def calculate_amount(self):
        # Base price
        if self.plan_type.lower() == "monthly":
            amount = 1200
        elif self.plan_type.lower() == "quarterly":
            amount = 3300
        else:
            amount = 0

        # Vehicle based discount
        if self.vehicle_type.lower() == "bike":
            amount *= 0.85   # 15% discount
        elif self.vehicle_type.lower() == "auto":
            amount *= 0.90   # 10% discount
        elif self.vehicle_type.lower() == "car":
            amount *= 1.00   # no discount

        # Student discount
        if self.is_student:
            amount *= 0.80   # 20% discount

        return int(amount)

    def display_digital_pass(self):
        print("\n========== DIGITAL RAPIDO PASS ==========")
        print(f"User ID        : {self.user_id}")
        print(f"Name           : {self.name}")
        print(f"Age            : {self.age}")
        print(f"Phone          : {self.phone}")
        print(f"Student        : {'Yes' if self.is_student else 'No'}")
        print(f"Vehicle Type   : {self.vehicle_type}")
        print(f"Plan Type      : {self.plan_type}")
        print(f"Amount Paid    : ₹{self.amount}")
        print(f"Issue Date     : {date.today()}")
        print("========================================")
        print("✔ Pass generated successfully")
        print("✔ Saves monthly expenses and time 🚀")


# ---------------- Main Program ----------------
def main():
    print("====== RAPIDO PASS REGISTRATION ======")

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    phone = input("Enter Phone Number: ")
    is_student = input("Are you a student? (yes/no): ").lower() == "yes"

    print("\nSelect Vehicle Type:")
    print("1. Bike")
    print("2. Auto")
    print("3. Car")
    vehicle_choice = input("Enter choice (1/2/3): ")

    if vehicle_choice == "1":
        vehicle_type = "Bike"
    elif vehicle_choice == "2":
        vehicle_type = "Auto"
    else:
        vehicle_type = "Car"

    print("\nSelect Pass Plan:")
    print("1. Monthly")
    print("2. Quarterly")
    plan_choice = input("Enter choice (1/2): ")
    plan_type = "Monthly" if plan_choice == "1" else "Quarterly"

    pass_obj = RapidoPass(
        name, age, phone, is_student, vehicle_type, plan_type
    )

    pass_obj.display_digital_pass()


# Run Program
if __name__ == "__main__":
    main()