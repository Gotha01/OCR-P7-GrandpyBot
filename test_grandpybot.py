import pytest
from grandpybot.parser import Parser
from grandpybot.api_requests import *

def test_parsing():
    a1 = "Salut Grandpybot! J'ai un voyage bientôt et je voudrais savoir si tu connaissais quelque chose sur la ville de Moscou."
    expect_for_a1 = ['moscou']
    print(Parser(a1).result)
    assert Parser(a1).result == expect_for_a1[0]

test_parsing()


#mock test pour l'API google
#mock test pour l'API Wikipedia
#mock final pour la fonction qui traite la question de manière générale