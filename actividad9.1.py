import json
import os


class Product:
    def __init__(self,name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        
        
        
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category
        }
class Inventory:
    def __init__(self, file_path="products.json"):
        self.file_path = file_path
        self.products = self.load_products()
        
    def load_products(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                
                data = json.load(file)
                return  [Product(c["name"],["price"], c["quantity"], c["category"]) for c in data]
        except Exception:
            return []
        
    def save_products(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            data = [c.to_dict() for c in self.products]
            json.dump(data, file, indent=4, ensure_ascii=False)
            
    def add_product(self, product):
        self.products.append(product)
        self.save_products()
        print("Product added and saved successfully!")
        
    def list_products(self):
        if not self.products:
            print("ERROR: No products found.")
            return
        
        print("\n--- Your products ---")
        for c in self.products:
            print(f"- {c.name} {c.price}: {c.quantity} - {c.category}")
            
    def search_product(self, query):
        for c in self.products:
            if c.name.lower() == query.lower():
                print(f"\nProduct  found: {c.name} - {c.price} - {c.quantity} - {c.category}")
                found = True
                break
            
            
def main():
    store = Inventory()
    
    while True:
        option = input("\nSelect an option:\n1. Add product\n2. View products\n3. Search products\n4. Exit: ").strip()
        
        
        if option == "1":
            name = input("Name: ").strip()
            price = input("Price: ").strip()
            quantity = input("Quantity: ").strip()
            category = input("Category: ").strip()
            
            if price and quantity:
                new_product = Product(name, price, quantity, category)
                store.add_product(new_product)
            else:
                print("ERROR: Price and quantity are required.")
                
        elif option == "2":
            store.list_products()
                
        elif option == "3":
                    query = input("Enter name to search: ").strip()
                    store.search_product(query)
                    
        elif option == "4":
            print("Bye")
            break
        
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
            