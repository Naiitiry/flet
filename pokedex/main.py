import flet as ft
# Como se va a utilizar una API, hay que realizar los "ASYNC" y "AWAIT"
async def main(page: ft.Page):

    page.window.width = 720
    page.window.height = 1000
    page.window.resizable = True
    page.padding = 0


    # Elementos dentro de items_superior

    btn_azul = ft.Stack([
        ft.Container(width=80,height=80,bgcolor=ft.colors.WHITE,border_radius=50),
        ft.Container(width=70,height=70,top=5,left=5,bgcolor=ft.colors.BLUE,border_radius=50)
    ])

    # Elementos dentro de superior

    items_superior = [
        ft.Container(btn_azul,width=80,height=80),
        ft.Container(width=40,height=40, bgcolor=ft.colors.RED_200, border_radius=50),
        ft.Container(width=40,height=40, bgcolor=ft.colors.YELLOW, border_radius=50),
        ft.Container(width=40,height=40, bgcolor=ft.colors.GREEN, border_radius=50)
    ]
    
    # Elementas dentro de centro

    stack_central = ft.Stack([
        ft.Container(width=500,height=300,bgcolor=ft.colors.WHITE),
        ft.Container(width=450,height=250,bgcolor=ft.colors.BLACK, top=25, left=25),
        ft.Image(
            src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10002.png",
            scale=4,
            width=50,
            height=50,
            top=250/2,
            right=450/2
        )
    ])

    superior = ft.Container(content=ft.Row(items_superior),width=600,height=80,margin=ft.margin.only(top=40))
    centro = ft.Container(content=stack_central,width=600,height=400,margin=ft.margin.only(top=40), 
                            alignment=ft.alignment.center)
    inferior = ft.Container(width=600,height=400,margin=ft.margin.only(top=40), border=ft.border.all())

    # Elementos dentro del contenedor

    col = ft.Column(spacing=0,controls=[
        superior,
        centro,
        inferior
    ])

    # Contenedor
    contenedor = ft.Container(
        col,
        width=720,
        height=1280,
        bgcolor="red",
        alignment=ft.alignment.top_center
    )


    page.add(contenedor)

ft.app(target=main)