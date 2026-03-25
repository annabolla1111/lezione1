#main grafico
import flet as ft

from gestionale.controller import Controller
from gestionale.view import View


def main(page: ft.Page): #ci creiamo gli ogg e gli facciamo parlare
    v = View() #creo il view da solo
    c = Controller(v)  # creo il cntroller passandogli il view
    v.set_controller()  #creo il set in view

ft.app(target = main) #chiamata al metodo app di flet