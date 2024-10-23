import tkinter as tk
from tkinter import messagebox
from tkinter import Button
from tkinter import PhotoImage

# cria a janela principal
janela = tk.Tk()

# define o titulo da janela 
janela.title("interface gráfica com tkinter")

#carrega a imagem (apenas png ou gif)
imagem = tk.PhotoImage(file="foguete.png")
#criação de um rótulo (Label) com a imagem
rotulo = tk.Label(janela, image=imagem)
rotulo.pack(pady=10)

#define o tamanho da janela
janela.geometry("300x200")

# cria um rótulo (texto)
rotulo = tk.Label(janela, text = "bem vindo à sua primeira interface gráfica!")

#exibe o rótulo na janela
rotulo.pack(pady=20)

#função que sera chamada quando o botão for clicado
def mostrar_mensagem():

#exibe uma caixa de mensagem informativa quando o botão é clicado
 messagebox.showinfo("informação","botão clicado!")

#cria um botão e associa a função mostrar_mensagem à ação de clique no botão
botao = tk.Button(janela, text = "clique aqui",command = mostrar_mensagem)
botao.pack(pady=20)

#executa o loop principal da janela
janela.mainloop()


