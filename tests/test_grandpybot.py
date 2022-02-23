import urllib.request

from grandpybot import api_requests as apir
from grandpybot import parser as pa
from config_user import google_api_key



# Parsing test
def test_parsing():
    """
        Tests the efficiency of the parser to filter a string of characters 
        and keep only the useful elements for the rest of the function
    """
    a1 = "Salut Grandpybot! J'ai un voyage bientôt et je voudrais savoir si tu connaissais quelque chose sur la ville de Moscou."
    expect_for_a1 = ['moscou']
    assert pa.Parser(a1).result == expect_for_a1[0]


#Google maps API test
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

# Wiki API tests
class Test_wiki:
    def setup_method(self):
        self.length = 1000
        self.type = str
        self.bot_error = [
                "Je ne crois pas avoir déjà entendu parler de cet endroit.",
                "Tu sais, de mon temps, ce lieu s'appelait peut-être différemment.\
                Regarde le GPS, peut-être en sait-il plus que moi.",
                "Êtes-vous sûr de l'avoir écrit correctement?"
            ]
        self.normal_search_zone = apir.Wiki_search("Dakar").search_zone()
        self.bad_search = apir.Wiki_search("vezrhnthgrea").search_zone()
        

    def test_type_wiki(self):
        assert type(self.normal_search_zone) == self.type
    def test_len_wiki(self):
        assert len(self.normal_search_zone) <= self.length
    def test_bad_search(self):
        assert self.bad_search in self.bot_error


#mock final pour la fonction qui traite la question de manière générale