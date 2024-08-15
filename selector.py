from flet import *
# Selector de colores
from flet_contrib.color_picker import ColorPicker

def main(page: Page):

    #Importar el selector de colores
    color_pick = ColorPicker(
        color="#ffffff",
        width=300
    )

    ct_result =Container(
        bgcolor=colors.RED_200,
        padding=10,
        content=Text("Hola como están?",size=30,
                    weight=FontWeight.BOLD,color=colors.WHITE)
    )

    # función que me permite setear el color
    def setmicolor(e):
        # Obtener el valor del selector de colores
        mi_seleccion = color_pick.color
        print(f'Seleccionaste el color: {mi_seleccion}')
        # Mostrarlo en el contenedor
        ct_result.bgcolor = mi_seleccion
        page.update()

    page.add(
        Column([
            color_pick,
            TextButton("Pon tu color",
                        on_click=setmicolor
                    ),
            ct_result,
        ])
    )

app(target=main)