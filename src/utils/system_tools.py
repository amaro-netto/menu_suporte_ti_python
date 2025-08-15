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
        
        subprocess.run(['cleanmgr', '/sagerun:1'], shell=True, check=True)
        
        messagebox.showinfo("Limpeza de Arquivos", "Limpeza de arquivos temporários concluída!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar a limpeza: {e.returncode}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

def verificar_erros_de_memoria():
    """
    Função para iniciar o Diagnóstico de Memória do Windows.
    """
    try:
        messagebox.showinfo("Diagnóstico de Memória", "Abrindo a ferramenta de Diagnóstico de Memória do Windows.\n"
                                                      "Siga as instruções na tela para verificar a memória.")
        
        subprocess.run(['mdsched.exe'], shell=True, check=False)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao abrir o Diagnóstico de Memória: {e}")

def restaurar_sistema():
    """
    Função para abrir a ferramenta de Restauração do Sistema.
    """
    try:
        messagebox.showinfo("Restauração do Sistema", "Abrindo a ferramenta de Restauração do Sistema.\n"
                                                      "Siga as instruções na tela para escolher um ponto de restauração.")
        
        subprocess.run(['rstrui.exe'], shell=True, check=False)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao abrir a Restauração do Sistema: {e}")

def gerenciar_processos():
    """
    Função para abrir o Gerenciador de Tarefas do Windows.
    """
    try:
        messagebox.showinfo("Gerenciador de Tarefas", "Abrindo o Gerenciador de Tarefas do Windows.\n"
                                                      "Use a ferramenta para monitorar e encerrar processos.")
        
        subprocess.run(['taskmgr.exe'], shell=True, check=False)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao abrir o Gerenciador de Tarefas: {e}")

def backup_de_drivers():
    """
    Função para realizar backup dos drivers do sistema.
    """
    try:
        messagebox.showinfo("Backup de Drivers", 
                            "Abrindo uma janela de console para exibir o progresso do backup de drivers.\n"
                            "Este processo pode levar algum tempo. Clique em OK para continuar.")
        
        comando = 'start cmd /k "echo Realizando backup de drivers... && ' \
                  'mkdir C:\\DriverBackup && ' \
                  'dism /online /export-driver /destination:C:\\DriverBackup && ' \
                  'echo. && ' \
                  'echo Backup de drivers concluido! Salvo em C:\\DriverBackup && ' \
                  'pause" '
                  
        subprocess.run(comando, shell=True)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar o backup de drivers: {e}")

def verificar_atualizacoes():
    """
    Função para abrir a ferramenta de Atualização do Windows.
    """
    try:
        messagebox.showinfo("Atualizações do Windows", "Abrindo as configurações de Atualização do Windows.\n"
                                                      "Verifique o status das atualizações e procure por novas.")
        
        subprocess.run(['start', 'ms-settings:windowsupdate'], shell=True, check=False)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao abrir o Windows Update: {e}")

def informacoes_do_sistema():
    """
    Função para exibir informações detalhadas do sistema.
    """
    try:
        messagebox.showinfo("Informações do Sistema", "Abrindo uma janela de console para exibir as informações detalhadas do sistema.\n"
                                                      "Clique em OK para continuar.")
        
        subprocess.run('start cmd /k "systeminfo & pause"', shell=True, check=False)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao obter as informações do sistema: {e}")

def desfragmentar_disco():
    """
    Função para desfragmentar o disco C.
    """
    try:
        messagebox.showinfo("Desfragmentação de Disco", 
                            "Abrindo uma janela de console para exibir o progresso da desfragmentação do disco C.\n"
                            "Este processo pode levar algum tempo. Clique em OK para continuar.")
        
        comando = 'start cmd /k "echo Executando desfragmentacao de disco... && defrag C: /O && echo Desfragmentacao concluida! && pause" '
                  
        subprocess.run(comando, shell=True)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao desfragmentar o disco: {e}")

def gerenciar_usuarios_locais():
    """
    Função para abrir o Gerenciamento de Usuários Locais.
    """
    try:
        messagebox.showinfo("Gerenciamento de Usuários", 
                            "Abrindo o Gerenciamento de Usuários e Grupos Locais.\n"
                            "Use a ferramenta para criar, editar ou excluir usuários.")
        
        subprocess.run(['lusrmgr.msc'], shell=True, check=False)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao abrir o Gerenciamento de Usuários: {e}")

def verificar_integridade_dism():
    """
    Função para verificar e reparar a integridade da imagem do Windows com DISM.
    """
    try:
        messagebox.showinfo("Verificação DISM", 
                            "Abrindo uma janela de console para verificar a integridade da imagem do Windows.\n"
                            "Este processo pode levar um tempo considerável e requer privilégios de administrador. Clique em OK para continuar.")
        
        # O comando DISM exige permissões de administrador.
        # Usamos `start cmd /k` para exibir o progresso.
        comando = 'start cmd /k "echo Verificando integridade da imagem do Windows... && ' \
                  'dism /online /cleanup-image /restorehealth && ' \
                  'echo Verificacao e reparo concluidos! && ' \
                  'pause"'
        
        subprocess.run(comando, shell=True)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar a verificação DISM: {e}")