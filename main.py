from domain import domain
from application.grpc_services.pos_service import pos_server
from infrastructure.event_bus import EventBus
import uuid

def main():
    _id = uuid.uuid4()
    product_category = domain.ProductCategory(name="kos", description="desc")
    product = domain.ProductDetail(Id=_id, name="chips", category=product_category, price=10.0, description="ch")
    product2 = domain.ProductDetail(Id=_id, name="chips2", category=product_category, price=10.0, description="ch")
    print(product.__dict__)
    print(product2.__dict__)
    print(product.__dict__ == product2.__dict__)

    print("product== product2")
    print(product== product2)
    print(type(product).__name__)

if __name__ == "__main__":
    # event_bus = EventBus()
    main()
    # test = pos_server.POSService(event_bus)

