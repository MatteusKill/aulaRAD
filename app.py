import tkinter as tk

janela = tk.Tk()
janela.geometry("500x300")
janela.title("Meu appo")

label = tk.Label(janela, text="aoba")
label.pack(pady=50)

def clicar():
    label.config(text="Conseguimos!")

botao = tk.Button(janela, text="Clicar", command=clicar)
botao.pack()



janela.mainloop()

# janela = tkinter.Tk()
# janela.title("Meu Primeiro App")
# janela.geometry("200x200")

# texto = tkinter.Label(janela, text="Olá, Mundo! O Tkinter está funcionando!", fg="green")
# texto.pack(pady=50)

# janela.mainloop()