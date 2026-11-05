#----Module Imports----
import flet as ft
import string
import secrets

#------Main Function------
def main(page: ft.Page):
    page.title = 'My Password Generator v1.0'
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 600
    page.window.center()
    page.window.maximizable = False
    page.window.resizable = False

    #------Generate Password Function------
    def generate_password():
        s1 = string.ascii_uppercase
        s2 = string.ascii_lowercase
        s3 = string.digits
        s4 = string.punctuation

        state1 = c1.value
        state2 = c2.value
        state3 = c3.value
        state4 = c4.value

        st = ''
        if state1:
            st += s1
        if state2:
            st += s2
        if state3:
            st += s3
        if state4:
            st += s4

        len_pass = int(slider.value)

        if st == '':
            t1.value = 'Please select at least one option'
            page.update()
            return

        while True:
            pg = ''
            for i in range(len_pass):
                pg += secrets.choice(st)
            if (not state1 or any([s in s1 for s in pg])) and \
               (not state2 or any([s in s2 for s in pg])) and \
               (not state3 or any([s in s3 for s in pg])) and \
               (not state4 or any([s in s4 for s in pg])):
                break
        t1.value = pg
        page.update()

    #------Rows------
    # row0
    t1 = ft.TextField('Your Generated Password :', read_only=True, bgcolor='#1B1D2B', color='#FFFFFF', width=350, height=50)
    r0 = ft.Row(controls=[t1], alignment=ft.MainAxisAlignment.CENTER)

    # row1
    c1 = ft.Checkbox(label='UpperCase', value=True)
    r1 = ft.Row(controls=[c1], alignment=ft.MainAxisAlignment.CENTER, wrap=True)

    # row2
    c2 = ft.Checkbox(label='LowerCase', value=True)
    r2 = ft.Row(controls=[c2], alignment=ft.MainAxisAlignment.CENTER, wrap=True)

    # row3
    c3 = ft.Checkbox(label='Digits', value=True)
    r3 = ft.Row(controls=[c3], alignment=ft.MainAxisAlignment.CENTER, wrap=True)

    # row4
    c4 = ft.Checkbox(label='Punctuation', value=True)
    r4 = ft.Row(controls=[c4], alignment=ft.MainAxisAlignment.CENTER, wrap=True)

    # row5
    slider = ft.Slider(min=4, max=30, divisions=26, value=8, label='{value}', on_change=lambda e: page.update(), expand=True)
    r5 = ft.Row(controls=[ft.Text('LenPass:'), ft.Text('4'), slider, ft.Text('30')], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=5)

    # row6
    exit = ft.ElevatedButton(text='Exit', bgcolor="#6548C8", color="#050505", width=100, height=50, on_click=lambda e: page.window.destroy())
    generate = ft.ElevatedButton(text='Generate', bgcolor="#6548C8", color="#050505", width=100, height=50, on_click=lambda e: generate_password())
    r6 = ft.Row(controls=[exit, generate], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    # row7
    nametag = ft.Text('Created by Amir Mahdi Zamani with ❤', color='#6548C8', size=15, weight=ft.FontWeight.BOLD)
    r7 = ft.Row(controls=[nametag], alignment=ft.MainAxisAlignment.CENTER)

    page.add(r0, r1, r2, r3, r4, r5, r6, r7)
    page.update()


ft.app(target=main)
