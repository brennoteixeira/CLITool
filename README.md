🚀 CLI Tool — Automação e Monitoramento com Python

  Ferramenta CLI (Command Line Interface) desenvolvida em Python para automação de tarefas operacionais e monitoramento de recursos do sistema, seguindo conceitos fundamentais de DevOps.

  O projeto simula uma ferramenta interna de infraestrutura, capaz de executar monitoramento, backup e limpeza de arquivos temporários, individualmente ou de forma encadeada (pipeline local).

🎯 Objetivo do Projeto

Demonstrar, na prática, o uso de Python como ferramenta DevOps, aplicando:

 - Automação de tarefas repetitivas

 - Monitoramento de recursos do sistema

 - Organização de código e separação de responsabilidades

- Criação de ferramentas CLI profissionais

-  Uso de configuração externa e logs

🛠️ Ferramentas, Linguagens e Tecnologias Utilizadas
Linguagem

 - Python 3

Bibliotecas Python

 - argparse
  Criação da interface de linha de comando (CLI) e parsing de argumentos.
  
-  psutil
  Coleta de métricas do sistema (CPU, memória e disco).
  
 - logging
  Geração de logs estruturados para auditoria e troubleshooting.
  
  pathlib
  Manipulação segura e moderna de caminhos de arquivos e diretórios.
  
 - shutil
  Operações de cópia e backup de diretórios.
  
 - json
  Leitura de configurações externas do projeto.
  
 - Conceitos DevOps Aplicados
  
 - Automação de infraestrutura
  
 - Monitoramento e observabilidade básica
  
 - Logging centralizado
  
 - Pipeline operacional local
  
 - Configuração externa da aplicação
  
 - Tratamento de erros e validações

⚙️ O Que o Projeto Faz (Detalhamento Técnico)

📊 Monitoramento do Sistema

 - Coleta e exibe métricas em tempo real:
  
 - Uso de CPU
  
 - Uso de memória
  
 - Uso de disco
  
 - As métricas são:
  
 - exibidas no terminal
  
 - registradas automaticamente em arquivo de log

📦 Backup de Diretórios

  - Realiza backup completo de um diretório informado:
    
  - Cria automaticamente o diretório de destino (backups/)
    
  - Gera versões com timestamp
    
  - Copia toda a estrutura de arquivos
    
  - Registra a operação em log

🧹 Limpeza de Arquivos Temporários

   - Remove arquivos temporários de um diretório alvo:
    
   - Baseado em extensões configuráveis (.log, .tmp, etc.)
    
   - Conta quantos arquivos foram removidos

   - Registra cada remoção em log

🔁 Pipeline Local (all)

   - Executa monitoramento → backup → limpeza em uma única execução.

   - Esse comando simula um pipeline operacional, muito comum em rotinas de DevOps e SRE.

Exemplo de fluxo:

   - Coleta métricas do sistema

   - Realiza backup do diretório informado

   - Remove arquivos temporários de outro diretório

📝 Logging

Todas as ações importantes do sistema são registradas:

   - métricas coletadas

   - backups realizados

   - arquivos removidos

   - erros e validações

**Os logs ficam centralizados no diretório logs/.**

📁 Estrutura do Projeto
  devops_cli/
  ├── src/
  │   ├── cli.py          # Ponto de entrada da aplicação
  │   ├── monitor.py     # Monitoramento de CPU, memória e disco
  │   ├── backup.py      # Rotina de backup de diretórios
  │   ├── cleaner.py     # Limpeza de arquivos temporários
  │   └── logger.py      # Configuração centralizada de logs
  ├── config/
  │   └── settings.json  # Configurações do projeto
  ├── backups/           # Backups gerados automaticamente
  ├── logs/              # Logs da aplicação
  └── requirements.txt   # Dependências
🔧 Configuração

As configurações do projeto ficam no arquivo:

  config/settings.json

Exemplo:

  {
    "backup_dir": "backups",
    "temp_extensions": [".tmp", ".log"],
    "cpu_alert": 80,
    "memory_alert": 80
  }
  
▶️ Como Executar

1️⃣ Instalar dependências
  pip install -r requirements.txt
2️⃣ Executar comandos disponíveis
   - Monitoramento
      python src/cli.py monitor
   - Backup
      python src/cli.py backup meu_projeto
   - Limpeza
      python src/cli.py clean tmp
   - Pipeline completo
      python src/cli.py all meu_projeto tmp

📈 Possíveis Evoluções

 - Alertas automáticos baseados em limites

 - Saída em JSON para integração com outras ferramentas

 - Dockerfile

 - Execução via cron

 - Integração com CI/CD

 - Testes automatizados

👨‍💻 Autor

Criado por Brenno Teixeira para praticar Python com foco em DevOps

⭐ Considerações Finais

Este projeto demonstra como Python pode ser utilizado de forma eficiente em rotinas DevOps, mesmo sem dependência de cloud ou ferramentas externas, focando em conceitos reais do mercado e boas práticas de automação.
