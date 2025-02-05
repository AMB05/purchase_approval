# **Purchase Approval Module Odoo17**

- Module Name: purchase_approval
- Category: Purchase
- Odoo Version: 17
- Description: Approval workflow for purchase orders and product API category_id and category_name
#
## Installation  
- Activate Purchase Module
- Create addons in the configuration section

  example:

	```name: odoo.conf```

	```addons_path = D:\Project\Odoo\Odoo\odoo17\addons,D:\Project\Odoo\Odoo\addons_custom```
- Run odoo
- Apps --> Activate approval module
#
## Approval Workflow
- After completing the activation of the purchase module and purchase approval module, please open the purchase module
![image](https://github.com/user-attachments/assets/aa9ba5a1-e853-44b3-b378-9868b07c7b5c)

- Create new order
  
  <img width="743" alt="create new" src="https://github.com/user-attachments/assets/486c52d7-9d4c-4ab1-8952-19ab6ae07428" />
  
  ![image](https://github.com/user-attachments/assets/4298895d-ebd2-4385-87e3-82aa634a6e4d)
### IF Total Amount < $5000
- Add data columns and add products, ```for example adding products with a total < $5000``` --> Confirm Order
  <img width="742" alt="create new 1" src="https://github.com/user-attachments/assets/aee672b0-ae01-42b5-a382-e7ea95dee9c1" />

- Display status becomes purchase order
  ![image](https://github.com/user-attachments/assets/09afc374-47d0-4de9-a8d1-92076484c6b1)

### IF Total Amount >= $5000  
- Create new order
  
  <img width="743" alt="create new" src="https://github.com/user-attachments/assets/486c52d7-9d4c-4ab1-8952-19ab6ae07428" />
  
  ![image](https://github.com/user-attachments/assets/4298895d-ebd2-4385-87e3-82aa634a6e4d)

- Add data columns and add products, ```for example adding products with a total >= $5000``` --> Confirm Order
  <img width="742" alt="create new 2" src="https://github.com/user-attachments/assets/d53831a1-8284-4d7c-8287-82793751f5fa" />

- If total amount >= $5000 then the status will be waiting approval and requires approval by the manager
  ![image](https://github.com/user-attachments/assets/2d8f99a8-cd6d-4c0a-bb75-a7c3e7813bd0)
  _**Note:**_ **_Approval can only be Approv by a manager or administrator_**

- After approval, the status will change to Purchase Order
  ![image](https://github.com/user-attachments/assets/563d16aa-9c22-4c4e-8626-ad5284b70903)
#
## REST API Endpoint
- GET API Product (Postman)
  http://localhost:8069/api/products
  ![image](https://github.com/user-attachments/assets/253b5f2b-0c49-497b-9e02-20bdb7009128)

- GET API Product (Browser)
  http://localhost:8069/api/products
  ![image](https://github.com/user-attachments/assets/25d22aca-cde6-457f-af0d-e7dd25fbbea1)

- GET API Product Filter Category_ID (Postman)
  http://localhost:8069/api/products?category_id=3
  ![image](https://github.com/user-attachments/assets/d356b9e2-8d4c-4663-9054-c0a535081263)
  
- GET API Product Filter Category_ID (Browser)
  http://localhost:8069/api/products?category_id=3
  ![image](https://github.com/user-attachments/assets/8f9ddba9-17b0-48e3-b6fe-a7202e9c6122)

- GET API Product Filter Category_Name (Postman)
  http://localhost:8069/api/products?category_name=service
  ![image](https://github.com/user-attachments/assets/d081980e-58bc-4750-96a3-f46f501baff5)
  
- GET API Product Filter Category_Name (Browser)
  http://localhost:8069/api/products?category_name=service
  ![image](https://github.com/user-attachments/assets/061c0c6b-8e3f-459d-9554-56687cb21b17)
