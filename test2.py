import email_checker as ec

sample_emails = ['xypnox@gmail.com', 'xypnox@iitkgp.ac.in', 'xypnoxgmail.com', 'yahoo@gamil.com', 'vadoo@gradoo']

emil = ec.EmailPurifier(sample_emails)
emil.CheckEmail(True)
