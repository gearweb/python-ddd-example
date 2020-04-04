from application.grpc_services.pos_service.generated import pos_pb2 as pos_messages 
from application.grpc_services.pos_service.generated import pos_pb2_grpc as pos_service 
from infrastructure.event_bus import EventBus
from application.commands import CreateUserCommand

class POSService(pos_service.POSServicer):
    def __init__(self, event_bus: EventBus):
        self.event_bus:EventBus = event_bus

# temp
    def CommandCreateUser(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        self.event_bus.send() 
        create_user_id = request.id 
        print("User id to create: " + str(create_user_id))
        return pos_messages.OKResponse(is_error=False, success_msg="Success Fully created User", error_msg="")

    def CreateUser(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        result = self.event_bus.send(CreateUserCommand(request.id))
        if result:
            return pos_messages.OKResponse(is_error=False, success_msg="Created User", error_msg="")
        else:
            return pos_messages.OKResponse(is_error=True, success_msg="", error_msg="Could not create user")

    def CreateCustomer(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        pass

    def GetCustomer(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        pass

    def GetStore(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        pass

    def GetStores(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        pass

    def GetCategory(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        pass

    def CreateOrder(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        pass

    def CustomerPayment(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        pass


