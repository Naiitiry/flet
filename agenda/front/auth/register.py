import flet as ft
import requests

# URL base de tu API Flask
API_BASE_URL = "http://127.0.0.1:5000"

def register_page(page: ft.Page, navigate_to_login):
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
            page.update()
        except requests.exceptions.RequestException as error:
            result_text.value = f"Request failed: {error}"
        page.update()
    
    # Función para navegar a la página de login
    def go_to_login(e):
        navigate_to_login()

    username_input = ft.TextField(label="Username")
    password_input = ft.TextField(label="Password", password=True)
    email_input = ft.TextField(label="Email")
    result_text = ft.Text("")
    register_button = ft.ElevatedButton(text="Register", on_click=register)
    login_button = ft.ElevatedButton(text="Go to Login", on_click=go_to_login)

    # Agrega los componentes a la página
    return ft.Column(
                controls=[
                    ft.Text("Register", size=24),
                    username_input,
                    password_input,
                    email_input,
                    register_button,
                    result_text,
                    login_button]
        )