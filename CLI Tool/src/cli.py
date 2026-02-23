import argparse
import json
from monitor import system_status
from backup import backup_directory
from cleaner import clean_temp_files

CONFIG_PATH = "config/settings.json"


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def main():
    config = load_config()

    parser = argparse.ArgumentParser(
        description="DevOps CLI Tool - Automação e Monitoramento"
    )

    subparsers = parser.add_subparsers(dest="command")

    # monitor
    subparsers.add_parser("monitor", help="Monitorar sistema")

    # backup
    backup_parser = subparsers.add_parser("backup", help="Realizar backup")
    backup_parser.add_argument("source", help="Diretório de origem")

    # clean
    clean_parser = subparsers.add_parser("clean", help="Limpar arquivos temporários")
    clean_parser.add_argument("directory", help="Diretório alvo")

    # all (pipeline)
    all_parser = subparsers.add_parser(
        "all", help="Executa monitoramento, backup e limpeza"
    )
    all_parser.add_argument("source", help="Diretório para backup")
    all_parser.add_argument("clean_dir", help="Diretório para limpeza")

    args = parser.parse_args()

    if args.command == "monitor":
        system_status()

    elif args.command == "backup":
        backup_directory(args.source, config["backup_dir"])

    elif args.command == "clean":
        clean_temp_files(args.directory, config["temp_extensions"])

    elif args.command == "all":
        print("\n========== SYSTEM MONITOR ==========")
        system_status()

        print("\n========== BACKUP ==========")
        backup_directory(args.source, config["backup_dir"])

        print("\n========== CLEAN ==========")
        clean_temp_files(args.clean_dir, config["temp_extensions"])

    else:
        parser.print_help()


if __name__ == "__main__":
    main()