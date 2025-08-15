import tkinter as tk
from tkinter import messagebox

# Importa as funções de ferramentas de sistema
from utils.system_tools import (
    verificar_chkdsk, 
    reparar_sfc, 
    limpar_arquivos_temporarios,
    verificar_erros_de_memoria,
    restaurar_sistema,
    gerenciar_processos,
    backup_de_drivers,
    verificar_atualizacoes,
    informacoes_do_sistema
)

# Importa as funções de ferramentas de rede
from utils.network_tools import (
    verificar_conectividade_de_rede,
    limpar_cache_dns  # Nova função importada
)

# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---

def criar_interface():
    janela = tk.Tk()
    janela.title("Menu de Reparo e Ferramentas de TI")
    janela.geometry("400x600")
    janela.configure(bg="#2E2E2E")

    titulo = tk.Label(janela, text="Menu de Reparo e Ferramentas de TI", font=("Helvetica", 16, "bold"), fg="#00FF00", bg="#2E2E2E")
    titulo.pack(pady=20)

    # --- CRIAÇÃO DOS BOTÕES ---

    # Botões de Sistema (já implementados)
    botao_chkdsk = tk.Button(janela, text="1. Verificar e Reparar Disco (CHKDSK)", command=verificar_chkdsk, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_chkdsk.pack(pady=5)
    botao_sfc = tk.Button(janela, text="2. Reparar Arquivos de Sistema (SFC)", command=reparar_sfc, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_sfc.pack(pady=5)
    botao_limpar = tk.Button(janela, text="3. Limpar Arquivos Temporários", command=limpar_arquivos_temporarios, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_limpar.pack(pady=5)
    botao_memoria = tk.Button(janela, text="4. Verificar Erros de Memória (Diagnóstico)", command=verificar_erros_de_memoria, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_memoria.pack(pady=5)
    botao_restaurar = tk.Button(janela, text="5. Restaurar Sistema", command=restaurar_sistema, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_restaurar.pack(pady=5)
    botao_processos = tk.Button(janela, text="7. Gerenciar Processos (Task Manager)", command=gerenciar_processos, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_processos.pack(pady=5)
    botao_backup = tk.Button(janela, text="8. Backup de Drivers", command=backup_de_drivers, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_backup.pack(pady=5)
    botao_atualizacoes = tk.Button(janela, text="9. Verificar Atualizações do Windows", command=verificar_atualizacoes, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_atualizacoes.pack(pady=5)
    botao_sysinfo = tk.Button(janela, text="10. Informações do Sistema", command=informacoes_do_sistema, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_sysinfo.pack(pady=5)
    
    # Separador visual para organizar os botões por categoria
    separador_rede = tk.Label(janela, text="--- Ferramentas de Rede ---", font=("Helvetica", 10), fg="#00BFFF", bg="#2E2E2E")
    separador_rede.pack(pady=(15, 5))

    # Botões de Rede
    botao_network = tk.Button(janela, text="6. Verificar Conectividade de Rede (Ping/Teste)", command=verificar_conectividade_de_rede, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_network.pack(pady=5)

    # Adicionando o novo botão de Limpar Cache DNS
    botao_dns = tk.Button(janela, text="11. Limpar Cache DNS", command=limpar_cache_dns, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_dns.pack(pady=5)

    # ... os outros botões virão aqui ...

    janela.mainloop()

# Inicia a aplicação
if __name__ == "__main__":
    criar_interface()