import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000"

def login_page(page: ft.Page, navigate_to_register):
    def login(e):
        username = username_input.value
        password = password_input.value
        
        try:
            response = requests.post(f"{API_BASE_URL}/auth/login", json={
                "username": username,
                "password": password
                })
            
            if response.status_code == 200:
                data = response.json()
                print("Data received:", data)
                # Forzando la redirección sin la verificación de 'Login successful'
                page.session.set("logged_in", True)
                page.session.set("username", username)
                print("Logged in:", page.session.get("logged_in"))
                print("Username:", page.session.get("username"))
                page.update()
                page.go("/home/home")
            else:
                result_text.value = "Login failed! Please check your credentials."

            page.update()
        except requests.exceptions.RequestException as error:
            result_text.value = f"Request failed: {error}"
        
        page.update()

    def go_to_register(e):
        navigate_to_register()

    username_input = ft.TextField(label="Username")
    password_input = ft.TextField(label="Password", password=True)
    result_text = ft.Text("")
    login_button = ft.ElevatedButton(text="Login", on_click=login)
    register_button = ft.ElevatedButton(text="Go to Register", on_click=go_to_register)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Login", size=24),
                username_input,
                password_input,
                login_button,
                result_text,
                register_button
            ]
        )
    )
