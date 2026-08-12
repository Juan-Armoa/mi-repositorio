import requests
import json

def fetch_online_users():
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:

        response = requests.get(url)
        response.raise_for_status() 
        users_data = response.json()
        
        print(f"Successfully retrieved {len(users_data)} users from the API!\n")
        
        clean_users = []
        for user in users_data:
            user_info = {
                "name": user["name"],
                "email": user["email"],
                "company": user["company"]["name"],
                "city": user["address"]["city"]
            }
            clean_users.append(user_info)
            
        return clean_users

    except requests.exceptions.RequestException as error:
        print(f"Error connecting to the API: {error}")
        return []

if __name__ == "__main__":
    users = fetch_online_users()
    
    for user in users[:3]:
        print(f"Name: {user['name']} | Company: {user['company']} | City: {user['city']}")
        
    with open("api_users.json", "w") as file:
        json.dump(users, file, indent=4)
        print("\nUsers saved successfully to api_users.json!")