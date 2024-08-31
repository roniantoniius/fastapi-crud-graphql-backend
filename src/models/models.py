from typing import List
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, Integer, String, ForeignKey
from src.databases.database import Base

class Vessels(Base):
    __tablename__ = "vessels"

    vessel_id = Column(Integer, primary_key=True)
    name = Column(String)
    distributor_id = Column(Integer, ForeignKey('distributors.distributor_id'))
    buyer_id = Column(Integer, ForeignKey('buyers.buyer_id'))
    active = Column(String)
    buyers: Mapped["Buyers"] = relationship("Buyers", back_populates="vessels")
    distributor: Mapped["Distributors"] = relationship("Distributors", back_populates="vessels")
    catches: Mapped["Catches"] = relationship("Catches", back_populates="vessels")

class Catches(Base):
    __tablename__ = "catches"

    catch_id = Column(Integer, primary_key=True)
    vessel_id = Column(Integer, ForeignKey('vessels.vessel_id'))
    local_shop_id = Column(Integer, ForeignKey('local_shops.local_shop_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    creation_date = Column(String)
    vessels: Mapped["Vessels"] = relationship("Vessels", back_populates="catches")
    local_shops: Mapped["LocalShops"] = relationship("LocalShops", back_populates="catches")
    products: Mapped["Products"] = relationship("Products", back_populates="catches")

class Buyers(Base):
    __tablename__ = "buyers"

    buyer_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    vessels: Mapped[List["Vessels"]] = relationship("Vessels", back_populates="buyers")

class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    description = Column(String)
    price_product = Column(Integer)
    catches: Mapped[List["Catches"]] = relationship("Catches", back_populates="products")

class LocalShops(Base):
    __tablename__ = "local_shops"

    local_shop_id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    catches: Mapped[List["Catches"]] = relationship("Catches", back_populates="local_shops")

class Resource(Base):
    __tablename__ = "resource"

    resource_id = Column(Integer, primary_key=True)
    name = Column(String)
    resource_type = Column(String)
    resource_details = Column(String)
    distributor: Mapped["Distributors"] = relationship("Distributors", back_populates="resource")

class Distributors(Base):
    __tablename__ = "distributors"

    distributor_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    resource_id = Column(Integer, ForeignKey('resource.resource_id'))
    vessels: Mapped[List["Vessels"]] = relationship("Vessels", back_populates="distributor")
    resource: Mapped["Resource"] = relationship("Resource", back_populates="distributor")
