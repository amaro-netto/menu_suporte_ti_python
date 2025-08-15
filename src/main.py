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
    informacoes_do_sistema,
    desfragmentar_disco,
    gerenciar_usuarios_locais,
    verificar_integridade_dism,
    gerenciar_firewall,
    verificar_logs_de_eventos,
    testar_velocidade_de_disco,
    criar_ponto_de_restauracao,
    executar_comando_personalizado
)

# Importa as funções de ferramentas de rede
from utils.network_tools import (
    verificar_conectividade_de_rede,
    limpar_cache_dns,
    reiniciar_servicos_de_rede
)

# Importa as funções de gerenciamento de apps
from utils.app_tools import (
    gerenciar_aplicativos_winget
)

# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---

# Função para sair com uma mensagem de despedida
def sair_aplicacao(janela):
    """
    Exibe uma mensagem de despedida e fecha a janela principal.
    """
    messagebox.showinfo("Encerrando...", "Obrigado por usar o IT tool - v1.0!\n\n"
                                          "Desenvolvido por Amaro Netto e Distribuido por Amaro Netto Soluções.\n\n"
                                          "Até a próxima! 😊")
    janela.quit()

def criar_interface():
    janela = tk.Tk()
    janela.title("Menu de Reparo e Ferramentas de TI")
    janela.geometry("400x600")
    janela.configure(bg="#2E2E2E")

    titulo = tk.Label(janela, text="MENU DE REPARO E FERRAMENTAS DE TI", font=("Helvetica", 14, "bold"), fg="#00FF00", bg="#2E2E2E")
    titulo.pack(pady=10)
    subtitulo = tk.Label(janela, text="v1.0 - Desenvolvedor:  Amaro Netto | Distribuido: Amaro Netto Soluções.", font=("Helvetica", 10), fg="#00FF00", bg="#2E2E2E")
    subtitulo.pack(pady=(0, 20))

    # --- CRIAÇÃO DOS BOTÕES ---

    # Botões de Sistema
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
    
    # Separador visual
    separador_rede_topo = tk.Label(janela, text="--- Ferramentas de Rede ---", font=("Helvetica", 10), fg="#00BFFF", bg="#2E2E2E")
    separador_rede_topo.pack(pady=(15, 5))
    
    # Botões de Rede
    botao_network = tk.Button(janela, text="6. Verificar Conectividade de Rede (Ping/Teste)", command=verificar_conectividade_de_rede, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_network.pack(pady=5)
    botao_dns = tk.Button(janela, text="11. Limpar Cache DNS", command=limpar_cache_dns, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_dns.pack(pady=5)
    botao_reiniciar_rede = tk.Button(janela, text="12. Reiniciar Serviços de Rede", command=reiniciar_servicos_de_rede, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_reiniciar_rede.pack(pady=5)

    # Separador visual
    separador_sistema_meio = tk.Label(janela, text="--- Mais Ferramentas de Sistema ---", font=("Helvetica", 10), fg="#00BFFF", bg="#2E2E2E")
    separador_sistema_meio.pack(pady=(15, 5))
    
    # Mais Botões de Sistema
    botao_processos = tk.Button(janela, text="7. Gerenciar Processos (Task Manager)", command=gerenciar_processos, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_processos.pack(pady=5)
    botao_backup = tk.Button(janela, text="8. Backup de Drivers", command=backup_de_drivers, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_backup.pack(pady=5)
    botao_atualizacoes = tk.Button(janela, text="9. Verificar Atualizações do Windows", command=verificar_atualizacoes, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_atualizacoes.pack(pady=5)
    botao_sysinfo = tk.Button(janela, text="10. Informações do Sistema", command=informacoes_do_sistema, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_sysinfo.pack(pady=5)
    botao_defrag = tk.Button(janela, text="13. Desfragmentar Disco", command=desfragmentar_disco, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_defrag.pack(pady=5)
    botao_usuarios = tk.Button(janela, text="14. Gerenciar Usuarios Locais", command=gerenciar_usuarios_locais, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_usuarios.pack(pady=5)
    botao_dism = tk.Button(janela, text="15. Verificar Integridade de Arquivos (DISM)", command=verificar_integridade_dism, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_dism.pack(pady=5)
    botao_firewall = tk.Button(janela, text="16. Ativar/Desativar Firewall do Windows", command=gerenciar_firewall, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_firewall.pack(pady=5)
    botao_logs = tk.Button(janela, text="17. Verificar Logs de Eventos", command=verificar_logs_de_eventos, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_logs.pack(pady=5)
    botao_disktest = tk.Button(janela, text="18. Testar Velocidade de Disco", command=testar_velocidade_de_disco, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_disktest.pack(pady=5)
    botao_restorepoint = tk.Button(janela, text="19. Criar Ponto de Restauracao", command=criar_ponto_de_restauracao, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_restorepoint.pack(pady=5)
    botao_customcmd = tk.Button(janela, text="20. Executar Comando Personalizado (CMD)", command=executar_comando_personalizado, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_customcmd.pack(pady=5)

    # Separador de Apps
    separador_app = tk.Label(janela, text="--- Gerenciamento de Aplicativos ---", font=("Helvetica", 10), fg="#00BFFF", bg="#2E2E2E")
    separador_app.pack(pady=(15, 5))
    
    # Botão de Gerenciamento de Apps
    botao_winget = tk.Button(janela, text="21. Gerenciar Aplicativos com Winget", command=gerenciar_aplicativos_winget, bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_winget.pack(pady=5)
    
    # Botão Sair
    separador_final = tk.Label(janela, text="--------------------------------------------------------------------------------", font=("Helvetica", 8), fg="#00FF00", bg="#2E2E2E")
    separador_final.pack(pady=(20, 5))
    botao_sair = tk.Button(janela, text="22. Sair", command=lambda: sair_aplicacao(janela), bg="#3A3A3A", fg="#FF0000", font=("Helvetica", 12), width=40)
    botao_sair.pack(pady=5)
    
    janela.mainloop()

# Inicia a aplicação
if __name__ == "__main__":
    criar_interface()