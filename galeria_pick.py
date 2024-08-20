import flet as ft

def main(page: ft.Page):
    # Características de la página
    page.title = "Galería de imágenes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 15

    # Función para cerrar el modal
    def cerrar_modal(e):
        modal.open = False
        page.update()

    # Crear el modal
    modal = ft.AlertDialog(
        modal=True,
        content=ft.Container(
            width=300,
            height=300,
            bgcolor=ft.colors.TRANSPARENT,
            content=ft.Image(
                src="",
                fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(10),
            ),
        ),
        actions=[
            ft.TextButton("Cerrar", on_click=cerrar_modal),
        ],
    )

    # Función para agrandar la imagen en el modal
    def agrandar_imagen(e):
        modal.content.content.src = e.control.content.src
        modal.open = True
        page.overlay.append(modal)
        page.update()

    # Características de las imágenes
    imagenes = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    page.add(imagenes)

    for i in range(0, 60):
        imagenes.controls.append(
            ft.Container(
                width=150,
                height=150,
                on_click=agrandar_imagen,
                content=ft.Image(
                    src=f"https://picsum.photos/150/150?{i}",
                    fit=ft.ImageFit.NONE,
                    border_radius=ft.border_radius.all(10),
                ),
                animate=ft.animation.Animation(400),
            )
        )

    page.update()

ft.app(target=main)
