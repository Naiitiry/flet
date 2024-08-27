import flet as ft
import requests
from werkzeug.security import generate_password_hash


# URL base de tu API Flask
API_BASE_URL = "http://127.0.0.1:5000"

def main(page: ft.Page):

    def login(e):
        # Datos del usuario para hacer login
        username = username_input.value
        password = password_input.value
        email = email_input.value
        
        # Realiza la petición a la API
        response = requests.post(f"{API_BASE_URL}/auth/register", json={
            "username": username,
            "password": password,
            "email": email
        })

        # Procesa la respuesta
        if response.status_code == 200:
            data = response.json()
            result_text.value = f"Login successful! Welcome {data['username']}"
        else:
            result_text.value = "Login failed! Please check your credentials."

        page.update()

    def register(e):
        # Similar al login, pero con la ruta de registro
        username = username_input.value
        password = password_input.value
        email = email_input.value

        try:
            response = requests.post(f"{API_BASE_URL}/auth/register", json={
                "username": username,
                "password": password,
                "email": email
            })

            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

            if response.status_code == 201:
                result_text.value = "Registration successful! You can now login."
            else:
                result_text.value = "Registration failed! Please try again."

            # Si la respuesta es JSON, la mostramos
            try:
                print(f"Response Content: {response.json()}")
            except ValueError:
                print("No JSON in response.")

        except requests.exceptions.RequestException as error:
            result_text.value = f"Request failed: {error}"
        page.update()

    # Crear los componentes de la UI
    username_input = ft.TextField(label="Username")
    password_input = ft.TextField(label="Password", password=True)
    email_input = ft.TextField(label="Email")
    result_text = ft.Text()

    login_button = ft.ElevatedButton(text="Login", on_click=login)
    register_button = ft.ElevatedButton(text="Register", on_click=register)
    
    # Añadir componentes a la página
    page.add(
        ft.Text("Login or Register", size=24),
        username_input,
        password_input,
        email_input,
        login_button,
        register_button,
        result_text
    )

ft.app(target=main)