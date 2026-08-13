import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["orders", "products", "customers", "reviews", "cancels"]

def my_func(i):
    wait = random.randint(1,10)
    time.sleep(wait)
    print(f"I am {i}, I took {wait} seconds")

with ThreadPoolExecutor(max_workers=len(tables)) as executor:
    executor.map(my_func, tables)