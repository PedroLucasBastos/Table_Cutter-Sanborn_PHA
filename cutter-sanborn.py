import os
import importlib.util

pasta = "dados" # o nome da pasta onde estão os arquivos
nome_autor = input("Digite o seu nome: ") # obtém o nome do usuário
nome_autor = nome_autor.lower().replace(",", "").replace(" ", "") # formata o nome
letra = nome_autor[0] # obtém a primeira letra do nome
arquivo = f"{letra}.py" # o nome do arquivo com a extensão
caminho = os.path.join(pasta, arquivo) # o caminho do arquivo na pasta
spec = importlib.util.spec_from_file_location(letra, caminho) # cria a especificação do módulo
modulo = importlib.util.module_from_spec(spec) # cria o módulo a partir da especificação
spec.loader.exec_module(modulo) # executa o módulo
# faça o que quiser com o módulo importado

def code(nome_autor):
    table = modulo.get_table() # chama a função get_table
    nome_autor = nome_autor.lower().replace(",", "").replace(" ", "")
    tabela_selecionada = table[letra]
    selecionado= ''
    for code, name in tabela_selecionada:
        if name > nome_autor:
            break
        selecionado = code
    return f'{nome_autor[0].upper()}{selecionado}'


if __name__ == "__main__":
    print(code(nome_autor))
