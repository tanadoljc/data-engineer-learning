from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal, List

class personal_info(BaseModel):
    name: str = Field(..., min_length=3, max_length=20, description="The full name of the person")
    age: Optional[int] = Field(..., gt=0, description="Age must be a positive integer")
    email: EmailStr = Field(..., title="Email Address")
    gender: Literal["Male", "Female", "Other"] = Field(..., description="This is gender")
    salaries: List[int] = Field(..., description="This is salaries")

def main(param: personal_info):
    print("Name:", param.name)
    print("Age:", param.age)
    print("Email:", param.email)
    print("Gender:", param.gender)
    print("Salaries:", param.salaries)

pyd_ins = personal_info(**{
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "gender": "Male",
    "salaries": [50000, 60000, 70000]
})

main(pyd_ins)