import email_checker as ec

sample_emails = ['xypnox@gmail.com', 'xypnox@iitkgp.ac.in', 'xypnoxgmail.com', 'yahoo@gamil.com', 'vadoo@gradoo']

print(sample_emails[0][len(sample_emails[0])-len('gmail.com'):])

kr = ec.EmailPurifier([])
kr.CorrectEmail('xypnoxgmail.com')
