from application import app,db
from application.models import prizesgiven
if __name__ == '__main__':
	app.run(port=5000, host='0.0.0.0')