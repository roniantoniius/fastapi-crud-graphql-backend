# Seafood CRUD FastAPI with GraphQL

Seafood CRUD FastAPI with GraphQL is a streamlined API project designed for managing marine products, built using FastAPI and GraphQL. It leverages Strawberry GraphQL for creating a robust and flexible GraphQL schema, providing a streamlined interface for data queries and mutations. The application utilizes SQLAlchemy ORM for seamless database interactions, interfacing with a SQLite backend to handle data persistence. The combination of FastAPI and GraphQL ensures high performance and efficient data management, making it an ideal solution for handling seafood inventory and related operations to support further website.

## Data Understanding
![database_ERD_marineShop](https://github.com/user-attachments/assets/eeb3f235-1b55-476f-9571-18dd889f8ed0)

1. Vessels
Function and Purpose: This table stores the overall information used for marine product sales or transactions. Each vessel has a unique ID namely vessel_id (PK), name, and active status. Analogously, this table is a transaction record that has information on transaction id (vessel_id), seller (distributor), buyer (buyer), and a list of products purchased (catches). This vessel is connected to the distributor (seller), buyer, and catches.

2. Catches
Function and Purpose: This table records the list of products purchased by customers along with the stores that sell these products. Each catches has a unique ID, namely catch_id (PK), vessel_id (FK), quantity, price_total, and the local ID of the shop and the associated product.

3. Buyers
Function and Purpose: This table stores information about buyers of marine products. Each buyer has a unique ID buyer_id (PK), name, email, phone, address.

4. Products
Function and Purpose: This table contains information about the various sea products sold. Each product has a unique ID, name, description, and price_product.

5. LocalShops
Function and Purpose: This table records information about local shops that sell marine products. Each shop has a unique ID, name, and location.

6. Resource
Function and Purpose: This table records information about the resources used by the distributor. This table has a unique ID, resource_type, and resource_details.

7. Distributors
Function and Purpose: This table stores information about those who sell marine products. Each distributor has a unique ID, name, email, phone, and the ID of the resource they use.


### Start FastAPI Server
```
uvicorn main:app --reload
```
and also
```
http://127.0.0.1:8000/docs
```

![fastapi_ui](https://github.com/user-attachments/assets/595da366-8424-4c81-906d-b08cafbd3b93)
