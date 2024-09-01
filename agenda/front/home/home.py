import flet as ft
from components.user_card import user_card

def home_page(page: ft.Page,on_logout: callable):
    if not page.session.get("logged_in"):
        page.go("/auth/login")  # Redirige a la página de login si no está autenticado

    username = page.session.get("username")  # Obtener el nombre de usuario de la sesión

    def handle_logout():
        # Eliminar sesión y redirigir al login
        page.session.set("logged_in", False)
        page.session.remove('username')
        page.session.clear()
        page.go("/auth/login")  # Redirige al login después del logout
        

    # Crear la tarjeta de usuario
    user_card_component = user_card(page, username, handle_logout)

    # Añadir componentes a la página
    return ft.Column(
        controls=[
            ft.Text(f"Welcome to the Home Page {username}", size=24),
            user_card_component
        ]
    )
