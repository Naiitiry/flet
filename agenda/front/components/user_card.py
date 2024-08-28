import flet as ft
import requests

def user_card(page: ft.Page, username: str, on_logout: callable) -> ft.Column:

    def logout(e):
        # Ejecutar función de logout
        on_logout()

    # Crear componentes de la tarjeta
    user_info = ft.Text(f"User: {username}", size=20)
    logout_button = ft.ElevatedButton(text="Logout", on_click=logout)

    # Crear la tarjeta

    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[user_info, logout_button],
                spacing=10
            ),
            padding=10,
            border_radius=10,
            bgcolor="#f0f0f0",
            border=ft.border_radius.all(10)
        ),
    )

    # card2 = ft.Column(
    #     controls=[
    #         ft.Container(
    #             content=ft.Column(
    #                 controls=[user_info, logout_button],
    #                 spacing=10
    #             ),
    #             padding=10,
    #             border_radius=10,
    #             bgcolor="#f0f0f0",
    #             border=ft.Border.all(1, "#ddd")
    #         ),
    #         spacing=10
    #             ]
    #     )

    return card