
import flet as ft

# Clase de las tareas y lo que hay dentro de ellas, así como su edición y eliminación
class Tareas(ft.Column):
    def __init__(self,tarea_nombre,tarea_eliminar):
        super().__init__()
        self.tarea_nombre = tarea_nombre
        self.tarea_eliminar = tarea_eliminar
        self.tarea_vista = ft.Checkbox(value=False,label=tarea_nombre)
        self.edicion_nombre = ft.TextField(expand=1)

        self.vista_pantalla = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.tarea_vista,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.EDIT,
                            tooltip="Editar",
                            on_click=self.editar_tarea
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            tooltip="Eliminar",
                            on_click=self.eliminar_tarea
                        )
                    ]
                )
            ]
        )
    
        self.vista_edicion = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edicion_nombre,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Actualizar tarea",
                    on_click=self.guardar_tarea,
                ),
            ],
        )
        self.controls = [self.vista_pantalla,self.vista_edicion]

    def editar_tarea(self,e):
        self.edicion_nombre.value = self.tarea_vista.label
        self.vista_pantalla.visible = False
        self.vista_edicion.visible = True
        self.update()

    def guardar_tarea(self,e):
        self.tarea_vista.label = self.edicion_nombre.value
        self.vista_pantalla.visible = True
        self.vista_edicion.visible = False
        self.update()

    def eliminar_tarea(self,e):
        self.tarea_eliminar(self)

# Clase de la lista de tareas
class ListaDeTareas(ft.Column):
    def __init__(self,):
        super().__init__()
        self.tareas = ft.TextField(hint_text="Tarea a realizar",expand=True)
        self.vista_tareas = ft.Column()
        self.width=600
        self.controls=[
                        ft.Row(
                        controls=[
                            self.tareas,
                            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.agregar_tarea)
                        ]
                    ),self.vista_tareas]
        
    # Función de agregar tarea
    def agregar_tarea(self,e):
        tarea = Tareas(self.tareas.value,self.borrar_tareas)
        self.vista_tareas.controls.append(tarea)
        self.tareas.value = ""
        self.update()
    
    def borrar_tareas(self,tarea):
        self.vista_tareas.controls.remove(tarea)
        self.update()

def main(page: ft.Page):
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 600
    page.window.width = 400
    page.title = "Lista de Tareas"
    # Iniciar, por default, en modo luz
    page.theme_mode = ft.ThemeMode.LIGHT
    # Agregar efecto de cambio progesivo de tema
    #page.overlay.append(ft.ProgressBar(visible=False))
    page.update()

    # Función para alternar el tema y mostrar la barra de progreso
    def cambiar_estado(e):

        # Mostrar la barra de progreso

        #page.overlay.append(ft.ProgressBar(visible=True))

        # Alternar entre tema CLARO y OSCURO

        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

        # Cambia el icono del boton OSCURO a CLARO

        boton_cambiar_tema.selected = not boton_cambiar_tema.selected
        
        # Ocultar la barra de progreso

        #page.overlay.pop() # Permite el cambio de vista sin mostrar la barra de carga.
        #page.overlay.append(ft.ProgressBar(visible=False))
        page.update()
    
    boton_cambiar_tema = ft.IconButton(
        on_click=cambiar_estado,
        icon=ft.icons.DARK_MODE,
        selected_icon=ft.icons.LIGHT_MODE,
        style=ft.ButtonStyle(
            # Cambiar de color, por ligth o dark
            color={"":ft.colors.BLACK,"selected":ft.colors.WHITE},
        )
    )

    barra_de_navegacion = ft.AppBar(
        title=ft.Text("Lista de Tareas"),
        bgcolor=ft.colors.TRANSPARENT,
        leading=ft.IconButton(ft.icons.MENU),
        actions=[
            boton_cambiar_tema
        ],
    )

    lista_de_tareas = ListaDeTareas()

    page.add(barra_de_navegacion,lista_de_tareas)

ft.app(target=main)