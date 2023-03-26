from pathlib import Path

# Criando um objeto Path para um arquivo existente
my_file = Path(r'C:\Users\rozen\OneDrive\Área de Trabalho\python\meu_arquivo.txt')


# Criando um objeto Path para um diretório existente
my_directory = Path(r'C:\Users\rozen\OneDrive\Área de Trabalho\python')


# Criando um novo diretório dentro do diretório atual
new_directory = Path(r'C:\Users\rozen\OneDrive\Área de Trabalho\python\novo_diretorio')
new_directory.mkdir()


# Listando todos os arquivos no diretório atual
current_directory = Path(r'C:\Users\rozen\OneDrive\Área de Trabalho\python')
for file in current_directory.glob('*'):
    print(file)
    
    
my_file = Path(r'C:\Users\rozen\OneDrive\Área de Trabalho\python\meu_arquivo.txt')
absolute_path = my_file.resolve()
print(absolute_path)    

# Verificando se um arquivo existe
my_file = Path('C:/Users/rozen/OneDrive/Área de Trabalho/python/file.txt')
if my_file.exists():
    print('O arquivo existe')

# Verificando se um diretório existe
my_directory = Path('C:/Users/rozen/OneDrive/Área de Trabalho/python/my_directory')
if my_directory.exists():
    print('O diretório existe')
