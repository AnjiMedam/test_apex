from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/apex_test_api")
def read_root():
    return [
  {
    "id": 1,
    "personal_details": {
      "first_name": "Alice",
      "last_name": "Johnson",
      "contact": {
        "email": "alice.johnson@example.com",
        "phone": "123-456-7890",
        "address": {
          "street": "123 Main St",
          "city": "Metropolis",
          "state": "CA",
          "zip": "90210"
        }
      }
    },
    "job_information": {
      "position": "Software Engineer",
      "department": {
        "name": "Engineering",
        "department_number": 101
      },
      "projects": [
        {
          "project_id": "P001",
          "project_name": "NextGen AI",
          "roles": ["Developer", "Tester"]
        },
        {
          "project_id": "P002",
          "project_name": "Cloud Migration",
          "roles": ["Lead Developer"]
        }
      ]
    },
    "skills": [
      {
        "skill_name": "Python",
        "level": "Expert"
      },
      {
        "skill_name": "Machine Learning",
        "level": "Advanced"
      }
    ]
  },
  {
    "id": 2,
    "personal_details": {
      "first_name": "Bob",
      "last_name": "Smith",
      "contact": {
        "email": "bob.smith@example.com",
        "phone": "987-654-3210",
        "address": {
          "street": "456 Elm St",
          "city": "Smallville",
          "state": "TX",
          "zip": "75432"
        }
      }
    },
    "job_information": {
      "position": "Product Manager",
      "department": {
        "name": "Product",
        "department_number": 102
      },
      "projects": [
        {
          "project_id": "P003",
          "project_name": "Mobile App Launch",
          "roles": ["Manager"]
        }
      ]
    },
    "skills": [
      {
        "skill_name": "Project Management",
        "level": "Expert"
      },
      {
        "skill_name": "Agile Methodologies",
        "level": "Advanced"
      }
    ]
  }
]

    
  




# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}