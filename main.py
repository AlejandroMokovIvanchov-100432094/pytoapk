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
import csv
import json

from pagina_consultas import SeccionConsultas
from pagina_ratios import SeccionRatios
from pagina_recetas import SeccionRecetas
from pagina_recetas_custom import SeccionRecetasCustom
from anadir_alimento import SeccionAnadirAlimento



class Alimento:
    def __init__(self, nombre, calorias, hc, azucares, proteinas, grasas, grupo):
        self.nombre = nombre
        self.calorias = calorias
        self.hc = hc
        self.azucares = azucares
        self.proteinas = proteinas
        self.grasas = grasas
        self.grupo = grupo


class MiApp(App):
    def build(self):
        Window.size = (800,1200)
        # Crea una caja vertical (BoxLayout)
        self.main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.main_page = GridLayout(cols=1, spacing=10, padding=10)
        with self.main_layout.canvas.before:
            Color(0.65, 0.65, 0.65, 0.6)  # RGBA (valores entre 0 y 1)
            self.rect = Rectangle(size=self.main_layout.size, pos=self.main_layout.pos)
        self.main_layout.bind(size=self.update_rect)
        self.menu_principal()
        return self.main_layout

    def menu_principal(self):
        self.btn_infnut = Button(text='Consultar información de un alimento', on_press=self.pagina_informacion_nutricional, height = Window.height*0.1, size_hint_y =None)
        self.btn_recetas = Button(text='Hacer recetas', on_press=self.pagina_recetas, height = Window.height*0.1, size_hint_y =None)
        self.btn_recetas_custom = Button(text='Hacer recetas personalizadas', on_press=self.pag_recetas_custom, height=Window.height * 0.1,size_hint_y=None)
        self.btn_ratios = Button(text='Definir ratios de insulina', on_press=self.pag_ratios, height = Window.height*0.1, size_hint_y =None)
        self.anadir_alimento = Button(text='Añadir alimento a la base de datos',height=Window.height * 0.1, size_hint_y=None, on_press = self.pag_anadir_alimento)
        self.btn_exit = Button(text='Salir', on_press=self.exit_app,height=Window.height * 0.1, size_hint_y=None,
                               background_color=(2,2,2,1), color = (0,0,0,1))
        self.main_page.add_widget(self.btn_infnut)
        self.main_page.add_widget(self.btn_recetas)
        self.main_page.add_widget(self.btn_recetas_custom)
        self.main_page.add_widget(self.anadir_alimento)
        self.main_page.add_widget(self.btn_ratios)
        self.main_page.add_widget(self.btn_exit)
        self.main_layout.add_widget(self.main_page)

    def exit_app(self, instance):
        App.get_running_app().stop()

    def pag_anadir_alimento(self, instance):
        self.main_layout.remove_widget(self.main_page)
        seccion = SeccionAnadirAlimento(self.main_layout,self.main_page)
        seccion.pagina_prncipal()

    def pagina_recetas(self, instance):
        self.main_layout.remove_widget(self.main_page)
        seccion = SeccionRecetas(self.main_layout, self.main_page)
        seccion.pagina_principal()

    def pagina_informacion_nutricional(self, instance):
        self.main_layout.remove_widget(self.main_page)
        seccion = SeccionConsultas(self.main_layout, self.main_page)
        seccion.pagina_principal()

    def leer_alimentos(self):
        self.alimentos = []
        with open("alimentos.csv", newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                alimento = Alimento(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                self.alimentos.append(alimento)

    def update_rect(self, instance, value):
        # Actualiza el tamaño y la posición del Rectangle al cambiar el tamaño de la ventana
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def pag_ratios(self, instance):
        self.main_layout.remove_widget(self.main_page)
        seccion = SeccionRatios(self.main_layout, self.main_page)
        seccion.pagina_principal()

    def pag_recetas_custom(self, instance):
        self.main_layout.remove_widget(self.main_page)
        seccion = SeccionRecetasCustom(self.main_layout,self.main_page)
        seccion.pagina_principal()



if __name__ == '__main__':
    MiApp().run()


