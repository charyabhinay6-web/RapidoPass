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
    PLAN_PRICES = {
        "monthly": 1200,
        "quarterly": 3300
    }

    VEHICLE_DISCOUNTS = {
        "bike": 0.15,
        "auto": 0.10,
        "car": 0.00
    }

    def __init__(self, name, age, phone, is_student, vehicle_type, plan_type):
        super().__init__(name, age, phone, is_student)

        self.vehicle_type = vehicle_type
        self.plan_type = plan_type
        self.user_id = self.generate_user_id()
        self.amount = self.calculate_amount()
        self.issue_date = date.today()

    def generate_user_id(self):
        return "RPD" + str(random.randint(100000, 999999))

    def calculate_amount(self):
        amount = self.PLAN_PRICES[self.plan_type.lower()]

        vehicle_discount = self.VEHICLE_DISCOUNTS[self.vehicle_type.lower()]
        amount *= (1 - vehicle_discount)

        if self.is_student:
            amount *= 0.80

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
        print(f"Issue Date     : {self.issue_date}")
        print("========================================")
        print("Pass generated successfully!")
        print("Saves monthly expenses and time.")


# ---------------- Input Functions ----------------
def get_name():
    while True:
        name = input("Enter Name: ").strip()

        if name and all(char.isalpha() or char.isspace() for char in name):
            return name

        print("Please enter a valid name.")


def get_age():
    while True:
        try:
            age = int(input("Enter Age: "))

            if 1 <= age <= 100:
                return age

            print("Age must be between 1 and 100.")

        except ValueError:
            print("Please enter a valid age.")


def get_phone():
    while True:
        phone = input("Enter Phone Number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Please enter a valid 10-digit phone number.")


def get_student_status():
    while True:
        choice = input("Are you a student? (yes/no): ").strip().lower()

        if choice == "yes":
            return True
        elif choice == "no":
            return False

        print("Please enter yes or no.")


def get_vehicle_type():
    while True:
        print("\nSelect Vehicle Type:")
        print("1. Bike")
        print("2. Auto")
        print("3. Car")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            return "Bike"
        elif choice == "2":
            return "Auto"
        elif choice == "3":
            return "Car"

        print("Invalid choice. Please select 1, 2, or 3.")


def get_plan_type():
    while True:
        print("\nSelect Pass Plan:")
        print("1. Monthly")
        print("2. Quarterly")

        choice = input("Enter choice (1/2): ").strip()

        if choice == "1":
            return "Monthly"
        elif choice == "2":
            return "Quarterly"

        print("Invalid choice. Please select 1 or 2.")


# ---------------- Main Program ----------------
def main():
    print("====== RAPIDO PASS REGISTRATION ======")

    name = get_name()
    age = get_age()
    phone = get_phone()
    is_student = get_student_status()
    vehicle_type = get_vehicle_type()
    plan_type = get_plan_type()

    pass_obj = RapidoPass(
        name,
        age,
        phone,
        is_student,
        vehicle_type,
        plan_type
    )

    pass_obj.display_digital_pass()


# ---------------- Run Program ----------------
if __name__ == "__main__":
    main()