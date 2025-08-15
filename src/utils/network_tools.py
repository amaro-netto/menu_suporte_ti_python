import subprocess
from tkinter import messagebox
import os

def verificar_conectividade_de_rede():
    """
    Função para verificar a conectividade de rede usando ping e ipconfig.
    """
    try:
        messagebox.showinfo("Verificação de Rede", 
                            "Abrindo uma janela de console para exibir os resultados do teste de rede. Clique em OK.")
        
        comando = 'start cmd /k "echo Verificando conectividade de rede... && ' \
                  'echo Testando conexao com google.com... && ' \
                  'ping google.com -n 4 && ' \
                  'echo. && ' \
                  'echo Testando conexao com gateway padrao... && ' \
                  'ipconfig | findstr "Gateway" && ' \
                  'echo. && ' \
                  'echo Teste de rede concluido. Pressione qualquer tecla para sair." '
                  
        subprocess.run(comando, shell=True)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar o teste de rede: {e}")

def limpar_cache_dns():
    """
    Função para limpar o cache DNS.
    """
    try:
        messagebox.showinfo("Limpeza de Cache DNS", "Iniciando a limpeza do cache DNS. Clique em OK para continuar.")
        
        # O comando ipconfig /flushdns exige permissões de administrador.
        # Por isso, o programa precisa ser executado como administrador.
        subprocess.run(['ipconfig', '/flushdns'], shell=True, check=True)
        
        messagebox.showinfo("Limpeza de Cache DNS", "Cache DNS limpo com sucesso!")
        
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro de Permissão", 
                             f"Ocorreu um erro ao limpar o cache DNS. Código de retorno: {e.returncode}\n"
                             "Verifique se o programa foi executado como administrador.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")