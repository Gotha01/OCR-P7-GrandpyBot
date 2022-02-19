#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.command.clean import clean


class Parser():
    """Class to parse text through a stop-words list."""
    def __init__(self, sentence=str):
        """
            Init function.
        Args:
            sentence (str): [text to parse]. Defaults to str.
        """
        self.parse_list = [
            'a',
            'abord',
            'absolument',
            'adresse',
            'afin',
            'ah',
            'ai',
            'aie',
            'ailleurs',
            'ainsi',
            'ait',
            'allaient',
            'allo',
            'allons',
            'allô',
            'alors',
            'anterieur',
            'anterieure',
            'anterieures',
            'apres',
            'après',
            'as',
            'assez',
            'attendu',
            'au',
            'aucun',
            'aucune',
            'aujourd',
            "aujourd'hui",
            'aupres',
            'auquel',
            'aura',
            'auraient',
            'aurait',
            'auront',
            'aussi',
            'autre',
            'autrefois',
            'autrement',
            'autres',
            'autrui',
            'aux',
            'auxquelles',
            'auxquels',
            'avaient',
            'avais',
            'avait',
            'avant',
            'avec',
            'avoir',
            'avons',
            'ayant',
            'b',
            'bah',
            'bas',
            'basee',
            'bat',
            'beau',
            'beaucoup',
            'bien',
            'bientôt',
            'bigre',
            'bonjour',
            'bonsoir',
            'boum',
            'bravo',
            'brrr',
            'c',
            'car',
            'ce',
            'ceci',
            'cela',
            'celle',
            'celle-ci',
            'celle-là',
            'celles',
            'celles-ci',
            'celles-là',
            'celui',
            'celui-ci',
            'celui-là',
            'cent',
            'cependant',
            'certain',
            'certaine',
            'certaines',
            'certains',
            'certes',
            'ces',
            'cet',
            'cette',
            'ceux',
            'ceux-ci',
            'ceux-là',
            'chacun',
            'chacune',
            'chaque',
            'cher',
            'cherche',
            'chers',
            'chez',
            'chiche',
            'chut',
            'chère',
            'chères',
            'chose',
            'ci',
            'cinq',
            'cinquantaine',
            'cinquante',
            'cinquantième',
            'cinquième',
            'clac',
            'clic',
            'combien',
            'comme',
            'comment',
            'comparable',
            'comparables',
            'compris',
            'concernant',
            'connais',
            'connaissais',
            'connais-tu',
            'contre',
            'couic',
            'crac',
            "d'",
            'da',
            'dans',
            'de',
            'debout',
            'dedans',
            'dehors',
            'deja',
            'delà',
            'depuis',
            'dernier',
            'derniere',
            'derriere',
            'derrière',
            'des',
            'desormais',
            'desquelles',
            'desquels',
            'dessous',
            'dessus',
            'deux',
            'deuxième',
            'deuxièmement',
            'devant',
            'devers',
            'devra',
            'different',
            'differentes',
            'differents',
            'différent',
            'différente',
            'différentes',
            'différents',
            'dire',
            'directe',
            'directement',
            'dis',
            'dit',
            'dite',
            'dits',
            'divers',
            'diverse',
            'diverses',
            'dix',
            'dix-huit',
            'dix-neuf',
            'dix-sept',
            'dixième',
            'doit',
            'doivent',
            'donc',
            'donne', 
            'donnez',
            'dont',
            'douze',
            'douzième',
            'dring',
            'du',
            'duquel',
            'durant',
            'dès',
            'désormais',
            'e',
            'effet',
            'egale',
            'egalement',
            'egales',
            'eh',
            'elle',
            'elle-même',
            'elles',
            'elles-mêmes',
            'en',
            'encore',
            'enfin',
            'entre',
            'envers',
            'environ',
            'es',
            'est',
            'est-ce',
            'et',
            'etant',
            'etc',
            'etre',
            'eu',
            'euh',
            'eux',
            'eux-mêmes',
            'exactement',
            'excepté',
            'extenso',
            'exterieur',
            'f',
            'fais',
            'faisaient',
            'faisant',
            'fait',
            'façon',
            'feront',
            'fi',
            'flac',
            'floc',
            'font',
            'g',
            'gens',
            'grandpy',
            'grandpybot',
            'h',
            'ha',
            'hein',
            'hem',
            'hep',
            'hi',
            'ho',
            'holà',
            'hop',
            'hormis',
            'hors',
            'hou',
            'houp',
            'hue',
            'hui',
            'huit',
            'huitième',
            'hum',
            'hurrah',
            'hé',
            'hélas',
            'i',
            'infos',
            'il',
            'ils',
            'importe',
            'j',
            'je',
            'jusqu',
            'jusque',
            'juste',
            'k',
            'l',
            'la',
            'laisser',
            'laquelle',
            'las',
            'le',
            'lequel',
            'les',
            'lesquelles',
            'lesquels',
            'leur',
            'leurs',
            'longtemps',
            'lors',
            'lorsque',
            'lui',
            'lui-meme',
            'lui-même',
            'là',
            'lès',
            'm',
            'ma',
            'maint',
            'maintenant',
            'mais',
            'malgre',
            'malgré',
            'maximale',
            'me',
            'meme',
            'memes',
            'merci',
            'mes',
            'mien',
            'mienne',
            'miennes',
            'miens',
            'mille',
            'mince',
            'minimale',
            'moi',
            'moi-meme',
            'moi-même',
            'moindres',
            'moins',
            'mon',
            'moyennant',
            'multiple',
            'multiples',
            'même',
            'mêmes',
            'n',
            'na',
            'naturel',
            'naturelle',
            'naturelles',
            'ne',
            'neanmoins',
            'necessaire',
            'necessairement',
            'neuf',
            'neuvième',
            'ni',
            'nombreuses',
            'nombreux',
            'non',
            'nos',
            'notamment',
            'notre',
            'nous',
            'nous-mêmes',
            'nouveau',
            'nul',
            'néanmoins',
            'nôtre',
            'nôtres',
            'o',
            'oh',
            'ohé',
            'ollé',
            'olé',
            'on',
            'ont',
            'onze',
            'onzième',
            'ore',
            'ou',
            'ouf',
            'ouias',
            'oust',
            'ouste',
            'outre',
            'ouvert',
            'ouverte',
            'ouverts',
            'o|',
            'où',
            'p',
            'paf',
            'pan',
            'papy',
            'par',
            'parce',
            'parfois',
            'parle',
            'parlent',
            'parler',
            'parmi',
            'parseme',
            'partant',
            'particulier',
            'particulière',
            'particulièrement',
            'pas',
            'passé',
            'pendant',
            'pense',
            'permet',
            'personne',
            'peu',
            'peut',
            'peuvent',
            'peux',
            'pff',
            'pfft',
            'pfut',
            'pif',
            'pire',
            'plein',
            'plouf',
            'plus',
            'plusieurs',
            'plutôt',
            'possessif',
            'possessifs',
            'possible',
            'possibles',
            'pouah',
            'pour',
            'pourquoi',
            'pourrais',
            'pourrait',
            'pouvait',
            'prealable',
            'precisement',
            'premier',
            'première',
            'premièrement',
            'pres',
            'probable',
            'probante',
            'procedant',
            'proche',
            'près',
            'psitt',
            'pu',
            'puis',
            'puisque',
            'pur',
            'pure',
            'q',
            'qu',
            'quand',
            'quant',
            'quant-à-soi',
            'quanta',
            'quarante',
            'quatorze',
            'quatre',
            'quatre-vingt',
            'quatrième',
            'quatrièmement',
            'que',
            'quel',
            'quelconque',
            'quelle',
            'quelles',
            "quelqu'un",
            'quelque',
            'quelques',
            'quels',
            'qui',
            'quiconque',
            'quinze',
            'quoi',
            'quoique',
            'r',
            'rare',
            'rarement',
            'rares',
            'relative',
            'relativement',
            'remarquable',
            'rend',
            'rendre',
            'restant',
            'reste',
            'restent',
            'restrictif',
            'retour',
            'revoici',
            'revoilà',
            'rien',
            's',
            'sa',
            'sacrebleu',
            'salut',
            'sais',
            'sais-tu',
            'sait',
            'sans',
            'sapristi',
            'sauf',
            'savoir',
            'se',
            'sein',
            'seize',
            'selon',
            'semblable',
            'semblaient',
            'semble',
            'semblent',
            'sent',
            'sept',
            'septième',
            'sera',
            'seraient',
            'serait',
            'seront',
            'ses',
            'seul',
            'seule',
            'seulement',
            'si',
            'sien',
            'sienne',
            'siennes',
            'siens',
            'sinon',
            'six',
            'sixième',
            'soi',
            'soi-même',
            'soit',
            'soixante',
            'son',
            'sont',
            'sous',
            'souvent',
            'specifique',
            'specifiques',
            'speculatif',
            'stop',
            'strictement',
            'subtiles',
            'suffisant',
            'suffisante',
            'suffit',
            'suis',
            'suit',
            'suivant',
            'suivante',
            'suivantes',
            'suivants',
            'suivre',
            'superpose',
            'sur',
            'surtout',
            't',
            'ta',
            'tac',
            'tant',
            'tardive',
            'te',
            'tel',
            'telle',
            'tellement',
            'telles',
            'tels',
            'tenant',
            'tend',
            'tenir',
            'tente',
            'tes',
            'tic',
            'tien',
            'tienne',
            'tiennes',
            'tiens',
            'toc',
            'toi',
            'toi-même',
            'ton',
            'touchant',
            'toujours',
            'tous',
            'tout',
            'toute',
            'toutefois',
            'toutes',
            'treize',
            'trente',
            'tres',
            'trois',
            'troisième',
            'troisièmement',
            'trop',
            'trouve',
            'très',
            'tsoin',
            'tsouin',
            'tu',
            'té',
            'u',
            'un',
            'une',
            'unes',
            'uniformement',
            'unique',
            'uniques',
            'uns',
            'v',
            'va',
            'vais',
            'vas',
            'vers',
            'via',
            'vif',
            'vifs',
            'ville',
            'vingt',
            'vivat',
            'vive',
            'vives',
            'vlan',
            'voici',
            'voilà',
            'vont',
            'vos',
            'votre',
            'vous',
            'vous-mêmes',
            'voudrais',
            'voyage',
            'voyages',
            'vu',
            'vé',
            'vôtre',
            'vôtres',
            'w',
            'x',
            'y',
            'z',
            'zut',
            'à',
            'â',
            'ça',
            'ès',
            'étaient',
            'étais',
            'était',
            'étant',
            'été',
            'être',
            'ô',
            'aucuns',
            'bon',
            'devrait',
            'dos',
            'droite',
            'début',
            'essai',
            'faites',
            'fois',
            'force',
            'haut',
            'ici',
            'mine',
            'mot',
            'nommés',
            'nouveaux',
            'parole',
            'personnes',
            'pièce',
            'plupart',
            'soyez',
            'sujet',
            'tandis',
            'valeur',
            'voie',
            'voient',
            'voulais',
            'vieux',
            'état',
            'étions'
            ]
        self.sentence = sentence.lower()
        self.result = self.to_parse()

    def to_parse(self):
        """
            Function to parse in class Parser which removes symbols
            and split sentences from a text.
        Returns:
            [str]: [text whithout stop-words and punctuation]
        """
        clean_words = [" "]
        linki_words  = ["de", "du", "des", "le", "la", "les", "des"]
        list_of_words = self.sentence.split()
        last_word_checked = str()
        for word in list_of_words:
            just_word = word.replace("!","").replace("?","")\
                .replace(',', "").replace(".", "")
            if last_word_checked == clean_words[-1] and just_word in linki_words:
                clean_words.append(just_word)
                last_word_checked = just_word
            else:
                if "'" not in just_word:
                    if just_word not in self.parse_list:
                        clean_words.append(just_word)
                        last_word_checked = just_word
                else:
                    onlyword = just_word[2:]
                    if onlyword not in self.parse_list:
                        clean_words.append(onlyword)
                        last_word_checked = onlyword
        parse_sentence = " ".join(clean_words[1:])
        return parse_sentence