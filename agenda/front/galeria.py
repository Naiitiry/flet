import flet as ft

def main(page: ft.Page):
    # Características de la página
    page.title = "Galería de imagenes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 15
    page.window.height = 500
    page.window.width = 500

    # {e.control.content.src} fuente de las imagenes

    imagen_ampliada_container = ft.Container()
    # Funciones
    def agrandar_imagen(e):
        # Verifica si, antes de seleccionar una imagen hay alguna otra previamente.
        if imagen_ampliada_container in page.controls:
            page.controls.remove(imagen_ampliada_container)
        # Crear contenedor de pantalla completa para la imagen seleccionada
        imagen_ampliada_container.content = ft.Container(
            height=page.window.height,
            width=page.window.width,
            bgcolor=ft.colors.AMBER_50,
            alignment=ft.alignment.center,
            animate_opacity=200,
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=e.control.content.src,
                        fit=ft.ImageFit.CONTAIN,
                        height=200,
                        border_radius=ft.border_radius.all(10),
                        animate_scale=ft.animation.Animation(400)
                    ),
                    ft.TextButton(
                        "Cerrar",
                        on_click=lambda _: page.controls.remove(imagen_ampliada_container) or page.update(),
                        style=ft.ButtonStyle(
                            overlay_color=ft.colors.TRANSPARENT
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        # Añade el contenedor con la imagen ampliada a la página
        page.controls.append(imagen_ampliada_container)
        page.update()


    # Características de las imagenes
    imagenes = ft.GridView(
        expand=1,
        runs_count = 5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    page.add(imagenes)

    for i in range(0,60):
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