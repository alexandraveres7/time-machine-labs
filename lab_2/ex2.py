def letter_count(sentence):
    s = sentence.lower()
    d = {}
    for c in s:
        cnt = s.count(c)
        d[c] = cnt
    print(str(d))


letter_count('Python gives you superpowers.')
