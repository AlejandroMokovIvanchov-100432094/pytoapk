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
    def __init__(self, nombre, hc, cantidad):
        self.nombre = nombre
        self.hc = hc
        self.cantidad = cantidad


class SeccionRecetasCustom:
    def __init__(self, main_layout, main_page):
        self.main_layout = main_layout
        self.main_page = main_page
        self.back_btn_size = (Window.width * 0.5, Window.width * 0.1)
        self.ingredientes = []

    def pagina_principal(self):
        self.layout_recetas_custom = GridLayout(cols = 1, spacing = 10)
        self.layout_ingredientes = GridLayout(cols=1, spacing=10, height=Window.height * 0.6, size_hint_y=None)
        self.back_btn = Button(text='Volver', on_press=partial(self.back_btn_recetas_custom, self),
                               height=self.back_btn_size[1], size_hint_y=None,
                               background_color=(2, 2, 2, 1), color=(0, 0, 0, 1))
        self.layout_recetas_custom.add_widget(self.back_btn)
        self.scroll_view = ScrollView()
        self.add_ingrediente = Button(text='Anadir ingrediente', on_press = self.anadir_ingrediente,
                               height=self.back_btn_size[1], size_hint_y=None,
                               background_color=(2, 2, 2, 1), color=(0, 0, 0, 1))
        self.layout_recetas_custom.add_widget(self.add_ingrediente)
        self.eliminar_ingredientes = Button(text='Eliminar ingredientes', on_press=self.delete_ingredientes,
                                      height=self.back_btn_size[1], size_hint_y=None,
                                      background_color=(2, 2, 2, 1), color=(0, 0, 0, 1))
        self.layout_recetas_custom.add_widget(self.eliminar_ingredientes)
        self.btn_calcular_totales = Button(text='Calcular carbohidratos totales', on_press = self.calcular_totales,
                                      height=self.back_btn_size[1], size_hint_y=None,
                                      background_color=(2, 2, 2, 1), color=(0, 0, 0, 1))
        self.layout_recetas_custom.add_widget(self.btn_calcular_totales)
        self.btn_calcular_insulina = Button(text='Calcular insulina necesaria', on_press = self.calcular_insulina,
                                           height=self.back_btn_size[1], size_hint_y=None,
                                           background_color=(2, 2, 2, 1), color=(0, 0, 0, 1))
        self.layout_recetas_custom.add_widget(self.btn_calcular_insulina)
        self.scroll_view.add_widget(self.layout_ingredientes)
        self.layout_recetas_custom.add_widget(self.scroll_view)
        self.main_layout.add_widget(self.layout_recetas_custom)

    def anadir_ingrediente(self, instance):
        self.layout_ingrediente = GridLayout(cols = 4, spacing = 10, height=self.back_btn_size[1]*0.7, size_hint_y=None)
        self.nombre_ingrediente = TextInput(hint_text = "Nombre")
        self.hc_ingrediente = TextInput(hint_text="Hidratos de carbono por 100g")
        self.cantidad_ingrediente = TextInput(hint_text="Cantidad")
        self.boton_anadir = Button(text = "Anadir", on_press = self.anadir_a_lista)

        self.layout_ingrediente.add_widget(self.nombre_ingrediente)
        self.layout_ingrediente.add_widget(self.hc_ingrediente)
        self.layout_ingrediente.add_widget(self.cantidad_ingrediente)
        self.layout_ingrediente.add_widget(self.boton_anadir)
        self.layout_ingredientes.add_widget(self.layout_ingrediente)

    def delete_ingredientes(self, instance):
        self.layout_ingredientes.clear_widgets()

    def anadir_a_lista(self, instance):
        if self.nombre_ingrediente.text == "":
            nombre_ingrediente = ""
        else:
            nombre_ingrediente = self.nombre_ingrediente.text

        if self.hc_ingrediente.text == "":
            hc_ingrediente = 0
        else:
            hc_ingrediente = float(self.hc_ingrediente.text)

        if self.cantidad_ingrediente.text == "":
            cantidad_ingrediente = 0
        else:
            cantidad_ingrediente = float(self.cantidad_ingrediente.text)

        self.ingredientes.append(Alimento(nombre_ingrediente, hc_ingrediente, cantidad_ingrediente))


    def calcular_totales(self, instance):
        self.hc_count = 0
        for ingrediente in self.ingredientes:
            self.hc_count += ingrediente.hc*ingrediente.cantidad/100
        self.layout_hc_totales = GridLayout(cols = 2, spacing = 10, height=self.back_btn_size[1], size_hint_y=None)
        self.carbohidratos_receta_custom = Label(text = "Carbohidratos totales de la receta:")
        self.carbohidratos_receta_custom_valor = Label(text=str(self.hc_count) + " gramos")
        self.layout_hc_totales.add_widget(self.carbohidratos_receta_custom)
        self.layout_hc_totales.add_widget(self.carbohidratos_receta_custom_valor)
        if self.layout_hc_totales not in self.layout_ingredientes.children:
            self.layout_ingredientes.add_widget(self.layout_hc_totales)

    def calcular_insulina(self, instance):
        self.layout_insulina = GridLayout(cols = 2)

        insulina_desayuno = Label(text = "Insulina desayuno: ", height=self.back_btn_size[1]*0.5,size_hint_y=None)
        insulina_desayuno_boton = Button(text= "Calcular unidades desayuno", height=self.back_btn_size[1]*0.5,size_hint_y=None, on_press = self.add_widget_desayuno)
        insulina_comida = Label(text="Insulina comida: ", height=self.back_btn_size[1]*0.5,size_hint_y=None)
        insulina_comida_boton = Button(text= "Calcular unidades comida", height=self.back_btn_size[1]*0.5,size_hint_y=None, on_press = self.add_widget_comida)
        insulina_cena = Label(text="Insulina cena: ", height=self.back_btn_size[1]*0.5,size_hint_y=None)
        insulina_cena_boton = Button(text="Calcular unidades cena", height=self.back_btn_size[1]*0.5,size_hint_y=None, on_press = self.add_widget_cena)

        self.layout_insulina.add_widget(insulina_desayuno)
        self.layout_insulina.add_widget(insulina_desayuno_boton)

        self.layout_insulina.add_widget(insulina_comida)
        self.layout_insulina.add_widget(insulina_comida_boton)

        self.layout_insulina.add_widget(insulina_cena)
        self.layout_insulina.add_widget(insulina_cena_boton)

        self.layout_ingredientes.add_widget(self.layout_insulina)

    def add_widget_desayuno(self, instance):
        hc = self.hc_count
        ratio_desayuno, ratio_comida, ratio_cena = self.leer_ratios()


        unidades_necesarias_desayuno = round(hc / 10 * ratio_desayuno, 2)
        insulina_desayuno_2 = Label(text="Insulina desayuno: ", height=self.back_btn_size[1] * 0.5, size_hint_y=None)
        self.insulina_desayuno_valor = Label(text=str(unidades_necesarias_desayuno) + " unidades",
                                        height=self.back_btn_size[1] * 0.5, size_hint_y=None)

        self.layout_insulina.add_widget(insulina_desayuno_2)
        self.layout_insulina.add_widget(self.insulina_desayuno_valor)

    def add_widget_comida(self, instance):
        hc = self.hc_count
        ratio_desayuno, ratio_comida, ratio_cena = self.leer_ratios()

        unidades_necesarias_comida = round(hc / 10 * ratio_comida, 2)

        insulina_comida_2 = Label(text="Insulina comida: ", height=self.back_btn_size[1] * 0.5, size_hint_y=None)
        self.insulina_comida_valor = Label(text=str(unidades_necesarias_comida) + " unidades", height=self.back_btn_size[1] * 0.5,
                                      size_hint_y=None)

        self.layout_insulina.add_widget(insulina_comida_2)
        self.layout_insulina.add_widget(self.insulina_comida_valor)

    def add_widget_cena(self, instance):
        hc = self.hc_count
        ratio_desayuno, ratio_comida, ratio_cena = self.leer_ratios()

        unidades_necesarias_cena = round(hc / 10 * ratio_cena, 2)

        insulina_cena_2 = Label(text="Insulina cena: ", height=self.back_btn_size[1] * 0.5, size_hint_y=None)
        self.insulina_cena_valor = Label(text=str(unidades_necesarias_cena) + " unidades", height=self.back_btn_size[1] * 0.5,
                                    size_hint_y=None)

        if self.insulina_cena_valor not in self.layout_insulina.children:
            self.layout_insulina.add_widget(insulina_cena_2)
            self.layout_insulina.add_widget(self.insulina_cena_valor)
        else:
            # Si los labels ya están presentes, los eliminamos
            self.layout_insulina.remove_widget(insulina_cena_2)
            self.layout_insulina.remove_widget(self.insulina_cena_valor)

    def leer_ratios(self):
        with open("ratios.json", 'r') as archivo:
            try:
                ratios_cargados = json.load(archivo)
            except json.JSONDecodeError:
                ratios_cargados = {}
            if ratios_cargados:
                ratio_desayuno = ratios_cargados["desayuno"]
                ratio_comida = ratios_cargados["comida"]
                ratio_cena = ratios_cargados["cena"]

        return round(float(ratio_desayuno),2), round(float(ratio_comida),2), round(float(ratio_cena),2)

    def back_btn_recetas_custom(self, instance, *args):
        self.ingredientes = []
        self.main_layout.remove_widget(self.layout_recetas_custom)
        self.main_layout.add_widget(self.main_page)