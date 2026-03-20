from main import app, db
from models import User

with app.app_context():
    user = User.query.get(1)
    if user:
        db.session.delete(user)
        db.session.commit()
        
        print('User deleted')