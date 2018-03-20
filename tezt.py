def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return deletes + transposes + replaces + inserts


if 'gamil' in edits1('gmail'):
    print("Hell Yeah")

print('gmail.co.in'.split('.', 1)[0])
