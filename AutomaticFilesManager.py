import os
import shutil

# Tipos de arquivos conforme extensão
FILE_TYPES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Áudio": [".mp3", ".wav", ".aac", ".ogg"],
    "Compactados": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"],
    "Programas": [".exe", ".msi", ".bat"],
    "Outros": []  # Para categorias indefinidas
}


def organize_files(target_directory):
    # Verifica se o diretório existe e se temos permissões de leitura/escrita
    if not os.path.isdir(target_directory):
        print(f"Erro: O diretório {target_directory} não existe.")
        return

    if not os.access(target_directory, os.R_OK) or not os.access(target_directory, os.W_OK):
        print(f"Erro: Sem permissão de leitura/escrita para o diretório {target_directory}.")
        return

    # Itera sobre todos os arquivos no diretório alvo
    for file in os.listdir(target_directory):
        file_path = os.path.join(target_directory, file)

        # Ignora subpastas, tratando apenas dos arquivos
        if os.path.isfile(file_path):
            # Identifica a categoria do arquivo com base em sua extensão
            category = "Outros"  # Categoria padrão caso a extensão não seja identificada
            for file_type, extensions in FILE_TYPES.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    category = file_type
                    break

            # Define o caminho da pasta de destino
            dest_folder = os.path.join(target_directory, category)
            # Cria a pasta, se não existir
            os.makedirs(dest_folder, exist_ok=True)

            # Tenta mover o arquivo para a pasta de destino, capturando possíveis erros
            try:
                shutil.move(file_path, os.path.join(dest_folder, file))
                print(f"Movido: {file} --> {category}")
            except Exception as e:
                print(f"Erro ao mover {file} para {category}: {e}")

    print("\nOrganização concluída!")


# Executa o script
if __name__ == "__main__":
    print("Bem-vindo ao Organizador de Arquivos! 🎉")
    directory = input("Por favor, insira o caminho completo do diretório que deseja organizar: ")
    organize_files(directory)
    print("Organização concluída com sucesso! ✅")