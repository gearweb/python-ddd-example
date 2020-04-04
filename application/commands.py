from dataclasses import dataclass
from domain.domain import immutable
from enum import Enum
from typing import List

@immutable
class OrderLine:
    product_id: str
    quantity: int

@immutable
class CreateOrderCommand:
    customer_id: str
    store_id: str
    lines: List[OrderLine]

def CreateOrderCommandHandler(command: CreateOrderCommand):
    """CreateOrderCommandHandler

    @param command:
    :type command: CreateOrderCommand
    """
    pass

@immutable
class PaymentType(Enum):
    CARD = 0
    CASH = 1 

@immutable
class CreateCustomerCommand:
    id: str
    amount: float
    type: PaymentType

def CreateCustomerCommandHandler(command: CreateCustomerCommand):
    """CreateCustomerCommandHandler

    @param command:
    :type command: CreateCustomerCommand
    """
    pass

@immutable
class CreateUserCommand:
    user_id: str

def CreateUserCommandHandler(command: CreateUserCommand):
    """CreateUserCommand

    @param command:
    :type command: CreateUserCommand
    """
    pass
