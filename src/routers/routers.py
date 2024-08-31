# endpoint for CRUD to each table

from typing import List
from src.databases.database import SessionLokal
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from src.models.models import Vessels, Catches, Buyers, Products, LocalShops, Distributors, Resource
from src.models.schema import VesselsModel, CatchesModel, BuyersModel, ProductsModel, LocalShopsModel, DistributorsModel, ResourceModel

router = APIRouter()
db = SessionLokal()

@router.get("/vessels", response_model=None, tags=["vessels"])
async def get_vessels() -> List[VesselsModel]:
    vessels = db.query(Vessels).all()
    return vessels

@router.post("/add-vessels/", tags=["vessels"])
async def insert_vessel(vessel: VesselsModel):
    new_vessel = Vessels(
        vessel_id = vessel.vessel_id,
        name=vessel.name,
        distributor_id=vessel.distributor_id,
        buyer_id=vessel.buyer_id,
        active=vessel.active
    )
    db.add(new_vessel)
    db.commit()
    db.refresh(new_vessel)
    return new_vessel

@router.put("/update-vessels/", tags=["vessels"])
async def update_vessel(updated_vessel: VesselsModel):
    newest_vessel = db.query(Vessels).filter(Vessels.vessel_id == updated_vessel.vessel_id).first()

    if newest_vessel:
        # this is to update the attributes of the existing vessel
        for ves, value1 in jsonable_encoder(updated_vessel).items():
            print(ves, value1)
            if value1:
                setattr(newest_vessel, ves, value1)
        
        db.commit()
        db.refresh(newest_vessel)
        return newest_vessel

    return {"message" : "Those Vessel or Table might be not found"}

@router.delete("/delete-vessels/{vessel_id}", tags=["vessels"])
async def delete_vessel(vessel_id, int):
    newest_vessel = db.query(Vessels).filter(Vessels.vessel_id == vessel_id).first()

    if newest_vessel:
        db.delete(newest_vessel)
        db.commit()
    
    return False

@router.get("/catches", response_model=None, tags=["catches"])
async def get_catches() -> List[CatchesModel]:
    catches = db.query(Catches).all()
    return catches

@router.post("/add-catches/", tags=["catches"])
async def insert_catch(catch: CatchesModel):
    new_catch = Catches(
        catch_id=catch.catch_id,
        vessel_id=catch.vessel_id,
        local_shop_id=catch.local_shop_id,
        product_id=catch.product_id,
        creation_date=catch.creation_date
    )
    db.add(new_catch)
    db.commit()
    db.refresh(new_catch)
    return new_catch

@router.put("/update-catches/", tags=["catches"])
async def update_catch(updated_catch: CatchesModel):
    existing_catch = db.query(Catches).filter(Catches.catch_id == updated_catch.catch_id).first()

    if existing_catch:
        for key, value in jsonable_encoder(updated_catch).items():
            if value is not None:
                setattr(existing_catch, key, value)
        db.commit()
        db.refresh(existing_catch)
        return existing_catch

    raise HTTPException(status_code=404, detail="Catch not found")


@router.delete("/delete-catches/{catch_id}", tags=["catches"])
async def delete_catch(catch_id: int):
    existing_catch = db.query(Catches).filter(Catches.catch_id == catch_id).first()

    if existing_catch:
        db.delete(existing_catch)
        db.commit()
        return True

    raise HTTPException(status_code=404, detail="Catch not found")


@router.get("/buyers", response_model=None, tags=["buyers"])
async def get_buyers() -> List[BuyersModel]:
    buyers = db.query(Buyers).all()
    return buyers

@router.post("/add-buyers/", tags=["buyers"])
async def insert_buyer(buyer: BuyersModel):
    new_buyer = Buyers(
        buyer_id=buyer.buyer_id,
        name=buyer.name,
        email=buyer.email,
        phone=buyer.phone,
        address=buyer.address
    )
    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)
    return new_buyer

@router.put("/update-buyers/", tags=["buyers"])
async def update_buyer(updated_buyer: BuyersModel):
    newest_buyer = db.query(Buyers).filter(Buyers.buyer_id == updated_buyer.buyer_id).first()

    if newest_buyer:
        # to update the attributes of the existing buyer
        update_item_encoded = jsonable_encoder(updated_buyer)
        for buy, value2 in update_item_encoded.items():
            if buy != "buyer_id":
                setattr(newest_buyer, buy, value2)

        db.commit()
        db.refresh(newest_buyer)
        
        return newest_buyer
    return {"message": "Buyer cant found here"}

@router.delete("/delete-buyers/{buyer_id}", tags=["buyers"])
async def delete_buyer(buyer_id: int):
    newest_buyer = db.query(Buyers).filter(Buyers.buyer_id == buyer_id).first()

    if newest_buyer:
        db.delete(newest_buyer)
        db.commit()
        return True
    return False

@router.get("/buyers/search/", response_model=None, tags=["buyers"])
async def search_buyer_by_name(name: str):
    buyer = db.query(Buyers).filter(Buyers.name == name).first()
    
    if buyer:
        return buyer

    raise HTTPException(status_code=404, detail="Buyer not found")

@router.get("/products", response_model=None, tags=["products"])
async def get_products() -> List[ProductsModel]:
    products = db.query(Products).all()
    return products

@router.post("/add-products/", tags=["products"])
async def insert_product(product: ProductsModel):
    new_product = Products(
        product_id=product.product_id,
        name=product.name,
        quantity=product.quantity,
        description=product.description,
        price_product=product.price_product
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.put("/update-products/", tags=["products"])
async def update_product(updated_product: ProductsModel):
    existing_product = db.query(Products).filter(Products.product_id == updated_product.product_id).first()

    if existing_product:
        for key, value in jsonable_encoder(updated_product).items():
            if value is not None:
                setattr(existing_product, key, value)
        db.commit()
        db.refresh(existing_product)
        return existing_product

    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/delete-products/{product_id}", tags=["products"])
async def delete_product(product_id: int):
    existing_product = db.query(Products).filter(Products.product_id == product_id).first()

    if existing_product:
        db.delete(existing_product)
        db.commit()
        return True

    raise HTTPException(status_code=404, detail="Product not found")

@router.get("/local_shops", response_model=None, tags=["local_shops"])
async def get_local_shops() -> List[LocalShopsModel]:
    local_shops = db.query(LocalShops).all()
    return local_shops

@router.post("/add-local-shops/", tags=["local_shops"])
async def insert_local_shop(local_shop: LocalShopsModel):
    new_local_shop = LocalShops(
        local_shop_id=local_shop.local_shop_id,
        name=local_shop.name,
        location=local_shop.location
    )
    db.add(new_local_shop)
    db.commit()
    db.refresh(new_local_shop)
    return new_local_shop


@router.put("/update-local-shops/", tags=["local_shops"])
async def update_local_shop(updated_local_shop: LocalShopsModel):
    existing_local_shop = db.query(LocalShops).filter(LocalShops.local_shop_id == updated_local_shop.local_shop_id).first()

    if existing_local_shop:
        for key, value in jsonable_encoder(updated_local_shop).items():
            if value is not None:
                setattr(existing_local_shop, key, value)
        db.commit()
        db.refresh(existing_local_shop)
        return existing_local_shop

    raise HTTPException(status_code=404, detail="Local Shop not found")

@router.delete("/delete-local-shops/{local_shop_id}", tags=["local_shops"])
async def delete_local_shop(local_shop_id: int):
    existing_local_shop = db.query(LocalShops).filter(LocalShops.local_shop_id == local_shop_id).first()

    if existing_local_shop:
        db.delete(existing_local_shop)
        db.commit()
        return True

    raise HTTPException(status_code=404, detail="Local Shop not found")

@router.get("/resource", response_model=None, tags=["resource"])
async def get_resource() -> List[ResourceModel]:
    resource = db.query(Resource).all()
    return resource

@router.post("/add-resource/", tags=["resource"])
async def insert_resource(resource: ResourceModel):
    new_resource = Resource(
        resource_id=resource.resource_id,
        name=resource.name,
        resource_type=resource.resource_type,
        resource_details=resource.resource_details
    )
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource

@router.put("/update-resource/", tags=["resource"])
async def update_resource(updated_resource: ResourceModel):
    existing_resource = db.query(Resource).filter(Resource.resource_id == updated_resource.resource_id).first()

    if existing_resource:
        for key, value in jsonable_encoder(updated_resource).items():
            if value is not None:
                setattr(existing_resource, key, value)
        db.commit()
        db.refresh(existing_resource)
        return existing_resource

    raise HTTPException(status_code=404, detail="Resource not found")

@router.delete("/delete-resource/{resource_id}", tags=["resource"])
async def delete_resource(resource_id: int):
    existing_resource = db.query(Resource).filter(Resource.resource_id == resource_id).first()

    if existing_resource:
        db.delete(existing_resource)
        db.commit()
        return True

    raise HTTPException(status_code=404, detail="Resource not found")

@router.get("/distributors", response_model=None, tags=["distributors"])
async def get_distributors() -> List[DistributorsModel]:
    distributors = db.query(Distributors).all()
    return distributors


@router.post("/add-distributors/", tags=["distributors"])
async def insert_distributor(distributor: DistributorsModel):
    new_distributor = Distributors(
        distributor_id=distributor.distributor_id,
        resource_id=distributor.resource_id,
        name=distributor.name,
        email=distributor.email,
        phone=distributor.phone
    )
    db.add(new_distributor)
    db.commit()
    db.refresh(new_distributor)
    return new_distributor

@router.put("/update-distributors/", tags=["distributors"])
async def update_distributor(updated_distributor: DistributorsModel):
    existing_distributor = db.query(Distributors).filter(Distributors.distributor_id == updated_distributor.distributor_id).first()

    if existing_distributor:
        for key, value in jsonable_encoder(updated_distributor).items():
            if value is not None:
                setattr(existing_distributor, key, value)
        db.commit()
        db.refresh(existing_distributor)
        return existing_distributor

    raise HTTPException(status_code=404, detail="Distributor not found")

@router.delete("/delete-distributors/{distributor_id}", tags=["distributors"])
async def delete_distributor(distributor_id: int):
    existing_distributor = db.query(Distributors).filter(Distributors.distributor_id == distributor_id).first()

    if existing_distributor:
        db.delete(existing_distributor)
        db.commit()
        return True

    raise HTTPException(status_code=404, detail="Distributor not found")