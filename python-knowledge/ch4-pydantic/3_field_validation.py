from pydantic import BaseModel, Field, field_validator
from typing import Optional

class personal_info(BaseModel):
    name: str = Field(..., min_length=3, max_length=20, description="The full name of the person")
    age: Optional[int] = Field(..., gt=0, description="Age must be a positive integer")
    email: str = Field(..., title="Email Address")
 
    @field_validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Invalid email address')
        if '.com' not in value:
            value = value + '.com'
        return value
    
pyd_ins = personal_info(**{
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example"
})

print(pyd_ins)