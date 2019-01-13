import pandas as pd
from . import email_checker as ec
import sys


def main():
    argv=sys.argv[1:]
    if len(argv)<2:
    	print('Improper format for arguments, correct format is :\nepurifier <input file> <output file> <optional_column_name>\nExiting...')
    	return

    inputfile = argv[0]
    outputfile = argv[1]
    if(len(argv)==3):
        column_header = (argv[2]).lower()
    else:
        column_header = 'email'

    #print(column_header)
    
    print('Input file is ', inputfile)

    data_df = pd.read_csv(inputfile)

    colName = None

    for column in data_df.columns:
    #    print(column)
        if column.lower() == column_header:
            colName = column

    if colName == None:
        print('The specified column name ' + column_header+ ' was not found in the input file '+inputfile+'!\nExiting...\n')
        return

    x = input('Do you want to remove duplicate entries? Enter 1 for yes, 2 for no : ')
    emails = data_df[colName]
    emil = ec.EmailPurifier(list(emails))
    emil.CheckEmails(checkTypo=True)
    emil.CorrectWrongEmails()
    data_df[colName] = emil.emails

    if x==1:
    	data_df.drop_duplicates(subset=None, keep='first', inplace=True)


    data_df.to_csv(outputfile, index=False)
    print('Emails Formated ! Output file is : ', outputfile)


if __name__ == "__main__":
    main()
