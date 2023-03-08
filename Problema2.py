class ValidateSequence:
    """
    Classe que valida sequências de caracteres contendo os caracteres '(', ')', '{', '}', '[' e ']'.
    """

    def __init__(self, sequence=None):
        """
        Construtor da classe ValidateSequence.

        Args:
            sequence (str, optional): Sequência de caracteres a ser validada. Pode ser None se a validação
                for feita por meio do método get_input. Defaults to None.
        """
        self.sequence = sequence
        self.queue = []

    def validator(self) -> bool:
        """
        Verifica se a sequência de caracteres contendo '(', ')', '{', '}', '[' e ']' é válida.

        Returns:
            bool: True se a sequência for válida, False caso contrário.
        """
        if self.sequence in ('', ' '):
            return True
        else:
            for character in self.sequence:
                if character in ['(', '{', '[']:
                    self.queue.append(character)

                elif character == ')' and (not self.queue or self.queue[-1] != '('):
                    return False

                elif character == '}' and (not self.queue or self.queue[-1] != '{'):
                    return False

                elif character == ']' and (not self.queue or self.queue[-1] != '['):
                    return False

                else:
                    self.queue.pop()

            return not self.queue

    @staticmethod
    def get_input():
        """
        Método estático que recebe a entrada do usuário e valida a sequência de caracteres.
        """
        valid_characters = ["{", "}", "[", "]", "(", ")", ' ', '']
        repeat_valid_characters = ['0', '1']

        valid_sequence = lambda x: all(character in valid_characters for character in x)
        valid_repeat = lambda x: all(character in repeat_valid_characters for character in x)

        while True:
            sequence = input("Insira uma sequência de caracteres contendo apenas {} [] (): ")

            if valid_sequence(sequence):
                status = ValidateSequence(sequence).validator()
                print(status)
                while True:
                    repeat = input("Deseja inserir outra sequência? Digite 1 para SIM ou 0 para não")

                    if valid_repeat(repeat):
                        if repeat == '1':
                            break
                        else:
                            print('Encerrando o programa, até logo!')
                            return
                    else:
                        print("Opção inválida.")
                        continue
            else:
                print("A sequência de caracteres contém caracteres inválidos.")

    def start(self):
        """
        Método que inicia a validação da sequência de caracteres.
        """
        self.get_input()
