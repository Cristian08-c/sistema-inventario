import os
from supabase import create_client, Client
from dotenv import load_dotenv


#load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")


supabase: Client = create_client(url, key)

def create_user(username, password, role):
    data = {
        "username": username,
        "password": password,
        "role": role
    }
    response = supabase.table("users").insert(data).execute()
    print("Usuario creado:", response.data)





def read_user_by_username(username):
    data = {"username"}

    response = supabase.table("users").select("*").eq("username",username).execute()
    if not response.data:
        print("User no encontado")
    else:
        return response.data[0]["username"],response.data[0]["password"]


user,password = read_user_by_username("Safe")

print(password)
