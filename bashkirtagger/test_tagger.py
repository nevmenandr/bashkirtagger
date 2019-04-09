#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tagger import Tagger

class TestTagger(object):
    def test_sentence(self):
        t = Tagger()
        tagged_sentence = t.predict_pos('Бер кеше йәшәй.')
        assert [('бер', 'NUM'), ('кеше', 'S'), ('йәшәй', 'V')] == tagged_sentence
        
    def test_text(self):
        t = Tagger()
        tagged_text = t.text_prc('Бер кеше йәшәй. Кем белә.')
        assert [[('бер', 'NUM'), ('кеше', 'S'), ('йәшәй', 'V')], [("кем", "SPRO"), ("белә", "V")]] == tagged_text


# Яңы Рәсәйҙе төҙөйәсәкбеҙ.
# Үҙ геройҙарын ватан онотмай тиҙәр.
# Йортта апай ейәнсәре менән йәшәй.
# Тау заводтары тигән яңы экспозициялар залы асыла.
# Ошоноң менән бәхәс тамам.
# Бизнесҡа ярҙам итеүгә ҙур иғтибар бүләбеҙ.

#from test_tagger import TestTagger
#t1 = TestTagger()
#t1.test_text()


