# to create a schema for GraphQL by class and data type attributes

import strawberry
from typing import Optional

@strawberry.type
class Vessels:
    vessel_id: int
    name: Optional[str]
    distributor_id: Optional[int]
    buyer_id: Optional[int]
    active: Optional[str]
    buyers: Optional["Buyers"]
    distributor: Optional["Distributors"]
    catches: Optional["Catches"]

@strawberry.input
class VesselsInput:
    vessel_id: int
    name: Optional[str]

@strawberry.input
class VesselsDelete:
    vessel_id: int


@strawberry.type
class Catches:
    catch_id: int
    vessel_id: int
    local_shop_id: int
    product_id: int
    creation_date: str
    local_shop: Optional["LocalShops"]
    products: Optional["Products"]

@strawberry.input
class CatchesInput:
    catch_id: int
    vessel_id: int
    local_shop_id: Optional[int]
    product_id: Optional[int]
    creation_date: Optional[str]

@strawberry.input
class CatchesDelete:
    catch_id: int

@strawberry.type
class Buyers:
    buyer_id: int
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]

@strawberry.input
class BuyersInput:
    buyer_id: int
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]

@strawberry.input
class BuyersDelete:
    buyer_id: int

@strawberry.type
class Products:
    product_id: int
    name: Optional[str]
    quantity: Optional[int]
    description: Optional[str]
    price_product: Optional[int]

@strawberry.input
class ProductsInput:
    product_id: int
    name: Optional[str]
    quantity: Optional[int]
    description: Optional[str]
    price_product: Optional[int]

@strawberry.input
class ProductsDelete:
    product_id: int

@strawberry.type
class LocalShops:
    local_shop_id: int
    name: Optional[str]
    location: Optional[str]

@strawberry.input
class LocalShopsInput:
    local_shop_id: int
    name: Optional[str]
    location: Optional[str]

@strawberry.input
class LocalShopsDelete:
    local_shop_id: int

@strawberry.type
class Resource:
    resource_id: int
    name: Optional[str]
    resource_type: Optional[str]
    resource_details: Optional[str]

@strawberry.input
class ResourceInput:
    resource_id: int
    name: Optional[str]
    resource_type: Optional[str]
    resource_details: Optional[str]

@strawberry.input
class ResourceDelete:
    resource_id: int

@strawberry.type
class Distributors:
    distributor_id: int
    resource_id: int
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    resource: Optional["Resource"]

@strawberry.input
class DistributorsInput:
    distributor_id: int
    resource_id: int
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]

@strawberry.input
class DistributorsDelete:
    distributor_id: int