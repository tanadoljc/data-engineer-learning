from pydantic import BaseModel, Field, model_validator

class API_auth(BaseModel):
    email: str = Field(..., title="Email Address")
    password: str = Field(..., min_length=8, max_length=20, description="Password must be between 8 and 20 characters")
    confirm_password: str = Field(..., min_length=8, max_length=20, description="Confirm Password must be between 8 and 20 characters")

    @model_validator(mode='after')
    def check_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self
    
pyd_ins = API_auth(**{ 
    "email": "john.doe@example.com",
    "password": "password123",
    "confirm_password": "password122"
})

print(pyd_ins)