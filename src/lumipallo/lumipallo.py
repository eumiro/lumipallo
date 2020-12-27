import re
from collections import Counter
from pathlib import Path


class Snow:
    def __init__(self, target_lang):
        self.target_lang = target_lang
        self.sentences = {}
        self.words = {}

    def load(self, *paths):
        pairs = {}
        sources = {}
        for path in paths:
            with path.open() as f:
                for line in f:
                    fields = line.split(maxsplit=2)
                    if len(fields) == 2:
                        pairs.setdefault(int(fields[0]), set()).add(
                            int(fields[1])
                        )
                        pairs.setdefault(int(fields[1]), set()).add(
                            int(fields[0])
                        )
                    elif len(fields) == 3:
                        s_id, s_lang, s_body = fields
                        if s_lang == self.target_lang:
                            self.sentences[int(s_id)] = {
                                "body": s_body.strip()
                            }
                        else:
                            sources[int(s_id)] = s_body.strip()
                    else:
                        pass
        for s_id, s_obj in self.sentences.items():
            s_obj["words"] = {
                word.casefold() for word in re.findall(r"\w+", s_obj["body"])
            }
            s_obj["translations"] = {
                sources[src_id] for src_id in pairs.get(s_id, [])
            }
            for word in s_obj["words"]:
                self.words.setdefault(word, set()).add(s_id)
        return len(self.sentences)

    def most_common_words(self, limit=None):
        return Counter(
            word
            for s_obj in self.sentences.values()
            for word in s_obj["words"]
        ).most_common(limit)


def learn():
    target = "deu"
    print(f"Learning language: {target!r}")
    snow = Snow(target)
    snow.load(*list(Path(__file__).with_name("testdata").glob("01_*.txt")))

    known_words = set()
    popularity = {
        word: i for i, (word, _) in enumerate(snow.most_common_words())
    }

    while True:
        print("============================================")
        print(f"You know {len(known_words)} words out of {len(snow.words)}.")
        if known_words == set(snow.words):
            print("You have learned everything.")
            break

        def difficulty(s_id):
            new_words = snow.sentences[s_id]["words"] - known_words
            return (
                (len(new_words), sum(popularity[word] for word in new_words))
                if new_words
                else (999, 999999)
            )

        s_obj = snow.sentences[min(snow.sentences, key=difficulty)]

        print(s_obj["body"])
        print("\n".join(s_obj["translations"]))
        for word in sorted(s_obj["words"] - known_words, key=popularity.get):
            res = input(f"Do you understand {word!r}? (y/n) ")
            if res.lower().startswith("y"):
                known_words.add(word)


if __name__ == "__main__":
    learn()
