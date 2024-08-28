import flet as ft
import requests
from components.user_card import user_card

def home_page(page: ft.Page):
    if not page.session.get("logged_in"):
        page.go("/auth/login")  # Redirige a la página de login si no está autenticado

    username = page.session.get("username", "User")  # Obtener el nombre de usuario de la sesión

    def handle_logout(e=None):
        # Eliminar sesión y redirigir al login
        page.session.set("logged_in", False)
        page.session.set("username",None)
        page.go("/auth/login")

    # Crear la tarjeta de usuario
    user_card_component = user_card(page, username, handle_logout)

    # Añadir componentes a la página
    page.add(
        ft.Text("Welcome to the Home Page", size=24),
        #user_card_component
    )
