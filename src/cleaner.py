from pathlib import Path
from logger import logger

def clean_temp_files(directory: str, extensions: list):
    base_path = Path(directory)

    if not base_path.exists():
        print("Diretório inválido.")
        return

    removed = 0

    for file in base_path.rglob("*"):
        if file.suffix in extensions:
            file.unlink()
            removed += 1
            logger.info(f"Arquivo removido: {file}")

    print(f"{removed} arquivos temporários removidos.")