def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    print('splits = ', splits)
    deletes = [L + R[1:] for L, R in splits if R]
    print('deletes = ', deletes)
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    print('transposes = ', transposes)
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    print('replaces = ', replaces)
    inserts = [L + c + R for L, R in splits for c in letters]
    print('inserts = ', inserts)
    print(deletes + transposes + replaces + inserts)
    print(len(set(deletes + transposes + replaces + inserts)))
    return deletes + transposes + replaces + inserts


edits1('gmail')

print('gmail.co.in'.split('.', 1)[0])
