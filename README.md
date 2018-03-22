# Email Purifier

A KISS(Keep It Stupid Simple) email validator for csv files

To validate and store the emails in a csv file run:

```bash
python csv_checker.py <input file> <output file>
```

And tackle with the invalid emails through keyboard.


> Note that both input and Output files should be in csv format


Also, to extend the valid emails you can either pass them when you create the EmailPurifier class as
```python
import email_checker as ec
emails_to_check = [
    # Your emails
]
additional_valid_emails = [
    # add only domain names such as 'google.com'
]
emil = ec.EmailPurifier(emails_to_check, additional_valid_emails)
```

By default it adds the passed additional emails to a list of top 10 valid emails present in `valid_emails.py`
If for some reason you want to only use the additional emails and don't want emails from `valid_emails` you can pass the argument `onlyAdditional=True` to override the behavior.
