import flet as ft


def main(page: ft.Page):

    es_presionado=False
    text = ft.Text('Botón sin presionar')
    def presion_del_boton(e):
        nonlocal es_presionado
        if es_presionado:
            text.value = 'Botón sin presionar'
        else:
            text.value = "Botón presionado"
        es_presionado = not es_presionado
        page.update()


    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                        text,
                        ft.ElevatedButton("Presionar", 
                                        on_click=presion_del_boton),
                ]
            )
        ]
    )

    page.add(
        view
    )

ft.app(target=main)