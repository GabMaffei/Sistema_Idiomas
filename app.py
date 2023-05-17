import tkinter as tk
# from tkinter import ttk
import tkinter.font as font


class App:
    def __init__(self, root):
        # setting title
        root.title("Sistema de idiomas")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.__labels_casos_entrada(root)
        self.__labels_pesos(root)

        g_label_884 = tk.Label(root)
        ft = font.Font(family='Segoe UI', size=10)
        g_label_884["font"] = ft
        g_label_884["fg"] = "#333333"
        g_label_884["justify"] = "left"
        g_label_884["text"] = "Caso recomendado:"
        g_label_884.place(x=20, y=290, width=229, height=30)

        g_button_477 = tk.Button(root)
        g_button_477["bg"] = "#f0f0f0"
        ft = font.Font(family='Segoe UI', size=10)
        g_button_477["font"] = ft
        g_button_477["fg"] = "#000000"
        g_button_477["justify"] = "center"
        g_button_477["text"] = "Calcular a similaridade"
        g_button_477.place(x=210, y=450, width=166, height=30)
        g_button_477["command"] = self.g_button_477_command

        g_button_640 = tk.Button(root)
        g_button_640["bg"] = "#f0f0f0"
        ft = font.Font(family='Segoe UI', size=10)
        g_button_640["font"] = ft
        g_button_640["fg"] = "#000000"
        g_button_640["justify"] = "center"
        g_button_640["text"] = "Lista de casos"
        g_button_640.place(x=30, y=450, width=74, height=30)
        g_button_640["command"] = self.g_button_640_command

    def __labels_casos_entrada(self, root):
        # Casos de entrada - Início
        g_label_772 = tk.Label(root)
        g_label_772["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10, weight='bold')
        g_label_772["font"] = ft
        g_label_772["fg"] = "#333333"
        g_label_772["justify"] = "left"
        g_label_772["text"] = "Caso de entrada:"
        g_label_772.place(x=20, y=20, width=120, height=30)

        g_label_743 = tk.Label(root)
        g_label_743["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_743["font"] = ft
        g_label_743["fg"] = "#333333"
        g_label_743["justify"] = "left"
        g_label_743["text"] = "Idioma alvo:"
        g_label_743.place(x=20, y=40, width=106, height=30)

        g_label_962 = tk.Label(root)
        g_label_962["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_962["font"] = ft
        g_label_962["fg"] = "#333333"
        g_label_962["justify"] = "left"
        g_label_962["text"] = "Nível idioma:"
        g_label_962.place(x=280, y=40, width=113, height=30)

        g_label_89 = tk.Label(root)
        g_label_89["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_89["font"] = ft
        g_label_89["fg"] = "#333333"
        g_label_89["justify"] = "left"
        g_label_89["text"] = "Objetivo aprendizagem:"
        g_label_89.place(x=20, y=65, width=148, height=30)

        g_label_155 = tk.Label(root)
        g_label_155["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_155["font"] = ft
        g_label_155["fg"] = "#333333"
        g_label_155["justify"] = "left"
        g_label_155["text"] = "Recurso aprendizagem:"
        g_label_155.place(x=280, y=65, width=148, height=30)

        g_label_255 = tk.Label(root)
        g_label_255["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_255["font"] = ft
        g_label_255["fg"] = "#333333"
        g_label_255["justify"] = "left"
        g_label_255["text"] = "Tempo disponível:"
        g_label_255.place(x=20, y=90, width=134, height=30)

        g_label_818 = tk.Label(root)
        g_label_818["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_818["font"] = ft
        g_label_818["fg"] = "#333333"
        g_label_818["justify"] = "left"
        g_label_818["text"] = "Comunidade:"
        g_label_818.place(x=280, y=90, width=91, height=30)
        # Casos de entrada - Fim

    def __labels_pesos(self, root):
        # Peso dos atributos - Início
        g_label_501 = tk.Label(root)
        g_label_501["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10, weight='bold')
        g_label_501["font"] = ft
        g_label_501["fg"] = "#333333"
        g_label_501["justify"] = "left"
        g_label_501["text"] = "Peso dos atributos:"
        g_label_501.place(x=20, y=125, width=130, height=30)

        g_label_743 = tk.Label(root)
        g_label_743["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_743["font"] = ft
        g_label_743["fg"] = "#333333"
        g_label_743["justify"] = "left"
        g_label_743["text"] = "Idioma alvo:"
        g_label_743.place(x=20, y=145, width=106, height=30)

        g_label_962 = tk.Label(root)
        g_label_962["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_962["font"] = ft
        g_label_962["fg"] = "#333333"
        g_label_962["justify"] = "left"
        g_label_962["text"] = "Nível idioma:"
        g_label_962.place(x=280, y=145, width=113, height=30)

        g_label_89 = tk.Label(root)
        g_label_89["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_89["font"] = ft
        g_label_89["fg"] = "#333333"
        g_label_89["justify"] = "left"
        g_label_89["text"] = "Objetivo aprendizagem:"
        g_label_89.place(x=20, y=170, width=148, height=30)

        g_label_155 = tk.Label(root)
        g_label_155["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_155["font"] = ft
        g_label_155["fg"] = "#333333"
        g_label_155["justify"] = "left"
        g_label_155["text"] = "Recurso aprendizagem:"
        g_label_155.place(x=280, y=170, width=148, height=30)

        g_label_255 = tk.Label(root)
        g_label_255["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_255["font"] = ft
        g_label_255["fg"] = "#333333"
        g_label_255["justify"] = "left"
        g_label_255["text"] = "Tempo disponível:"
        g_label_255.place(x=20, y=195, width=134, height=30)

        g_label_818 = tk.Label(root)
        g_label_818["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_818["font"] = ft
        g_label_818["fg"] = "#333333"
        g_label_818["justify"] = "left"
        g_label_818["text"] = "Comunidade:"
        g_label_818.place(x=280, y=195, width=91, height=30)
        # Peso dos atributos - Fim

    def g_button_477_command(self):
        print("command")

    def g_button_640_command(self):
        print("command")
