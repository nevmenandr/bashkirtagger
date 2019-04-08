#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tagger import Tagger

class TestTagger(object):
    def test_sentence(self):
        t = Tagger()
        tagged_sentence = t.predict_pos('Яңы Рәсәйҙе төҙөйәсәкбеҙ')
        assert [("яңы", "ADJ"), ("рәсәйҙе", "S"), ("төҙөйәсәкбеҙ", "V")] == tagged_sentence
    
    return 0

if __name__ == '__main__':
    main()

