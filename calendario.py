import datetime
import flet as ft
import calendar
from calendar import HTMLCalendar
from dateutil import relativedelta

class FletCalendar(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page=page
        self.get_current_date() # Funciones
        self.set_theme()

        # Init del container de control
        self.calendar_container=ft.Container(
            width=355,height=300,padding=ft.padding.all(2),
            border=ft.border.all(2,self.border_color),
            border_radius=ft.border_radius.all(10),
            alignment=ft.alignment.bottom_center
        )
        self.build() # Contruye el calendario
        self.output=ft.Text() # Agregar salida de control
    
    def get_current_date(self):
        # Toma la fecha inicial
        today = datetime.datetime.today() # Toma el día de hoy
        self.current_month = today.month
        self.curren_day = today.day
        self.current_year = today.year

    def selected_date(self,e):
        # Selección de la fecha, hecha por el usuario
        self.output.value = e.control.data
        self.output.update()

    def set_current_date(self):
        # Pone la fecha actual en el calendario
        today=datetime.datetime.today()
        self.current_month = today.month
        self.curren_day = today.day
        self.current_year = today.year
        self.build()
        self.calendar_container.update()

    def get_next(self,e):
        # Moverse para el siguiente mes
        current = datetime.date(self.current_year,self.current_month,self.curren_day)
        add_month = relativedelta.relativedelta(month=1)
        nex_month =  current + add_month

        self.current_month =nex_month.month
        self.curren_day =nex_month.day
        self.current_year =nex_month.year
        self.build()
        self.calendar_container.update()

    def get_prev(self):
        # Moverse para el anterior mes
        current = datetime.date(self.current_year,self.current_month,self.curren_day)
        add_month = relativedelta.relativedelta(month=1)
        nex_month =  current - add_month
        self.current_month =nex_month.month
        self.curren_day =nex_month.day
        self.current_year =nex_month.year
        self.build()
        self.calendar_container.update()

    def get_calendar(self):
        # Obtener el calendario desde el módulo Calendar
        cal = HTMLCalendar()
        return cal.monthdayscalendar(self.current_year,self.current_month)
    
    def set_theme(self, border_color=ft.colors.PINK_700,
                text_color=ft.colors.pink_50, 
                current_day_color=ft.colors.PINK_700):
        self.border_color=border_color
        self.text_color=text_color
        self.current_day_color=current_day_color

    def build(self):
        # Contrucción del calendario
        current_calendar = self.get_calendar()
        str_date = '{0} {1}, {2}'.format(calendar.month_name[self.current_month],self.curren_day,self.current_year)

        date_display=ft.Text(str_date,text_align=ft.TextAlign.CENTER,size=20,color=self.text_color)
        next_button = ft.Container(ft.Text('>',text_align=ft.TextAlign.RIGHT,size=20,color=self.text_color ),on_click=self.get_next)
        div = ft.Divider(height=1,thickness=2.0,color=self.border_color)
        prev_button = ft.Container(ft.Text('<',text_align=ft.TextAlign.LEFT,size=20,color=self.text_color ),on_click=self.get_prev)

        calendar_column = ft.Column(
            controls=[
                ft.Row(controls=[
                    prev_button, date_display,next_button
                ],alignment=ft.MainAxisAlignment.SPACE_EVENLY, vertical_alignment=ft.CrossAxisAlignment.CENTER,
                height=40,expand=False),div
            ], spacing=2,width=355,height=330,alignment=ft.MainAxisAlignment.START,expand=False
        )

        # Bucle de semanas y agregar Row
        for week in current_calendar:
            week_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
            # Bucle de días y agregar días a Row
            for day in week:
                if day > 8:
                    is_current_day_font = ft.FontWeight.W_300
                    is_current_day_bg = ft.colors.TRANSPARENT
                    display_day = str(day)
                    if len(str(display_day)) == 1: display_day = '0%s' % display_day

def main(page: ft.Page):
    pass

ft.app(target=main)