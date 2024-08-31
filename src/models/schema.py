# pydantic models for the schema

from typing import List, Optional
from dataclasses import dataclass

@dataclass
class BuyersModel:
    buyer_id: int
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]

@dataclass
class ProductsModel:
    product_id: int
    name: Optional[str]
    quantity: Optional[int]
    description: Optional[str]
    price_product: Optional[int]

@dataclass
class LocalShopsModel:
    local_shop_id: int
    name: Optional[str]
    location: Optional[str]

@dataclass
class ResourceModel:
    resource_id: int
    name: Optional[str]
    resource_type: Optional[str]
    resource_details: Optional[str]

@dataclass
class DistributorsModel:
    distributor_id: int
    resource_id: Optional[int]
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    resource: Optional[ResourceModel] = None

@dataclass
class CatchesModel:
    catch_id: int
    vessel_id: int
    local_shop_id: Optional[int]
    product_id: Optional[int]
    creation_date: Optional[str]
    local_shop: Optional[LocalShopsModel] = None

@dataclass
class VesselsModel:
    vessel_id: int
    name: Optional[str]
    distributor_id: Optional[int]
    buyer_id: Optional[int]
    active: Optional[str]
    buyers: Optional[BuyersModel] = None
    distributor: Optional[DistributorsModel] = None
    catches: Optional[CatchesModel] = None