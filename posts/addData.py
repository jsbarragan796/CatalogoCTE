# -- coding: utf-8 --
from unittest import TestCase

from faker import Faker
from selenium import webdriver


class FunctionalTest(TestCase):
    global URL
    # URL = 'https://catalogodevelop.herokuapp.com/'
    URL = 'http://127.0.0.1:8000/'
    #URL = 'https://catalogocte.herokuapp.com/'

    def setUp(self):
        # self.browser = webdriver.Chrome("C:\\Users\\chromedriver.exe")
        # Sebastian añada su ruta por tener mac :c, para el chromedriver
        self.browser = webdriver.Chrome("/Users/BarraganJeronimo/PycharmProjects/chromedriver")
        self.browser.implicitly_wait(2)

    def test_agregar_herramientas(self):
        fake = Faker()
        herramientas = ['Sicua quiz',
                        'Moodle quiz',
                        'Moodle calificaciones',
                        'Sicua calificaciones',
                        'Sicua entrega tareas',
                        'Moodle entrega tareas']
        urls = ['https://sicuaplus.uniandes.edu.co/',
                'https://moodleinstitucional.uniandes.edu.co',
                'https://moodleinstitucional.uniandes.edu.co',
                'https://sicuaplus.uniandes.edu.co/',
                'https://sicuaplus.uniandes.edu.co/',
                'https://moodleinstitucional.uniandes.edu.co']

        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('fmedina')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('fmedina2018')
        self.browser.find_element_by_id('boton_login').click()

        for x in range(0, 5):
            self.browser.find_element_by_id('boton_agregar_herramienta').click()
            nombre_herramienta = self.browser.find_element_by_id('id_nombre')
            nombre_herramienta.send_keys(herramientas[x])
            url_herramienta = self.browser.find_element_by_id('id_urlReferencia')
            url_herramienta.send_keys(urls[x])
            sistema_operativo_herramienta = self.browser.find_element_by_id('id_sistemaOperativo')
            sistema_operativo_herramienta.send_keys("No aplica")
            plataforma_herramienta = self.browser.find_element_by_id('id_plataforma')
            plataforma_herramienta.send_keys("Web")
            ficha_tecnica_herramienta = self.browser.find_element_by_id('id_fichaTecnica')
            ficha_tecnica_herramienta.send_keys(fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None))
            licencia_herramienta = self.browser.find_element_by_id('id_licencia')
            licencia_herramienta.send_keys(fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None))
            descripcion_herramienta = self.browser.find_element_by_id('id_descripcion')
            descripcion_herramienta.send_keys(fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None))
            self.browser.find_element_by_id('boton_add').click()
            self.browser.implicitly_wait(1)

        self.assertIn('Inicio Catalogo', self.browser.title)

