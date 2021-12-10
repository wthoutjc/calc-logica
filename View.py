#INTERFAZ

from tkinter import *
from tkinter import Canvas, messagebox
import pyparsing
import ttg

#Model
from Model import Model

class View():

    def __init__(self, title):
        self.text = ''
        self.model = Model()
        self.window = Tk()

        self.window.title(title)
        self.window.resizable(0,0)

        self.labelTitle0 = Label(self.window, text="Calculadora Lógica - UDFJC",font=("Helvetica", 10)).grid(row=0,column=0,columnspan = 4,pady=2,padx=2)

        #Data
        self.entry = Entry(self.window, font = ("Calibri 20"))
        self.entry.grid(row=4,column=0, columnspan = 4, pady=5,padx=5)

        self.btn_ac = Button(self.window, text = "AC", width = 8, height = 2, command = lambda: self.borrar(0)).grid(row = 5, column = 0, padx = 2, pady = 2)
        self.btn_del = Button(self.window, text = "DEL", width = 8, height = 2, command = lambda: self.borrar(1)).grid(row = 5, column = 1, padx = 2, pady = 2)
        self.btn_equal = Button(self.window, text="=",width = 16, height = 2, command=lambda: self.tablas_logicas(self.model.get_data(self.entry.get()))).grid(row = 5, column = 2, columnspan = 2,pady=2, padx=2,)

        #Identifiers
        self.btn_p = Button(self.window, text = "p", width = 8, height = 2, command = lambda: self.escribir("p")).grid(row = 6, column = 0, padx = 2, pady = 2)
        self.btn_q = Button(self.window, text = "q", width = 8, height = 2, command = lambda: self.escribir("q")).grid(row = 6, column = 1, padx = 2, pady = 2)
        self.btn_r = Button(self.window, text = "r", width = 8, height = 2, command = lambda: self.escribir("r")).grid(row = 6, column = 2, padx = 2, pady = 2)      
        self.btn_s = Button(self.window, text = "s", width = 8, height = 2, command = lambda: self.escribir("s")).grid(row = 6, column = 3, padx = 2, pady = 2)
        
        #Operators
        self.btn_negacion = Button(self.window, text = "~", width = 8, height = 2, command = lambda: self.escribir("~")).grid(row = 7, column = 0, padx = 2, pady = 2)
        self.btn_y = Button(self.window, text = "˄", width = 8, height = 2, command = lambda: self.escribir("˄")).grid(row = 7, column = 1, padx = 2, pady = 2)
        self.btn_o = Button(self.window, text = "v", width = 8, height = 2, command = lambda: self.escribir("v")).grid(row =7, column = 2, padx = 2, pady = 2)
        self.btn_entonces = Button(self.window, text = "→", width = 8, height = 2, command = lambda: self.escribir("→")).grid(row = 7, column = 3, padx = 2, pady = 2)
        self.btn_si = Button(self.window, text = "↔", width = 8, height = 2, command = lambda: self.escribir("↔")).grid(row = 8, column = 0, padx = 2, pady = 2)
        

        #Symbols
        self.btn_parent0 = Button(self.window, text = "(", width = 8, height = 2, command = lambda: self.escribir("(")).grid(row = 8, column = 2, padx = 2, pady = 2)
        self.btn_parent1 = Button(self.window, text = ")", width = 8, height = 2, command = lambda: self.escribir(")")).grid(row = 8, column = 3, padx = 2, pady = 2)
        
        self.window.mainloop()
    
    def borrar(self, option):
        if option == 0:
            self.entry.delete(0, END)
            self.text = ''
        elif option == 1:
            if self.text != '':
                self.entry.delete(0, END)
                self.text = self.text[:len(self.text)-1]
                self.entry.insert(0, self.text)

    def escribir(self, x):
        self.entry.insert(len(self.text), x)
        self.text += x
    
    def tablas_logicas(self, array):
        if array[0]:
            try:
                self.new_window = Tk()
                self.new_window.title('Results')
                self.table = Text(self.new_window, width=80,height=21)
                print(array[0],[str(array[1])])
                self.table.insert(INSERT, ttg.Truths(array[0],[str(array[1])]))
                self.table.config(state=DISABLED)
                self.table.grid(row=0, column=0, padx=5, pady=5)
                self.window.destroy()
                self.btn_p = Button(self.new_window, text = "Nuevo", width = 8, height = 2, command = lambda: self.new_calc(self.new_window)).grid(row = 1, column = 0, padx = 2, pady = 2)
                self.new_window.mainloop()
            except BaseException:
                self.new_window.destroy()
    
    def new_calc(self, window):
        self._window = window
        self._window.destroy()
        self.__init__("Calculadora Lógica")