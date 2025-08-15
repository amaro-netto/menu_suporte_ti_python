import subprocess
from tkinter import messagebox
from tkinter import simpledialog

def gerenciar_aplicativos_winget():
    """
    Função para abrir um sub-menu com as opções do Winget.
    """
    try:
        # Pede ao usuário para escolher uma opção do Winget
        escolha = simpledialog.askstring("Winget - Gerenciador de Apps",
                                         "Escolha uma opção do Winget:\n\n"
                                         "1. Listar aplicativos instalados\n"
                                         "2. Procurar por um aplicativo\n"
                                         "3. Instalar um aplicativo\n"
                                         "4. Atualizar todos os aplicativos\n"
                                         "5. Desinstalar um aplicativo\n"
                                         "6. Sair",
                                         parent=None)

        if escolha == '1':
            listar_aplicativos_winget()
        elif escolha == '2':
            procurar_aplicativo_winget()
        elif escolha == '3':
            instalar_aplicativo_winget()
        elif escolha == '4':
            atualizar_todos_winget()
        elif escolha == '5':
            desinstalar_aplicativo_winget()
        elif escolha == '6' or escolha is None: # Se o usuário clicar em "Cancelar" ou digitar "6"
            messagebox.showinfo("Winget", "Retornando ao menu principal.")
        else:
            messagebox.showerror("Erro", "Opção inválida.")
            gerenciar_aplicativos_winget() # Chama a função novamente para permitir nova escolha

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# --- Funções individuais do Winget ---

def listar_aplicativos_winget():
    """
    Lista todos os aplicativos instalados usando winget list.
    """
    messagebox.showinfo("Winget", "Abrindo uma janela de console para listar os aplicativos instalados.")
    comando = 'start cmd /k "winget list && pause"'
    subprocess.run(comando, shell=True)

def procurar_aplicativo_winget():
    """
    Procura por um aplicativo na fonte do winget.
    """
    app_name = simpledialog.askstring("Winget - Procurar App", "Digite o nome do aplicativo que deseja procurar:")
    if app_name:
        messagebox.showinfo("Winget", f"Procurando por '{app_name}'. Abrindo console para exibir resultados.")
        comando = f'start cmd /k "winget search "{app_name}" && pause"'
        subprocess.run(comando, shell=True)

def instalar_aplicativo_winget():
    """
    Instala um aplicativo usando winget.
    """
    app_id = simpledialog.askstring("Winget - Instalar App", "Digite o ID ou nome do aplicativo que deseja instalar:")
    if app_id:
        messagebox.showinfo("Winget", f"Instalando '{app_id}'. Abrindo console para exibir progresso.")
        comando = f'start cmd /k "winget install "{app_id}" && pause"'
        subprocess.run(comando, shell=True)

def atualizar_todos_winget():
    """
    Atualiza todos os aplicativos usando winget.
    """
    messagebox.showinfo("Winget", "Atualizando todos os aplicativos. Abrindo console para exibir progresso.")
    comando = 'start cmd /k "winget upgrade --all && pause"'
    subprocess.run(comando, shell=True)

def desinstalar_aplicativo_winget():
    """
    Desinstala um aplicativo usando winget.
    """
    app_id = simpledialog.askstring("Winget - Desinstalar App", "Digite o ID ou nome do aplicativo que deseja desinstalar:")
    if app_id:
        messagebox.showinfo("Winget", f"Desinstalando '{app_id}'. Abrindo console para exibir progresso.")
        comando = f'start cmd /k "winget uninstall "{app_id}" && pause"'
        subprocess.run(comando, shell=True)