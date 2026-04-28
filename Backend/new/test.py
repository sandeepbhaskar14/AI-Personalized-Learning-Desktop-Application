from main import app, db
from models import User, Result, Prompt


# delete a user
# with app.app_context():
#     user = User.query.get(1)
#     if user:
#         db.session.delete(user)
#         db.session.commit()
        
#         print('User deleted')
        
# delete a table
with app.app_context():
    Prompt.__table__.drop(db.engine)
    print("results table deleted")