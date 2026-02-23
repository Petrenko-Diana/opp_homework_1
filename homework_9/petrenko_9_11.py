import re

N, M = map(int, input().split())

dictionary = set()
for _ in range(N):
    dictionary.add(input().strip().lower())

used_words = set()

pattern = re.compile(r"[a-zA-Z]+")

for _ in range(M):
    line = input().lower()
    for w in pattern.findall(line):
        used_words.add(w)


if not used_words.issubset(dictionary):
    print("Some words from the text are unknown.")
    exit()


if not dictionary.issubset(used_words):
    print("The usage of the vocabulary is not perfect.")
    exit()
print("Everything is going to be OK.")
