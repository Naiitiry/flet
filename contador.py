import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_numero = ft.TextField(value='0',text_align=ft.TextAlign.CENTER,width=100)

    def incrementar(e):
        txt_numero.value = str(int(txt_numero.value) + 1)
        page.update()

    def decrementar(e):
        txt_numero.value = str(int(txt_numero.value)-1)
        page.update()

    page.add(
        ft.Row([
            ft.ElevatedButton(ft.icons.REMOVE,on_click=decrementar),
            txt_numero,
            ft.ElevatedButton(ft.icons.ADD,on_click=incrementar)
        ],alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)