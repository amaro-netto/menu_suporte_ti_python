import subprocess
from tkinter import messagebox
import os

# --- FUNÇÕES DE SISTEMA ---

def verificar_chkdsk():
    """
    Função que executa o comando CHKDSK para verificar e reparar o disco C.
    """
    try:
        messagebox.showinfo("Verificação de Disco", 
                            "O comando CHKDSK será agendado para o próximo reinício do sistema.\n"
                            "Ele pode levar algum tempo. Clique em OK para continuar.")

        # O comando CHKDSK exige permissões de administrador.
        # Estamos executando o comando para o disco C: com as flags /f (reparar) e /r (recuperar).
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

def reparar_sfc():
    """
    Função para reparar arquivos de sistema com o SFC.
    """
    try:
        messagebox.showinfo("Reparo SFC", 
                            "Executando reparo de arquivos de sistema. Isso pode levar algum tempo. "
                            "Por favor, aguarde. Uma janela de console pode aparecer.")
        
        # O comando sfc /scannow precisa de permissões de administrador.
        subprocess.run(['sfc', '/scannow'], shell=True, check=True)
        
        messagebox.showinfo("Reparo SFC", "Reparo de arquivos de sistema concluído!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro no SFC", 
                             f"Ocorreu um erro ao executar o SFC. Código de retorno: {e.returncode}\n"
                             "Verifique se o programa foi executado como administrador.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

def limpar_arquivos_temporarios():
    """
    Função para limpar arquivos temporários do sistema.
    """
    try:
        messagebox.showinfo("Limpeza de Arquivos", "Iniciando a limpeza de arquivos temporários. Clique em OK para continuar.")
        
        # Comando do seu script .bat: `cleanmgr /sagerun:1`. Este comando abre uma
        # interface de limpeza do disco com configurações pré-definidas.
        subprocess.run(['cleanmgr', '/sagerun:1'], shell=True, check=True)
        
        messagebox.showinfo("Limpeza de Arquivos", "Limpeza de arquivos temporários concluída!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar a limpeza: {e.returncode}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")