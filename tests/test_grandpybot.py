import urllib.request

from grandpybot import api_requests as apir
from grandpybot import parser as pa
from config_user import google_api_key

def test_parsing():
    """
        Tests the efficiency of the parser to filter a string of characters 
        and keep only the useful elements for the rest of the function
    """
    a1 = "Salut Grandpybot! J'ai un voyage bientôt et je voudrais savoir si tu connaissais quelque chose sur la ville de Moscou."
    expect_for_a1 = ['moscou']
    print(pa.Parser(a1).result)
    assert pa.Parser(a1).result == expect_for_a1[0]

def test_API_google(monkeypatch):
    """
        Tests the retrieval of data in an object during a query on the Google Maps API
    """
    results = {
        'address': 'Marseille, France',
        'lati': 43.296482,
        'lngi': 5.36978,
        'name': 'Marseille'
        }
    
    def mockreturn(request):
        return results
    
    monkeypatch.setattr(urllib.request, "urlopen", mockreturn)

    assert apir.Google_maps_search(google_api_key).request_google(user_input="marseille") == results

def test_API_Wiki(monkeypatch):
    """Tests the length and type of the 'Wiki_search.search_zone' function response"""
    results = {
        "type" : str,
        "lenght": 1000
        }
    assert type(apir.Wiki_search("Dakar").search_zone()) == results['type']
    assert len(apir.Wiki_search("Dakar").search_zone()) <= results['lenght']

#mock final pour la fonction qui traite la question de manière générale