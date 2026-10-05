from pydantic import BaseModel, Field, StrictInt

class input(BaseModel):

    x : StrictInt = Field(...,description="this is x")
    y : str = Field(...,description="this is y")


pyd_input = input(**{"x":10, "y":"Most"})

def main(param: input):
    print(f"Hello This is param {param}")

main(pyd_input)