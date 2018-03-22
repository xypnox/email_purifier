from query_yes_or_no import query_yes_no as qyn

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
    def __init__(self, emails, valid_emails=valid_email):
        '''
        Initialises The Instance with emails and empty wrong emails list
        Valid Email domains are stored in valid
        '''
        self.emails = emails
        self.wrong_emails = []
        # self.corrected_emails = []
        self.valid = valid_emails
        self.correct = 0
        # self.CheckEmails(fillWrong=True)

    def CheckEmails(self, checkTypo=False, fillWrong=True):
        '''Checks Emails in List Wether they are Correct or not'''
        self.correct = 0
        self.wrong_emails = []
        for email in self.emails:
            if self.CheckEmail(email, checkTypo):
                self.correct += 1
            else:
                self.wrong_emails.append(email)
        return self.correct

    def CheckEmail(self, email, checkTypo=False):
        '''Checks a Single email if it is correct'''
        contents = email.split('@')
        if len(contents) == 2:
            if contents[1] in self.valid:
                return True
        return False

    def CorrectWrongEmails(self, askInput=True):
        '''Corrects Emails in wrong_emails'''
        # self.corrected_emails = []
        for email in self.wrong_emails:
            corrected_email = self.CorrectEmail(email)
            self.emails[self.emails.index(email)] = corrected_email

        self.wrong_emails = []

    def CorrectEmail(self, email):
        '''Returns a Corrected email USER INPUT REQUIRED'''
        print("Wrong Email : "+email)
        contents = email.split('@')
        if len(contents) == 2:
            domain_data = contents[1].split('.')
            for vemail in valid_email:
                alters = perms(vemail.split('.', 1)[0])

                if domain_data[0] in alters and qyn("Did you mean : " + contents[0] + '@' + vemail) is True:
                        return contents[0] + '@' + vemail
                else:
                    corrected = input('Enter Corrected Email : ')
                    while self.CheckEmail(corrected) is False:
                        corrected = input('PLEASE Enter "Corrected" Email : ')
                    return corrected
        else:
            print('Looks like you missed/overused `@`')
            corrected = input('Enter Corrected Email : ')
            while self.CheckEmail(corrected) is False:
                corrected = input('PLEASE Enter "Corrected" Email : ')
            return corrected

    def stats(self):
        print('___STATS___')
        print('Emails = ', self.emails)
        print('Correct = ', self.correct)
        print('Wrong Emails = ', self.wrong_emails)
        # print('Corrected Emails = ', self.corrected_emails)
        print('Valid Domains = ', self.valid)
        print('___END___')
