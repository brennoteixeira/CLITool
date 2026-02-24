import shutil
from datetime import datetime
from pathlib import Path
from logger import logger


def backup_directory(source: str, backup_root: str):
    source_path = Path(source)
    backup_root_path = Path(backup_root)

    if not source_path.exists():
        print("Diretório não encontrado.")
        logger.error(f"Diretório de origem não encontrado: {source}")
        return

    # cria o diretório de backup se não existir
    backup_root_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_root_path / f"backup_{timestamp}"

    shutil.copytree(source_path, backup_path)

    logger.info(f"Backup criado com sucesso em {backup_path}")
    print(f"Backup realizado com sucesso em: {backup_path}")