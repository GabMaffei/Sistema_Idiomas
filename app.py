import tkinter as tk
from tkinter import ttk
import tkinter.font as font
# from atributos import *
import similaridades


class App:
    def __init__(self, root):
        # Definindo o título
        root.title("Sistema de idiomas")
        # Definindo tamanho da janela
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        # Labels da janela
        self.__labels_casos_entrada(root)
        self.__labels_pesos(root)
        self.__labels_recomendados(root)

        # Casos ENTRADA - Início -----------------------
        g_line_edit_obj_ent = tk.Entry(root)
        g_line_edit_obj_ent_txt = tk.StringVar()
        g_line_edit_obj_ent["borderwidth"] = "1px"
        ft = font.Font(family='Segoe UI', size=10)
        g_line_edit_obj_ent["font"] = ft
        g_line_edit_obj_ent["fg"] = "#333333"
        g_line_edit_obj_ent["justify"] = "left"
        g_line_edit_obj_ent_txt.set("8")
        g_line_edit_obj_ent["textvariable"] = g_line_edit_obj_ent_txt
        # g_line_edit_obj_ent["text"] = "8"
        # g_line_edit_obj_ent["show"] = "8"
        # g_line_edit_obj_ent["invalidcommand"] = "invalud"
        # g_line_edit_obj_ent["validatecommand"] = "validate"
        g_line_edit_obj_ent.place(x=170, y=70, width=100, height=20)

        g_line_edit_temp_ent = tk.Entry(root)
        g_line_edit_temp_ent_txt = tk.StringVar()
        g_line_edit_temp_ent["borderwidth"] = "1px"
        ft = font.Font(family='Segoe UI', size=10)
        g_line_edit_temp_ent["font"] = ft
        g_line_edit_temp_ent["fg"] = "#333333"
        g_line_edit_temp_ent["justify"] = "left"
        g_line_edit_temp_ent_txt.set("2")
        g_line_edit_temp_ent["textvariable"] = g_line_edit_temp_ent_txt
        g_line_edit_temp_ent.place(x=140, y=95, width=130, height=20)

        g_combo_box_230 = ttk.Combobox(root)
        ft = font.Font(family='Segoe UI', size=10)
        g_combo_box_230["font"] = ft
        g_combo_box_230["justify"] = "left"
        g_combo_box_230.place(x=100, y=45, width=170, height=20)
        g_combo_box_230['values'] = similaridades.idioma_alvo_valores
        g_combo_box_230.current(1)

        g_combo_box_231 = ttk.Combobox(root)
        ft = font.Font(family='Segoe UI', size=10)
        g_combo_box_231["font"] = ft
        g_combo_box_231["justify"] = "left"
        g_combo_box_231.place(x=370, y=45, width=220, height=20)
        g_combo_box_231['values'] = similaridades.nivel_idioma_valores
        g_combo_box_231.current(2)

        g_combo_box_232 = ttk.Combobox(root)
        ft = font.Font(family='Segoe UI', size=10)
        g_combo_box_232["font"] = ft
        g_combo_box_232["justify"] = "left"
        g_combo_box_232.place(x=430, y=70, width=160, height=20)
        g_combo_box_232['values'] = similaridades.recursos_aprendizagem_valores
        g_combo_box_232.current(1)

        g_combo_box_233 = ttk.Combobox(root)
        ft = font.Font(family='Segoe UI', size=10)
        g_combo_box_233["font"] = ft
        g_combo_box_233["justify"] = "left"
        g_combo_box_233.place(x=370, y=95, width=220, height=20)
        g_combo_box_233['values'] = similaridades.comunidade_valores
        g_combo_box_233.current(0)
        # Casos ENTRADA - Fim -----------------------

        # PESO - Início -----------------------
        g_line_edit_obj_pes = tk.Entry(root)
        g_line_edit_obj_pes_txt = tk.StringVar()
        g_line_edit_obj_pes["borderwidth"] = "1px"
        ft = font.Font(family='Segoe UI', size=10)
        g_line_edit_obj_pes["font"] = ft
        g_line_edit_obj_pes["fg"] = "#333333"
        g_line_edit_obj_pes["justify"] = "left"
        g_line_edit_obj_pes_txt.set("0.3")
        g_line_edit_obj_pes["textvariable"] = g_line_edit_obj_pes_txt
        g_line_edit_obj_pes.place(x=170, y=175, width=100, height=20)

        g_line_edit_temp_pes = tk.Entry(root)
        g_line_edit_temp_pes_txt = tk.StringVar()
        g_line_edit_temp_pes["borderwidth"] = "1px"
        ft = font.Font(family='Segoe UI', size=10)
        g_line_edit_temp_pes["font"] = ft
        g_line_edit_temp_pes["fg"] = "#333333"
        g_line_edit_temp_pes["justify"] = "left"
        g_line_edit_temp_pes_txt.set("0.3")
        g_line_edit_temp_pes["textvariable"] = g_line_edit_temp_pes_txt
        g_line_edit_temp_pes.place(x=140, y=200, width=130, height=20)
        # PESO - Fim -----------------------

        # Caso RECOMENDADO - Início -----------------------
        g_line_edit_obj_rec = tk.Entry(root)
        g_line_edit_obj_rec_txt = tk.StringVar()
        g_line_edit_obj_rec["borderwidth"] = "1px"
        ft = font.Font(family='Segoe UI', size=10)
        g_line_edit_obj_rec["font"] = ft
        g_line_edit_obj_rec["fg"] = "#333333"
        g_line_edit_obj_rec["justify"] = "left"
        g_line_edit_obj_rec_txt.set("8")
        g_line_edit_obj_rec["textvariable"] = g_line_edit_obj_rec_txt
        g_line_edit_obj_rec.place(x=170, y=285, width=100, height=20)

        g_line_edit_temp_rec = tk.Entry(root)
        g_line_edit_temp_rec_txt = tk.StringVar()
        g_line_edit_temp_rec["borderwidth"] = "1px"
        ft = font.Font(family='Segoe UI', size=10)
        g_line_edit_temp_rec["font"] = ft
        g_line_edit_temp_rec["fg"] = "#333333"
        g_line_edit_temp_rec["justify"] = "left"
        g_line_edit_temp_rec_txt.set("2")
        g_line_edit_temp_rec["textvariable"] = g_line_edit_temp_rec_txt
        g_line_edit_temp_rec.place(x=140, y=310, width=130, height=20)

        g_combo_box_240 = ttk.Combobox(root)
        ft = font.Font(family='Segoe UI', size=10)
        g_combo_box_240["font"] = ft
        g_combo_box_240["justify"] = "left"
        g_combo_box_240.place(x=100, y=260, width=170, height=20)
        g_combo_box_240['values'] = similaridades.idioma_alvo_valores
        g_combo_box_240.current(1)

        g_combo_box_241 = ttk.Combobox(root)
        ft = font.Font(family='Segoe UI', size=10)
        g_combo_box_241["font"] = ft
        g_combo_box_241["justify"] = "left"
        g_combo_box_241.place(x=370, y=260, width=220, height=20)
        g_combo_box_241['values'] = similaridades.nivel_idioma_valores
        g_combo_box_241.current(2)

        g_combo_box_242 = ttk.Combobox(root)
        ft = font.Font(family='Segoe UI', size=10)
        g_combo_box_242["font"] = ft
        g_combo_box_242["justify"] = "left"
        g_combo_box_242.place(x=430, y=285, width=160, height=20)
        g_combo_box_242['values'] = similaridades.recursos_aprendizagem_valores
        g_combo_box_242.current(1)

        g_combo_box_243 = ttk.Combobox(root)
        ft = font.Font(family='Segoe UI', size=10)
        g_combo_box_243["font"] = ft
        g_combo_box_243["justify"] = "left"
        g_combo_box_243.place(x=370, y=310, width=220, height=20)
        g_combo_box_243['values'] = similaridades.comunidade_valores
        g_combo_box_243.current(0)
        # Caso RECOMENDADO - Fim -----------------------

        self.__botoes(root)

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

    def __labels_recomendados(self, root):
        # Casos recomendados - Início
        g_label_884 = tk.Label(root)
        g_label_884["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10, weight='bold')
        g_label_884["font"] = ft
        g_label_884["fg"] = "#333333"
        g_label_884["justify"] = "left"
        g_label_884["text"] = "Caso recomendado:"
        g_label_884.place(x=20, y=230, width=229, height=30)

        g_label_743 = tk.Label(root)
        g_label_743["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_743["font"] = ft
        g_label_743["fg"] = "#333333"
        g_label_743["justify"] = "left"
        g_label_743["text"] = "Idioma alvo:"
        g_label_743.place(x=20, y=255, width=106, height=30)

        g_label_962 = tk.Label(root)
        g_label_962["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_962["font"] = ft
        g_label_962["fg"] = "#333333"
        g_label_962["justify"] = "left"
        g_label_962["text"] = "Nível idioma:"
        g_label_962.place(x=280, y=255, width=113, height=30)

        g_label_89 = tk.Label(root)
        g_label_89["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_89["font"] = ft
        g_label_89["fg"] = "#333333"
        g_label_89["justify"] = "left"
        g_label_89["text"] = "Objetivo aprendizagem:"
        g_label_89.place(x=20, y=280, width=148, height=30)

        g_label_155 = tk.Label(root)
        g_label_155["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_155["font"] = ft
        g_label_155["fg"] = "#333333"
        g_label_155["justify"] = "left"
        g_label_155["text"] = "Recurso aprendizagem:"
        g_label_155.place(x=280, y=280, width=148, height=30)

        g_label_255 = tk.Label(root)
        g_label_255["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_255["font"] = ft
        g_label_255["fg"] = "#333333"
        g_label_255["justify"] = "left"
        g_label_255["text"] = "Tempo disponível:"
        g_label_255.place(x=20, y=305, width=134, height=30)

        g_label_818 = tk.Label(root)
        g_label_818["anchor"] = "w"
        ft = font.Font(family='Segoe UI', size=10)
        g_label_818["font"] = ft
        g_label_818["fg"] = "#333333"
        g_label_818["justify"] = "left"
        g_label_818["text"] = "Comunidade:"
        g_label_818.place(x=280, y=305, width=91, height=30)
        # Casos recomendados - Fim

    def __botoes(self, root):
        # Botões
        g_button_477 = tk.Button(root)
        g_button_477["bg"] = "#f0f0f0"
        ft = font.Font(family='Segoe UI', size=10, weight='bold')
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
        g_button_640.place(x=30, y=450, width=100, height=30)
        g_button_640["command"] = self.g_button_640_command

    def g_button_477_command(self):
        # Saída
        print('Caso de entrada :')
        print(similaridades.caso_entrada)
        print('Pesos:')
        print(similaridades.atributos)
        print('Caso recomendado:')
        print(similaridades.caso_recomendado)
        print('Casos base ordenados por similaridade:')
        # for case, similaridade in similaridades:
        #    print(case)
        #    print('Similaridade:', similaridade)
        # Calculo do percentual
        total_similaridade = sum([sim[1] for sim in similaridades.similaridades])
        for sim in similaridades.similaridades:
            case = sim[0]
            similaridade = sim[1]
            similaridade_percentual = round((similaridade / total_similaridade) * 100, 2)
            print(f"{case}, similaridade: {similaridade_percentual}%")
        # A saída das similaridades é apresentada em ordem decrescente de similaridade. Em seguida, a
        # similaridade é convertida em um percentual de similaridade em relação ao total da similaridade
        # para cada caso. Finalmente, é exibido cada caso da base de casos, com seu percentual de
        # similaridade em relação ao caso de entrada.

    def g_button_640_command(self):
        print("command")
