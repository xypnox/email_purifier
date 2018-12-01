# Email Purifier

A KISS(Keep It Stupid Simple) email validator for csv files

To install the script locally use:

To install the program run

```
$ pip install todx
```

If you are using Ubuntu run this instead:

```
$ pip3 install todx
```

If the installation of pandas fails due to user permissions, you can either use sudo or install using the `--user` parameter.


To validate and store the emails in a csv file run:

```
epurifier <input file> <output file>
```

And tackle with the invalid emails through keyboard.


> Note that both input and Output files should be in csv format

If you clone the repo you can extend the code, to install the cloned repo as a package, run:

```
pip install -e .
```

Now, editing the files in the local folder will reflect systemwide installation of epurifier so you can use the epurifier with your modified parameters.

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
