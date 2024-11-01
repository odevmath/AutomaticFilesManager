# 🗂️ Organizador de Arquivos

Este script organiza automaticamente os arquivos de um diretório, classificando-os em pastas conforme o tipo de arquivo (ex: Imagens, Documentos, Vídeos, etc.). É uma maneira prática de manter seus arquivos bem organizados! 😄

## 🚀 Funcionalidades

- Organiza arquivos em pastas por tipo: Imagens, Documentos, Vídeos, Áudio, Compactados, Scripts, Programas, e Outros.
- Cria automaticamente pastas com base nos tipos de arquivos configurados.
- Verifica permissões de leitura/escrita e exibe mensagens de erro detalhadas.

## 📋 Pré-requisitos

- **Python 3.6** ou superior.
- Biblioteca `shutil` (já incluída nas bibliotecas padrão do Python).
- **PyInstaller** para criar executáveis.

## 📦 Instalação

1. **Clone** este repositório ou faça o **download** dos arquivos.
    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    cd seu_repositorio
    ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    ```

3. **Instale as dependências**:
    ```bash
    pip install pyinstaller
    ```

4. **Crie o executável**:
    ```bash
    pyinstaller --onefile organizador.py
    ```

## 📝 Como Usar

1. **Execute o script**:
   - Se você gerou um executável, ele estará na pasta `dist`:
   ```bash
   ./dist/organizador  # Para Linux/Mac
   dist\organizador.exe  # Para Windows
2. **Insira o caminho** completo do diretório que deseja organizar quando solicitado.

3. **O programa irá mover os arquivos para suas respectivas** pastas e exibirá a mensagem de conclusão. 🎉

## ⚙️ Estrutura do Código
**`FILE_TYPES:`** Dicionário que mapeia categorias a extensões de arquivos. Personalize conforme necessário.
**`organize_files(target_directory):`** Função principal que organiza os arquivos.
**Verificação de permissões e erros:** Lida com problemas de permissões e erros de movimentação.

## 📂 Exemplo de Uso
Para um diretório com os seguintes arquivos:
```plaintext
pasta_exemplo/
├── foto.jpg
├── documento.pdf
├── video.mp4
├── script.py
```
Após executar o script, a estrutura será reorganizada como:
```plaintext
pasta_exemplo/
├── Imagens/
│   └── foto.jpg
├── Documentos/
│   └── documento.pdf
├── Vídeos/
│   └── video.mp4
├── Scripts/
│   └── script.py
```

## 🛠️ Contribuição
Sinta-se à vontade para abrir issues e enviar pull requests com melhorias, correções de bugs ou novas funcionalidades! 😊

## 📄 Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

Feito com 💙 por *Matheus Santos*



