# to define resolver for each class to handle query and mutation

import strawberry
from typing import List, Optional
from strawberry.fastapi import GraphQLRouter
from src.graphql.define import Vessels, Catches, Buyers, Products, LocalShops, Resource, Distributors, VesselsInput, VesselsDelete, CatchesInput, CatchesDelete, BuyersInput, BuyersDelete, ProductsInput, ProductsDelete, LocalShopsInput, LocalShopsDelete, ResourceInput, ResourceDelete, DistributorsInput, DistributorsDelete
from src.routers.routers import get_vessels, get_catches, get_buyers, get_products, get_local_shops, get_resource, get_distributors, insert_buyer, update_buyer, delete_buyer, insert_vessel, update_vessel, delete_vessel, insert_catch, update_catch, delete_catch, insert_product, update_product, delete_product, insert_local_shop, update_local_shop, delete_local_shop, insert_resource, update_resource, delete_resource, insert_distributor, update_distributor, delete_distributor


# Query is for read operation
@strawberry.type
class Query:
    @strawberry.field(is_subscription=False)
    async def get_vessels(self) -> List[Vessels]:
        return await get_vessels()
    
    @strawberry.field(is_subscription=False)
    async def get_catches(self) -> List[Catches]:
        return await get_catches()

    @strawberry.field(is_subscription=False)
    async def get_buyers(self) -> List[Buyers]:
        return await get_buyers()

    @strawberry.field(is_subscription=False)
    async def get_products(self) -> List[Products]:
        return await get_products()

    @strawberry.field(is_subscription=False)
    async def get_local_shops(self) -> List[LocalShops]:
        return await get_local_shops()
    
    @strawberry.field(is_subscription=False)
    async def get_resource(self) -> List[Resource]:
        return await get_resource()
    
    @strawberry.field(is_subscription=False)
    async def get_distributors(self) -> List[Distributors]:
        return await get_distributors()
    

# mutation is for create, update, and delete operation
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_buyer(self, buyer: BuyersInput) -> Buyers:
        return await insert_buyer(buyer)

    @strawberry.mutation
    async def update_buyer(self, buyer: BuyersInput) -> Buyers:
        return await update_buyer(buyer)
    
    @strawberry.mutation
    async def delete_buyer(self, buyer: BuyersDelete) -> bool:
        return await delete_buyer(buyer_id = buyer.buyer_id)
    
    @strawberry.mutation
    async def create_vessel(self, vessel: VesselsInput) -> Vessels:
        return await insert_vessel(vessel)
    
    @strawberry.mutation
    async def update_vessel(self, vessel: VesselsInput) -> Vessels:
        return await update_vessel(vessel)
    
    @strawberry.mutation
    async def delete_vessel(self, vessel: VesselsDelete) -> bool:
        return await delete_vessel(vessel_id = vessel.vessel_id)
    
    @strawberry.mutation
    async def create_catch(self, catch: CatchesInput) -> Catches:
        return await insert_catch(catch)
    
    @strawberry.mutation
    async def update_catch(self, catch: CatchesInput) -> Catches:
        return await update_catch(catch)
    
    @strawberry.mutation
    async def delete_catch(self, catch: CatchesDelete) -> bool:
        return await delete_catch(catch_id = catch.catch_id)
    
    @strawberry.mutation
    async def create_product(self, product: ProductsInput) -> Products:
        return await insert_product(product)
    
    @strawberry.mutation
    async def update_product(self, product: ProductsInput) -> Products:
        return await update_product(product)
    
    @strawberry.mutation
    async def delete_product(self, product: ProductsDelete) -> bool:
        return await delete_product(product_id = product.product_id)
    
    @strawberry.mutation
    async def create_local_shop(self, local_shop: LocalShopsInput) -> LocalShops:
        return await insert_local_shop(local_shop)
    
    @strawberry.mutation
    async def update_local_shop(self, local_shop: LocalShopsInput) -> LocalShops:
        return await update_local_shop(local_shop)
    
    @strawberry.mutation
    async def delete_local_shop(self, local_shop: LocalShopsDelete) -> bool:
        return await delete_local_shop(local_shop_id = local_shop.local_shop_id)
    
    @strawberry.mutation
    async def create_resource(self, resource: ResourceInput) -> Resource:
        return await insert_resource(resource)
    
    @strawberry.mutation
    async def update_resource(self, resource: ResourceInput) -> Resource:
        return await update_resource(resource)
    
    @strawberry.mutation
    async def delete_resource(self, resource: ResourceDelete) -> bool:
        return await delete_resource(resource_id = resource.resource_id)
    
    @strawberry.mutation
    async def create_distributor(self, distributor: DistributorsInput) -> Distributors:
        return await insert_distributor(distributor)
    
    @strawberry.mutation
    async def update_distributor(self, distributor: DistributorsInput) -> Distributors:
        return await update_distributor(distributor)
    
    @strawberry.mutation
    async def delete_distributor(self, distributor: DistributorsDelete) -> bool:
        return await delete_distributor(distributor_id = distributor.distributor_id)

    
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)