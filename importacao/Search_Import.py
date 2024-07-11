import tkinter as tk
from tkinter import filedialog

# Criando uma janela de diálogo de arquivo
root = tk.Tk()
root.withdraw()  # Ocultar a janela principal

# Abrir a janela de diálogo de arquivo
file_path = filedialog.askopenfilename()
# Defina o caminho para o arquivo
file = file_path
#transformar em df
data = pd.read_excel(file)
