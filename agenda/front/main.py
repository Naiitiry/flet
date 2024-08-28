import flet as ft
from auth.login import login_page
from auth.register import register_page
from home.home import home_page

def main(page: ft.Page):
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False

    def show_login_page(e=None):
        page.controls.clear()
        login_page(page, show_register_page)
        page.update()

    def show_register_page(e=None):
        page.controls.clear()
        register_page(page, show_login_page)
        page.update()

    def show_home_page(e=None):
        page.controls.clear()
        home_page(page)
        page.update()

    def on_route_change(route):
        if route == "/home/home":
            if page.session.get("logged_in"):
                show_home_page()
            else:
                show_login_page()
        elif route == "/auth/login":
            show_login_page()
        elif route == "/auth/register":
            show_register_page()
        else:
            show_login_page()

    def logout(e=None):
        page.session.clear()
        page.go("/auth/login")

    page.on_route_change = on_route_change
    page.route = "/auth/login"
    page.update()

ft.app(target=main)
