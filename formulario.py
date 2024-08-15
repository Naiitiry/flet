import flet as ft

def main(page: ft.Page):
    page.title = "Formulario"
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False
    page.padding = 50
    page.theme_mode = ft.ThemeMode.DARK

    nombre = ft.TextField(label="Nombre")
    apellido = ft.TextField(label="Apellido")
    email = ft.TextField(label="Email",keyboard_type=ft.KeyboardType.EMAIL)
    area_texto = ft.TextField(label="Comantarios",multiline=True)

    def enviar_formulario(e):
        nombre_val = nombre.value
        apellido_val = apellido.value
        email_val = email.value
        area_texto_val = area_texto.value

        # Mostrar los valores en la consola o hacer algo con ellos
        print(f"Nombre: {nombre_val}")
        print(f"Apellido: {apellido_val}")
        print(f"Correo electrónico: {email_val}")
        print(f"Comentarios: {area_texto_val}")

        page.add(

            ft.Text(f"Gracias por enviar el formulario, {nombre_val}")
        )

        nombre.value = ""
        apellido.value = ""
        email.value = ""
        area_texto.value = ""
        page.update()

    enviar_boton = ft.ElevatedButton("Enviar", on_click=enviar_formulario)

    page.add(
        nombre,
        apellido,
        email,
        area_texto,
        enviar_boton
    )

ft.app(target=main)