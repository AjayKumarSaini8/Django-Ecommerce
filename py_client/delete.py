import requests

product_id = input("What is the product id you want to delete?\n")

try:
    product_id = int(product_id)
except ValueError:
    print(f"{product_id} is not a valid id (must be an integer)")
    # Exit or handle the error accordingly
    exit()

endpoint = f"http://127.0.0.1:8000/products/{product_id}/"

get_response = requests.delete(endpoint)

if get_response.status_code == 204:
    print(f"Product with id {product_id} successfully deleted.")
else:
    print(
        f"Error deleting product with id {product_id}. Status code: {get_response.status_code}"
    )
    print(
        get_response.text
    )  # Print the response content for further debugging if needed
