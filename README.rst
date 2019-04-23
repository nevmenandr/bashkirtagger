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
will need an Internet connection and about 150 megabytes of incoming 
traffic.


Usage example
==============

Tagging one sentence at a time

::

    >>> from bashkirtagger import Tagger
    >>> t = Tagger()
    >>> sentence = "Бер кеше йәшәй."
    >>> tagged_sentence = t.predict_pos(sentence)
    >>> print(tagged_sentence)
    [('бер', 'NUM'), ('кеше', 'S'), ('йәшәй', 'V')]
    
Tagging a text of several sentences

::

    >>> from bashkirtagger import Tagger
    >>> t = Tagger()
    >>> text = "Бер кеше йәшәй. Кем белә."
    >>> tagged_text = t.text_prc(text)
    >>> print(tagged_text)
    [[('бер', 'NUM'), ('кеше', 'S'), ('йәшәй', 'V')], [("кем", "SPRO"), ("белә", "V")]]
    
    
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

You can make your own wrap of the trained model.

Model's evaluation: loss: 0.0015 - acc: 0.9996 - val_loss: 0.0975 - val_acc: 0.9847.


Contacts
==============

You can contact the contriutor of the project via email:

`Boris Orekhov <http://nevmenandr.net/bo.php>`_ (nevmenandr)

@ gmail