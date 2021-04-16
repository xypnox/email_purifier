import os
class Config:
	UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
	SECRET_KEY = 'choose any valid secret key'.encode('utf8')

