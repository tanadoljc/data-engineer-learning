from pydantic import BaseModel, Field, computed_field

class order(BaseModel):
    id: int = Field(..., description="The unique identifier for the order")
    unit_price: float = Field(..., description="The price per unit")
    amount: int = Field(..., description="The quantity of items ordered")

    @computed_field
    @property
    def total_price(self) -> float:
        return self.unit_price * self.amount
    
pyd_ins = order(**{
    "id": 1,
    "unit_price": 10.0,
    "amount": 5
})

print(pyd_ins)