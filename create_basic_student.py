import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DangoDBForWinforms.settings")
django.setup()

from DangoDBApp.models import TblStudentBasicInfoApplications

sample_data = [
    {
        "first_name": "John",
        "middle_name": None,
        "last_name": "Doe",
        "suffix": None,
        "is_transferee": False,
        "contact_number": "09123456789",
        "year_level": "1st year",
        "address": "123 Main St, Anytown",
        "campus": "Mandaue Campus",
        "program": "BSIT",
        "birth_date": "2000-01-15",
        "sex": "Male",
        "email": "johndoe@example.com",
        "status": "pending", 
        "active": True,
    },
    {
        "first_name": "Jane",
        "middle_name": None,
        "last_name": "Smith",
        "suffix": None,
        "is_transferee": False,
        "contact_number": "09198765432",
        "year_level": "2nd year",
        "address": "456 Elm St, Othertown",
        "campus": "Cebu Campus",
        "program": "BSTM",
        "birth_date": "1999-05-22",
        "sex": "Female",
        "email": "janesmith@example.com",
        "status": "pending",  
        "active": True,
    },
    {
        "first_name": "Mike",
        "middle_name": None,
        "last_name": "Johnson",
        "suffix": None,
        "is_transferee": False,
        "contact_number": "09234567890",
        "year_level": "3rd year",
        "address": "789 Oak St, Differenttown",
        "campus": "Mandaue Campus",
        "program": "BSIT",
        "birth_date": "2001-09-10",
        "sex": "Male",
        "email": "mikejohnson@example.com",
        "status": "pending", 
        "active": True,
    },
]

for data in sample_data:
    TblStudentBasicInfoApplications.objects.create(
        first_name=data["first_name"],
        middle_name=data["middle_name"],
        last_name=data["last_name"],
        suffix=data["suffix"],
        is_transferee=data["is_transferee"],
        contact_number=data["contact_number"],
        year_level=data["year_level"],
        address=data["address"],
        campus=data["campus"],
        program=data["program"],
        birth_date=datetime.strptime(data["birth_date"], "%Y-%m-%d").date(),
        sex=data["sex"],
        email=data["email"],
        status=data["status"],  # Corrected field name
        active=data["active"],
    )

print("Data inserted successfully!")
