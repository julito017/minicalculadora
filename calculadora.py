import tkinter as tk
from tkinter import font

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto Calculadora")
        self.root.configure(bg='#f2f2f2')
        
        # Configurar fuentes
        titulo_font = font.Font(family="Arial", size=16, weight="bold")
        subtitulo_font = font.Font(family="Arial", size=12)
        boton_font = font.Font(family="Arial", size=12)
        pantalla_font = font.Font(family="Arial", size=16)
        
        # Títulos
        titulo = tk.Label(root, text="Proyecto Calculadora", font=titulo_font, bg="#e25e5e")
        titulo.pack(pady=10)
        
        subtitulo = tk.Label(root, text="Julio Cesar", font=subtitulo_font, bg='#f2f2f2', fg='#666')
        subtitulo.pack()
        
        # Marco de la calculadora
        marco_calculadora = tk.Frame(root, bg='white', padx=20, pady=20, relief='raised', bd=2)
        marco_calculadora.pack(pady=20)
        
        # Pantalla
        self.pantalla = tk.Entry(marco_calculadora, width=25, font=pantalla_font, 
                                justify='right', state='readonly', readonlybackground='white')
        self.pantalla.grid(row=0, column=0, columnspan=4, pady=10, ipady=8)
        
        # Botones
        botones = [
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '/', '=',
            'C'
        ]
        
        # Variables para el diseño
        row_val = 1
        col_val = 0
        
        for boton in botones:
            if boton == 'C':
                btn = tk.Button(marco_calculadora, text=boton, width=15, height=2, 
                               font=boton_font, command=self.limpiar)
                btn.grid(row=row_val, column=0, columnspan=4, pady=5)
            else:
                btn = tk.Button(marco_calculadora, text=boton, width=5, height=2, 
                               font=boton_font, command=lambda b=boton: self.click(b))
                btn.grid(row=row_val, column=col_val, padx=2, pady=2)
                
                col_val += 1
                if col_val > 3:
                    col_val = 0
                    row_val += 1
        
        # Inicializar variables
        self.operacion = ""
        self.resultado_calculado = False

    def click(self, valor):
        if self.resultado_calculado and valor not in ['+', '-', '*', '/']:
            self.limpiar()
            
        estado_actual = self.pantalla.cget('state')
        self.pantalla.configure(state='normal')
        
        if valor == '=':
            try:
                resultado = eval(self.operacion)
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, str(resultado))
                self.operacion = str(resultado)
                self.resultado_calculado = True
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error")
                self.operacion = ""
        else:
            if self.pantalla.get() == "Error":
                self.pantalla.delete(0, tk.END)
                
            self.pantalla.insert(tk.END, valor)
            self.operacion += valor
            self.resultado_calculado = False
            
        self.pantalla.configure(state='readonly')

    def limpiar(self):
        self.pantalla.configure(state='normal')
        self.pantalla.delete(0, tk.END)
        self.pantalla.configure(state='readonly')
        self.operacion = ""
        self.resultado_calculado = False

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()