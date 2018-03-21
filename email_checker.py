valid_email = ['gmail.com', 'yahoo.co.in', 'iitkgp.ac.in']


def perms(word):
    '''All edits that are one edit away from `word`.'''
    letters = 'qwertyuiopasdfghjklzxcvbnm'

    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]

    return set(deletes + transposes + replaces + inserts)


class EmailPurifier:
    def __init__(self, emails, check=False):
        self.emails = emails
        if check is True:
            self.CheckEmail()

    def CheckEmail(self, checkTypo=False, echoText=False):
        self.correct = 0
        for email in self.emails:
            contents = email.split('@')
            if len(contents) == 2:

                if contents[1] in valid_email:
                    self.correct += 1
                    print('It is correct')

                elif checkTypo is True:
                    domain_data = contents[1].split('.')
                    for vemail in valid_email:
                        alters = perms(vemail.split('.', 1)[0])

                        if domain_data[0] in alters and echoText is True:
                                print("Wrong Domain : " + contents[1])
                                print("Did you mean : " + vemail)
                                break
        return self.correct
