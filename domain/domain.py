from typing import List, Set
from datetime import datetime
from enum import Enum
from uuid import UUID
from dataclasses import dataclass, field, make_dataclass, fields

# used in entity and aggregate_root
def eq(self, other):
    return self.Id == other.Id

# validates all fields with their givin field type
def validate(instance):
    for field in fields(instance):
        attr = getattr(instance, field.name)
        if not isinstance(attr, field.type):
            msg = "Field {0.name} is of type {1}, should be {0.type}".format(field, type(attr))
            raise ValueError(msg)

# A value object is immutable and it equality operator compares the values of each field
def value_object(cls):
    cls.__post_init__ = validate
    return dataclass(cls, frozen=True)

# make class immutable
def immutable(cls):
    cls.__post_init__ = validate
    return dataclass(cls, frozen=True)

# entity is immutable and it equality operator compares just the Id values
def entity(cls):
    # note the order of the field should be Id, ...
    T = make_dataclass(cls.__name__, fields=[('Id', UUID)], frozen=True)
    T.__post_init__ = validate
    X = dataclass(cls, frozen=True)
    Y = make_dataclass(cls.__name__, fields=[], bases=(X, T,), frozen=True)
    Y.__eq__ = eq
    return Y

# turns class into a mutable dataclass with the id field and the equality operator compares the Id values
def aggregate_root(cls):
    X = make_dataclass(cls.__name__, fields=[('Id', UUID)], bases=(cls,))
    X.__eq__ = eq
    X.__post_init__ = validate
    return X

# ---------- User aggregate ---------- 

@entity
class UserPersonalDetails:
    username: str
    password: str
    token: str

@aggregate_root
class User:
    user_info: UserPersonalDetails
    # y: int = field(init=False) # do not generate in __init__()

# ---------- User Groups aggregate ---------- 

@entity
class UserGroupDetail:
    group: str
    users: List[UUID]

@aggregate_root
class UserGroup:
    group_detail: UserGroupDetail

# ---------- Products aggregate ---------- 

@value_object
class ProductCategory:
    name: str
    description: str = ""

@entity
class ProductDetail:
    name: str
    category: ProductCategory
    price: float
    description: str 

@aggregate_root
class Product:
    product_detail: ProductDetail
    product_category: ProductCategory

# ---------- Store aggregate ---------- 
 
@entity
class StoreDetail:
    name: str
    description: str
    products: List[UUID]
    users: List[UUID]

@aggregate_root
class Store:
    store_detail: StoreDetail

# ---------- Customer aggregate ---------- 

@entity
class CustomerDetail:
    name: str
    balance: float
    tag_id: str
    products: List[UUID]

@aggregate_root
class Customer:
    customer_detail: CustomerDetail

# ---------- Order aggregate ---------- 

class PaymentType(Enum):
    Card = 1
    Cash = 2

@value_object
class ProductQuantity:
    product: UUID
    quantity: int
    price_per_product: float

@entity
class OrderDetail:
    store: StoreDetail
    customer: UUID
    user: User
    productsQuantity: List[ProductQuantity]
    payment_type: PaymentType
    total_amount: float
    refunded: bool =  False
    comment: str = ""
    datetime: datetime = datetime.utcnow()

@aggregate_root
class Order:
    order_detail: OrderDetail

