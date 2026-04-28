from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Customer(BaseModel):
    name: str
    email: str


customers_list = [
    Customer(name="Joa", email="joa@gmail.com"),
    Customer(name="Bob", email="bob@gmail.com"),
    Customer(name="Alice", email="alice@gmail.com"),
    Customer(name="Cielo", email="cielo@gmail.com")
]


@app.get("/customers")
def customers():
    return customers_list.copy()


@app.get("/customers/{customer_name}")
def find_by_name(customer_name: str) -> Customer | None:
    for customer in customers_list:
        if customer.name == customer_name:
            return Customer(name=customer.name, email=customer.email)

    return None


@app.post("/customers")
def save_customer(customer: Customer):
    customers_list.append(customer)


@app.put("/customers/{customer_name}")
def update_customer(customer_name: str, new_customer: Customer):
    for customer in customers_list:
        if customer.name == customer_name:
            customer.name = new_customer.name
            customer.email = new_customer.email
            break


@app.delete("/customers/{customer_name}")
def delete_customer(name: str):
    for customer in customers_list:
        if customer.name == name:
            customers_list.remove(customer)
            break
