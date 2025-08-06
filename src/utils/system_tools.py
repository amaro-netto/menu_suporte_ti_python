import os
import subprocess
from tkinter import messagebox

def verificar_chkdsk():
    """
    Função que executa o comando CHKDSK para verificar e reparar o disco C.
    """
    try:
        messagebox.showinfo("Verificação de Disco", 
                            "O comando CHKDSK será agendado para o próximo reinício do sistema.\n"
                            "Ele pode levar algum tempo. Clique em OK para continuar.")

        subprocess.run(['chkdsk', 'C:', '/f', '/r'], shell=True, check=True)
        
        messagebox.showinfo("Verificação de Disco", 
                            "Verificação de disco agendada com sucesso!\n"
                            "Reinicie o computador para que a verificação seja executada.")
                            
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro no CHKDSK", 
                             f"Ocorreu um erro ao agendar o CHKDSK. Código de retorno: {e.returncode}\n"
                             "Verifique se o programa foi executado como administrador.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

# ... outras funções de sistema serão adicionadas aqui ...