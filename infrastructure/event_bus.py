from dataclasses import dataclass
from typing import List, Callable

class EventBus():
    def __init__(self):
        self.subscriptions: dict = {} 

    def subscribe_handler(self, event, func: Callable):
        """subscribe a function to recieve a certain event

        @param event: any class
        @param func: any function that takes in the event as parameter
        """
        # if multiple events have a function, add them together.
        # they will be executed in def broadcast, but only the last one will be def send
        key = event.__name__
        if key in self.subscriptions:
            self.subscriptions[key].append(func)
        else:
            self.subscriptions[key] = [func]

    def send(self, event):
        """runs the function that was subscribe to the event and return its result

        @param event: must be a class to retrieve name
        """
        # only send to the last function in the list
        func_list = self.subscriptions[type(event).__name__]
        func = func_list[len(func_list)-1]
        return func(event)

    def broadcast(self, event):
        """runs the functions that was subscribe to the event, they do not return any results

        @param event: must be a class to retrieve name
        """
        for func in self.subscriptions[type(event).__name__]:
            func(event)

# ------------ Example ------------ 

"""

event_bus = EventBus()
# Create command
@dataclass
class CreateUserCommand:
    name: str
    surname: str

# Function to handle the command
def handle_user_command(command: CreateUserCommand):
    print('Function handle_user_command received:')
    print(command)
    return "returned value"

# subscribe the function to handle the command
event_bus.subscribe_handler(CreateUserCommand, handle_user_command,)
event_bus.subscribe_handler(CreateUserCommand, handle_user_command,)

# send the command, def handle_user_command() executes
test = CreateUserCommand(name="chris", surname="james")
returned = event_bus.send(test)
print(returned) 


print("broadcast") 
event_bus.broadcast(test)

"""
