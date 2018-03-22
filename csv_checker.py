import pandas as pd
import email_checker as ec
import sys


def main(argv):

    inputfile = argv[0]
    outputfile = argv[1]

    print('Input file is ', inputfile)

    data_df = pd.read_csv(inputfile)

    for column in data_df.columns:
        if column == 'Email':
            colName = 'Email'
        elif column == 'email':
            colName = 'email'

    emails = data_df[colName]
    emil = ec.EmailPurifier(list(emails))
    emil.CheckEmails(checkTypo=True)
    emil.CorrectWrongEmails()
    data_df[colName] = emil.emails

    data_df.to_csv(outputfile, index=False)
    print('Emails Formated ! Output file is : ', outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
