from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from functools import partial
import csv
import json

class Alimento:
    def __init__(self, nombre, calorias, hc, azucares, proteinas, grasas, grupo):
        self.nombre = nombre
        self.calorias = calorias
        self.hc = hc
        self.azucares = azucares
        self.proteinas = proteinas
        self.grasas = grasas
        self.grupo = grupo

class SeccionAnadirAlimento:
    def __init__(self,main_layout,main_page):
        self.main_layout = main_layout
        self.main_page = main_page
    def pagina_prncipal(self):
        self.layout_anadir_alimento = GridLayout(cols = 1, spacing = 10)
        self.back_btn = Button(text='Volver', on_press=partial(self.back_btn_anadir, self),
                               height=Window.height*0.1, size_hint_y=None,
                               background_color=(2, 2, 2, 1), color=(0, 0, 0, 1))
        self.layout_anadir_alimento.add_widget(self.back_btn)

        self.nombre_valor = TextInput(hint_text="Nombre: ", height = Window.height * 0.07, size_hint_y = None, font_size = Window.height * 0.05)
        self.calorias_valor = TextInput(hint_text="Calorias: ", height = Window.height * 0.07, size_hint_y = None, font_size = Window.height * 0.05)
        self.hc_valor = TextInput(hint_text="Hidratos de carbono: ", height = Window.height * 0.07, size_hint_y = None, font_size = Window.height * 0.05)
        self.azucares_valor = TextInput(hint_text="de los cuales azucares: ", height = Window.height * 0.07, size_hint_y = None, font_size = Window.height * 0.05)
        self.proteinas_valor = TextInput(hint_text="Proteinas: ", height = Window.height * 0.07, size_hint_y = None, font_size = Window.height * 0.05)
        self.grasas_valor = TextInput(hint_text="Grasas: ", height = Window.height * 0.07, size_hint_y = None, font_size = Window.height * 0.05)
        self.grupo_valor = TextInput(hint_text="Grupo: ", height = Window.height * 0.07, size_hint_y = None, font_size = Window.height * 0.05)

        self.layout_anadir_alimento.add_widget(self.nombre_valor)
        self.layout_anadir_alimento.add_widget(self.calorias_valor)
        self.layout_anadir_alimento.add_widget(self.hc_valor)
        self.layout_anadir_alimento.add_widget(self.azucares_valor)
        self.layout_anadir_alimento.add_widget(self.proteinas_valor)
        self.layout_anadir_alimento.add_widget(self.grasas_valor)
        self.layout_anadir_alimento.add_widget(self.grupo_valor)

        self.btn_anadir_ingrediente = Button(text='Anadir ingrediente', on_press=self.anadir_a_csv,
                               height=Window.height * 0.1, size_hint_y=None,
                               background_color=(2, 2, 2, 1), color=(0, 0, 0, 1))
        self.layout_anadir_alimento.add_widget(self.btn_anadir_ingrediente)

        self.main_layout.add_widget(self.layout_anadir_alimento)

    def anadir_a_csv(self, instance):
        nombre = self.nombre_valor.text
        calorias = self.calorias_valor.text
        hc = self.hc_valor.text
        azucares = self.azucares_valor.text
        proteinas = self.proteinas_valor.text
        grasas = self.grasas_valor.text
        grupo = self.grupo_valor.text
        with open('alimentos.csv', mode='a', newline="\n") as csvfile:
            write = csv.writer(csvfile,delimiter = ",")
            write.writerow([nombre,calorias,hc,azucares,proteinas,grasas,grupo])

    def back_btn_anadir(self, instance, *args):
        self.main_layout.remove_widget(self.layout_anadir_alimento)
        self.main_layout.add_widget(self.main_page)