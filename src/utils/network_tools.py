import subprocess
from tkinter import messagebox
import os

def verificar_conectividade_de_rede():
    """
    Função para verificar a conectividade de rede usando ping e ipconfig.
    """
    try:
        # Abertura de uma nova janela de console para exibir o resultado.
        messagebox.showinfo("Verificação de Rede", 
                            "Abrindo uma janela de console para exibir os resultados do teste de rede. Clique em OK.")
        
        # O comando `start cmd /k ...` abre um novo prompt de comando (`cmd`)
        # e o mantém aberto (`/k`) após a execução dos comandos.
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