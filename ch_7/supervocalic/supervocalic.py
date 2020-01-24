vowels = "aeiou"


def get_sv(file):
    return {
        word.strip()
        for word in open(file)
        if set(vowels).issubset(set(word.strip().lower()))
    }


print(get_sv("words.txt"))
