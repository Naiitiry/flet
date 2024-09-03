import flet as ft
from components.user_card import user_card
from components.themes import themes_change


def home_page(page: ft.Page, on_logout: callable):
    if not page.session.get("logged_in"):
        page.go("/auth/login")  # Redirige a la página de login si no está autenticado

    username = page.session.get("username")  # Obtener el nombre de usuario de la sesión

    def handle_logout():
        # Eliminar sesión y redirigir al login
        print("Deslogeo exitoso!")
        on_logout
        page.session.set("logged_in", False)
        page.session.remove('username')
        page.session.clear()
        page.go("/auth/login")  # Redirige al login después del logout
        
    # Traer el cambio de temas
    cambio_de_tema = themes_change(page)

    # Crear la tarjeta de usuario
    user_card_component = user_card(page, username, handle_logout)


    # Añadir componentes a la página
    return ft.Column(
        controls=[
            cambio_de_tema,
            ft.Text(f"Welcome to the Home Page {username}", size=24),
            user_card_component,
        ]
    )
