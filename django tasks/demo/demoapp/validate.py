import re
from datetime import datetime, date
from django.core.exceptions import ValidationError

class Validate:
    reason = ""
    def validate_text(self, text):
        if not  re.match("^[A-Za-z ]+$", text):
            raise ValidationError("Invalid Input")

    def validate_gns(self, gen, nationality, state):
        """validating nationality state"""
        states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
                      "Chhattisgarh", "Karnataka", "Madhya Pradesh",
                      "Odisha", "Tamil Nadu", "Telangana", "West Bengal"]
        if gen not in ["male", "female","Male","Female","MALE","FEMALE"]:
            raise ValidationError('Gender is not appropriate')
        if nationality not in ("Indian", "American"):
            self.reason += " nationality not matched "
        if state not in states:
            self.reason += " State not matched "

    def validate_pin(self, pin):
        """validate pin"""
        reg = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
        p = re.compile(reg)
        m = re.match(p, pin)
        if m is None or len(pin)>6:
            raise ValidationError(' Invalid pin')

    def validate_salary(self, salary):
        """validate salary"""
        if not 10000<=int(salary)<=90000:
            self.reason += "salary not matched "

    def validate_pan(self, pan):
        """validate pan """
        reg = "[A-Za-z]{5}[0-9]{4}[A-Za-z]{1}"
        p = re.compile(reg)
        if not (re.search(p, pan) and len(pan) == 10):
            self.reason += " Invalid PAN "

    def validate_age(self, dob, gen):
        """validate age """
        y,m,d = map(int, dob.split("-"))
        bday = date(y,m,d)
        today = date.today()
        age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
        if age < 18 and gen == "female":
            self.reason += " Age not matched "
        if age < 21 and gen == "male":
            self.reason += " Age not matched "

    def return_status(self):
        return self.reason
