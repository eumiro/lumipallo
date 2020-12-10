# lumipallo
Snowball effect in language learning

## Development

The project is in the alpha stage, features may appear/disappear quickly.

Start it with `python src/lumipallo/lumipallo.py`

Your source language is English (`eng`), your target language is German (`deu`). It has a list of 13 somehow related sentences with 15 different words (different forms of the same word are different words). Each session starts from zero and there is no load/save functionality.

It shows you a sentence in your target language, then in the source language. Then it asks for every new word in the sentence. Answer `y<RETURN>` if you know the word, `n<ENTER>` otherwise. It should show new sentences with minimal number of new words and these words should be the most popular (within the list of course). When you “learn“ all 15 words, it's over.
