from pydantic import BaseModel, Field

class input(BaseModel):
    query: str = Field(..., description="The search query string")

class output(BaseModel):
    query: str = Field(..., description="The search query string")
    results: str = Field(..., description="The str of search results")

def process_data(param: input) -> output:

    query_input = param.query
    result = "Good Job Bro!"

    return output(**{
        "query": query_input,
        "results": result
    })

input_query = input(**{"query": "Hello World!"})

response = process_data(input_query)

# Pydantic
print(response)
print("-----------------------------")
# Pydantic to Dict
print(response.model_dump())
print("-----------------------------")
# Pydantic to JSON
print(response.model_dump_json())

