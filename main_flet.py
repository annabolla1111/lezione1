#main grafico
import flet as ft

from gestionale.controller import Controller
from gestionale.view import View


def main(page: ft.Page): #ci creiamo gli ogg e gli facciamo parlare
    v = View(page) #creo il view da solo, cosi saprà dove scrivere le cose
    c = Controller(v)  # creo il cntroller passandogli il view
    v.set_controller(c)  #creo il set in view
    v.carica_interfaccia()

ft.app(target = main) #chiamata al metodo app di flet