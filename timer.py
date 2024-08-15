import time
import flet as ft

def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    timer_picker_value_ref = ft.Ref[ft.Text]()
    countdown_text_ref = ft.Ref[ft.Text]()
    timer_value_in_seconds = 3600  # Valor por defecto del temporizador (1 hora)

    def handle_timer_picker_change(e):
        nonlocal timer_value_in_seconds
        timer_value_in_seconds = int(e.data)
        timer_picker_value_ref.current.value = time.strftime("%H:%M:%S", time.gmtime(timer_value_in_seconds))
        page.update()

    def start_countdown(e):
        nonlocal timer_value_in_seconds
        for remaining_time in range(timer_value_in_seconds, -1, -1):
            countdown_text_ref.current.value = time.strftime("%H:%M:%S", time.gmtime(remaining_time))
            page.update()
            time.sleep(1)

    cupertino_timer_picker = ft.CupertinoTimerPicker(
        value=3600,
        second_interval=10,
        minute_interval=1,
        mode=ft.CupertinoTimerPickerMode.HOUR_MINUTE_SECONDS,
        on_change=handle_timer_picker_change,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    tight=True,
                    controls=[
                        ft.Text("TimerPicker Value:", size=23),
                        ft.CupertinoButton(
                            content=ft.Text(
                                ref=timer_picker_value_ref,
                                value="01:00:00",
                                size=23,
                                color=ft.cupertino_colors.DESTRUCTIVE_RED,
                            ),
                            on_click=lambda e: page.open(
                                ft.CupertinoBottomSheet(
                                    cupertino_timer_picker,
                                    height=216,
                                    padding=ft.padding.only(top=6),
                                )
                            ),
                        ),
                    ],
                ),
                ft.Text(ref=countdown_text_ref, value="00:00:00", size=30, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton("Start Countdown", on_click=start_countdown),
            ],
        ),
    )

ft.app(target=main)
