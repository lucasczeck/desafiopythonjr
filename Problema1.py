def find_substring_in_string(s1, s2):
    """
    Conta o número de ocorrências da string s2 dentro da string s1.

    Args:
        s1 (str): A string principal onde se deve buscar ocorrências da string s2.
        s2 (str): A string a ser buscada em s1.

    Returns:
        int: O número de ocorrências de s2 em s1.
    """
    count = 0
    index = 0

    while index >= 0:
        index = s1.find(s2, index)
        if index < 0:
            break
        count += 1
        index += 1

    return count


def start():
    """
    Função principal que solicita ao usuário as strings s1 e s2 e exibe o número de ocorrências de s2 em s1.
    """
    s1 = input('Insira a primeira string: ')
    s2 = input('Insira a segunda string: ')
    result = find_substring_in_string(s1, s2)
    print(result)
