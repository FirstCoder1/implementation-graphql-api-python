import strawberry

import movierental.api.definitions.film as film
from movierental.database.models import City as CityModel
from movierental.database.models import Addres as AddressModel
from movierental.database.models import Country as CountryModel
from movierental.database.models import Customer as CustomerModel
from movierental.api.definitions.address import Address


@strawberry.type(description="Customer and it's properties")
class Customer:
    customer_id: int = strawberry.field(description="Id of the address")
    first_name: str = strawberry.field(description="First name of the customer")
    last_name: str = strawberry.field(description="Last name of the customer")
    email: str = strawberry.field(description="Email of the customer")
    active: bool = strawberry.field(description="Is customer active")

    instance: strawberry.Private[CustomerModel]

    @strawberry.field
    def address(self) -> Address:
        return Address.from_instance(self.instance.address)

    @classmethod
    def from_instance(cls, instance):
        return cls(
            instance=instance,
            customer_id=instance.customer_id,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            active=True if instance.active == 1 else False,
        )
