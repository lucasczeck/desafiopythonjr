import json
import re


class Expression:
    """
    Classe para leitura de expressões de um arquivo de texto.
    """

    def __init__(self, txt: str):
        """
        Construtor da classe Expression.

        Args:
            txt (str): Caminho do arquivo de texto contendo as expressões.
        """
        self.txt = txt

    def txt_to_list(self) -> list:
        """
        Lê as expressões do arquivo de texto e as retorna em uma lista.

        Returns:
            list: Lista contendo as expressões do arquivo de texto.
        """
        with open(self.txt, "r", encoding='utf-8') as txt:
            lines = txt.readlines()
            expressions_list = [line.strip() for line in lines]

        return expressions_list


class Text:
    """
    Classe para leitura e processamento de arquivos JSON contendo textos.
    """

    def __init__(self, json_file: str):
        """
        Construtor da classe Text.

        Args:
            json_file (str): Caminho do arquivo JSON contendo os textos.
        """
        self.json_file = json_file

    def read_json(self) -> list:
        """
        Lê o arquivo JSON e retorna uma lista contendo os textos.

        Returns:
            list: Lista contendo os textos do arquivo JSON.
        """
        with open(self.json_file, 'r', encoding='utf-8') as file:
            texts = json.load(file)

        return texts

    def split_sentences(self) -> dict:
        """
        Separa as frases dos textos e retorna um dicionário contendo as frases separadas para cada texto.

        Returns:
            dict: Dicionário contendo as frases separadas para cada texto.
        """
        texts = self.read_json()
        sentences = {}
        for text in texts:
            id = text['id']
            text = text['texto']
            sentences_text = re.split(r'(?<=[.?!])\s+', text)
            sentences_text = [sentence.strip() for sentence in sentences_text]
            sentences_text = [sentence for sentence in sentences_text if sentence]
            if id in sentences:
                sentences[id].extend(sentences_text)
            else:
                sentences[id] = sentences_text

        return sentences


class Compare:
    """
    Classe para comparação de frases com expressões.
    """

    def __init__(self, sentences: dict, expressions_file: str):
        """
        Construtor da classe Compare.

        Args:
            sentences (dict): Dicionário contendo as frases a serem comparadas.
            expressions_file (str): Caminho do arquivo contendo as expressões a serem buscadas nas frases.
        """
        self.sentences = sentences
        self.expressions = Expression(expressions_file).txt_to_list()

    @staticmethod
    def get_tokens(sentence: str) -> list:
        """
        Retorna uma lista de tokens de uma frase.

        Args:
            sentence (str): Frase a ser tokenizada.

        Returns:
            List: Lista de tokens da frase.
        """
        tokens_list = re.findall(r"[\w']+|[.,!?;]", sentence)

        return tokens_list[:3]

    def create_json_list(self) -> list:
        """
        Cria uma lista de dicionários contendo a frase e a expressão correspondente em cada frase.

        Returns:
            list: Lista de dicionários contendo a frase e a expressão correspondente em cada frase.
        """
        list_for_json = []
        for id, sentences in self.sentences.items():
            sentences_list = []
            for sentence in sentences:
                sentence_dict = {"sentença": sentence,
                                 "expressão": self.find_expression_in_sentence(sentence)}
                sentences_list.append(sentence_dict)

            text_dict = {"id": id,
                         "sentenças": sentences_list}
            list_for_json.append(text_dict)

        return list_for_json

    def find_expression_in_sentence(self, sentence: str) -> str or None:
        """
        Busca uma expressão em uma frase e retorna a primeira expressão encontrada.

        Args:
            sentence (str): Frase a ser verificada.

        Returns:
            Optional[str]: A primeira expressão encontrada na frase, ou None se nenhuma expressão for encontrada.
        """
        tokens = self.get_tokens(sentence)

        for expression in self.expressions:
            if re.findall(r"[\w']+|[.,!?;]", expression)[0] in tokens:
                return expression

        return None

    @staticmethod
    def create_json_file(list_for_json: list) -> None:
        """
        Cria um arquivo JSON com a lista de dicionários passada como parâmetro.

        Args:
            list_for_json (list): Lista de dicionários contendo as frases e expressões correspondentes.

        Returns:
            None.
        """
        out_file = open("output.json", "w", encoding='utf-8')
        json.dump(list_for_json, out_file, indent=4, ensure_ascii=False)
        out_file.close()


class Execute:
    """
    Classe responsável por executar o programa e criar o arquivo JSON resultante.
    """

    def __init__(self, json: str, txt: str):
        """
        Construtor da classe Execute.

        Recebe os caminhos dos arquivos JSON e de texto contendo as informações necessárias para processamento.

        Inicializa os atributos 'sentences', 'comparison', 'list_for_json' e cria o arquivo JSON.

        Args:
            json (str): Caminho do arquivo JSON contendo os textos a serem processados.
            txt (str): Caminho do arquivo de texto contendo as expressões a serem buscadas nas frases.
        """
        self.sentences = Text(json).split_sentences()
        self.comparison = Compare(self.sentences, txt)
        self.list_for_json = self.comparison.create_json_list()
        self.comparison.create_json_file(self.list_for_json)
        print('Arquivo json criado com sucesso!')
