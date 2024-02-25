# Django E-Commerce Backend API

## Overview

This project is a Django-based backend API for a basic e-commerce platform. It demonstrates the implementation of RESTful API development and database integration using Django and Django REST Framework.

## Getting Started

Follow these steps to set up and run the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`

Create and activate a virtual environment:
python -m venv venv
for mac/linux -> source venv/bin/activate # On Windows, use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Run the development server:
python manage.py runserver

API Endpoints
GET /products: Returns a list of all products.
GET /products/<id>: Returns details of a specific product.
POST /cart: Adds a product to the cart. Send data in the request body (e.g., {"product_id": 1, "quantity": 2}).
GET /cart: Retrieves the cart items.
DELETE /cart/<id>: Removes a specific item from the cart.

You can create data using :
python py_client/create.py

You can read data using :
python py_client/read.py

You can update data using :
python py_client/update.py

You can delete data using :
python py_client/delete.py

Contributing
Feel free to contribute to this project by opening issues or pull requests.

This project is licensed under the MIT License.
