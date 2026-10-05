from pydantic import BaseModel, Field

class Address(BaseModel):
    street: str = Field(..., description="The street name")
    city: str = Field(..., description="The city name")
    state: str = Field(..., description="The state name")
    country: str = Field(..., description="The country name")
    zip_code: str = Field(..., description="The zip code")

class personal_info(BaseModel):
    name: str = Field(..., description="The person's name")
    age: int = Field(..., description="The person's age")
    email: str = Field(..., description="The person's email address")
    address: Address = Field(..., description="The person's address")

pyd_ins = personal_info(**{
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "address": Address(**{
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "country": "USA",
        "zip_code": "12345"
    })
})

print(pyd_ins)
    