#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipediaapi
import random
import requests

class Wiki_search():
    def __init__(self, zone, desc_sentences=2):
        self.zone = zone
        self.desc_sent = desc_sentences
        self.bot_said = [
            "J'y suis passé plusieurs fois dans ma vie. ",
            "Alors, écoute bien jusqu'au bout. ",
            "Pour en avoir fait la visite il y a longtemps, ",
            "Laisse moi te raconter ce que j'en sais. "]
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
            words = result.summary[0:700]
            return words
        else:
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
        sentences_list = self.less_parens_search.split(".")
        sentences_to_show = sentences_list[:self.desc_sent]
        result = ".".join(sentences_to_show) + "."
        return result

    def cleaning_syntax(self):
        return self.many_sentences_search.replace(",.", ".").replace(" ,", ",").replace("  ", " ").replace(". ", ".\n")
    
    def finally_answer(self):
        if self.good_syntax_search != "Êtes-vous sûr de l'avoir écrit correctement?":
            result = self.bot_said[random.randint(0, 3)] + self.good_syntax_search
            return result
        else:
            return self.good_syntax_search


class Google_maps_search():
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
            result = answer['candidates'][0]
            to_search['address'] = result['formatted_address']
            to_search['name'] = result['name']
            to_search['lati'] = result['geometry']['location']['lat']
            to_search['lngi'] = result['geometry']['location']['lng']
            return to_search