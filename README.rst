.. image:: https://github.com/eumiro/lumipallo/workflows/CI/badge.svg
  :target: https://github.com/eumiro/lumipallo/actions?query=workflow%3ACI

.. image:: https://img.shields.io/pypi/v/lumipallo.svg
  :target: https://pypi.org/project/lumipallo/

.. image:: https://img.shields.io/pypi/pyversions/lumipallo.svg
  :target: https://pypi.org/project/lumipallo/

.. image:: https://img.shields.io/github/license/eumiro/lumipallo
  :target: https://github.com/eumiro/lumipallo/


lumipallo: snowball effect in language learning
===============================================


**lumipallo** is the Finnish word for **snowball** (lumi = snow, pallo = ball).
Learning a foreign language is like a snowball. Start with a tiny amount
of snow and by rolling add one snowflake after another to get a big snowball.

How it works
------------

The smallest meaningful unit of a language is a sentence consisting of words.
If you see a sentence in a foreign language, you understand somewhere
between 0 and 100 percent of those words. If you understand nothing,
you'll be overwhelmed by all those new words. If you understand all
of them, you probably won't learn much. The best learning effect
is to get a sentence with one or two words that are new or almost new to you.
One unknown word in a familier context is easier to understand
than seeing it isolated in a dictionary.

So where to get the right sentences?

**lumipallo** uses the extensive sentences database from Tatoeba and keeps
track of the words you know. Each time it tries to find a sentence with
as few and as frequent words as possible and asks you about those
new words. It will provide you with a translation, but feel free to
check for the word in a dictionary, compare grammar tables, or just do
anything with the sentence. Your brain has to deal with stuff in order
to learn something new.


Prototype
---------

The project is in the alpha stage, features may appear/disappear quickly.

Install it:

.. code::

    pip install lumipallo

Start it with:

.. code::

    lumipallo

In this first prototype there is little you can do, but this is just
to show the principle and get in touch with people interested in trying
something new.

Your source language is English (:code:`eng`),
your target language is German (:code:`deu`).
It has a list of 13 somehow related sentences with 15 different words
(different forms of the same word are different words).
Each session starts from zero and there is no load/save functionality.

It shows you a sentence in your target language, then in the source language.
Then it asks for every new word in the sentence.
Answer :code:`y<RETURN>` if you know the word, :code:`n<ENTER>` otherwise.
It should show new sentences with minimal number of new words
and these words should be the most popular (within the list of course).
When you “learn“ all 15 words, it's over.

