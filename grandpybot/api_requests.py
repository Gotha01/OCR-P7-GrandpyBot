#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipediaapi
import random
import requests

class Wiki_search():
    """Function to search in Wikipedia-API."""
    def __init__(self, zone, adress="", desc_sentences=2):
        """
            Init function for Wiki-search class.
        Args:
            zone (str): Name of the zone to search.
            adress (str, optional): optional return if search don't match. Defaults to "".
            desc_sentences (int, optional): Number of sentences needed to return the description of the wikipedia page. Defaults to 2.
        """
        self.zone = zone
        self.adress = adress
        self.desc_sent = desc_sentences
        self.bot_said = [
            "J'y suis passé plusieurs fois dans ma vie. ",
            "Alors, écoute bien jusqu'au bout. ",
            "Pour avoir étudié cet endroit dans ma jeunesse, je peux t'en dire plusieurs choses.",
            "Laisse moi te raconter ce que j'en sais. "]
        self.bot_error = [
            "Je ne crois pas avoir déjà entendu parler de cet endroit.",
            "Tu sais, de mon temps, ce lieu s'appelait peut-être différemment.\
            Regarde le GPS, peut-être en sait-il plus que moi."
        ]
        self.count = 1
        self.search = self.search_zone()
        self.less_parens_search = self.remove_nested_parens()
        self.many_sentences_search = self.sentences_search()
        self.good_syntax_search = self.cleaning_syntax()
        self.answer = self.finally_answer()

    def search_zone(self):
        """ Returns, if available, the first seven hundred characters
            of the wikipedia description of the selected location"""
        wiki_config = wikipediaapi.Wikipedia('fr')
        result = wiki_config.page(self.zone)
        if result.exists():
            words = result.summary[0:1000]
            if "== Toponym" in words:
                self.count -= 1
                return words
            else:
                return words
        else:
            self.count -= 1 
            return "Êtes-vous sûr de l'avoir écrit correctement?"
    
    def remove_nested_parens(self):
        """ Returns a copy of 'input_str' with any parenthesized text removed. 
            Nested parentheses are handled."""
        result = ''
        paren_level = 0
        for ch in self.search:
            if ch == '(' or ch == '[':
                paren_level += 1
            elif (ch == ')' or ch == ']') and paren_level:
                paren_level -= 1
            elif not paren_level:
                result += ch
        return result
    
    def sentences_search(self):
        """ Function to split text on '.' but ignore them in dates. """
        sentences_list = self.less_parens_search.split(".")
        if "-C" in sentences_list:
            index_of = sentences_list.index("-C")
            sentences_list.pop(index_of)
            sentences_list.pop(index_of-1)
            to_replace = sentences_list[index_of-2]
            sentences_list[index_of-2] = to_replace + " J-C"
        if len(sentences_list) >= 2:
            random_sentences = random.randint(0, (len(sentences_list)-2))
            sentences_to_show = sentences_list[random_sentences:random_sentences+self.desc_sent]
            result = ".".join(sentences_to_show) + "."
            return result
        elif len(sentences_list) << 2:
            result = ".".join(sentences_list) + "."
            return result
        elif "Êtes-vous sûr de l'avoir écrit correctement?" in sentences_list:
            return "Êtes-vous sûr de l'avoir écrit correctement?"

    def cleaning_syntax(self):
        """ Returns sentences with better syntactic appearence."""
        return self.many_sentences_search.replace(",.", ".").replace(" ,", ",").replace("  ", " ").replace(". ", ".\n")
    
    def finally_answer(self):
        """ Returns a str which could be an answer for a bot."""
        if self.count:
            result = self.bot_said[random.randint(0, 3)] + self.good_syntax_search
            return result
        elif self.adress != "":
            result = "Je connais l'adresse mais ne sait pas grand chose dessus. C'est au "+ self.adress
            return result
        else:
            return self.bot_error[random.randint(0, 1)]


class Google_maps_search():
    """Find the coordinates on Google Maps API from an text"""
    def __init__(self, key):
        self.key = key
        
    def request_google(self, user_input=""):
        to_search = {}
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
        info = {"input": user_input,
                 "key": self.key,
                 "inputtype": "textquery",
                 "fields": "formatted_address,name,geometry",
                 "language": "fr"
                 }
        request = requests.get(url, params=info)
        if request.status_code == requests.codes.ok:
            answer = request.json()
            if answer['status'] != 'ZERO_RESULTS':
                result = answer['candidates'][0]
                to_search['address'] = result['formatted_address']
                to_search['name'] = result['name']
                to_search['lati'] = result['geometry']['location']['lat']
                to_search['lngi'] = result['geometry']['location']['lng']
                return to_search
            else:
                to_search['address'] = ""
                return to_search