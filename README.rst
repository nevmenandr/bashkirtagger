=====================================================
 A Python LSTM-based POS-tagger for Bashkir language
=====================================================

This module contains a utility for part-of-speech tagging of Bashkir text.
The tool based on LSTM neural network and takes a word order into account.

Installation
============

The tool could be installed with pip

::

    pip3 install bashkirtagger
    
**Note:** the model for the utility must be downloaded separately. 
Due to limitations on the size of the project, I could not place it 
on a github or PiPy. After launching the program it will download 
and unpack the model. No action is necessary on your part. But you 
will need an Internet connection and about 50 megabytes of incoming 
traffic.


Usage example
==============

Tagging one sentence at a time

::

    >>> from tagger import Tagger
    >>> t = Tagger()
    >>> sentence = "Яңы Рәсәйҙе төҙөйәсәкбеҙ."
    >>> tagged_sentence = t.predict_pos(sentence)
    >>> print(tagged_sentence)
    [("яңы", "ADJ"), ("рәсәйҙе", "S"), ("төҙөйәсәкбеҙ", "V")]
    
Tagging a text of several sentences

::

    >>> from tagger import Tagger
    >>> t = Tagger()
    >>> text = "Яңы Рәсәйҙе төҙөйәсәкбеҙ. Бизнесҡа ярҙам итеүгә ҙур 
    иғтибар бүләбеҙ."
    >>> tagged_text = t.text_prc(text)
    >>> print(tagged_text)
    [[("яңы", "ADJ"), ("рәсәйҙе", "S"), ("төҙөйәсәкбеҙ", "V")], 
    [("бизнесҡа", "S"), ("ярҙам", "S"), ("итеүгә", "V"), ("ҙур", "ADJ"), 
    ("иғтибар", "S"), ("бүләбеҙ", "V")]]
    
    
Tagset
==============

Tagset based on `Bashmorph morphological analyzer <http://nevmenandr.net/cgi-bin/bashmorphweb.py>`_ for Bashkir language 
by Boris Orekhov.

* S: substantive
* V: verb
* ADJ: adjective
* NUM: numeral
* SPRO: pronoun
* PART: particle
* INTJ: interjunction
* POST: postposition
* CONJ: conjunction

See the `paper <http://nevmenandr.net/personalia/bashmorph_problems.pdf>`_ for the details.

Data
==============

The model trained on collected from the web `Bashkir text corpus <https://github.com/nevmenandr/bashkir-corpus>`_ which 
was marked up by Bashmorph.

This tool can be used for disambiguation of rule-based markup.

You an make your own wrap of the trained model.


Contacts
==============

You can contact the contriutor of the project via email:

`Boris Orekhov <http://nevmenandr.net/bo.php>`_ (nevmenandr)

@ gmail