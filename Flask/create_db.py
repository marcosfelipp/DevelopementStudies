from market import db
from market.models import Item, User

db.drop_all()
db.create_all()

u1 = User(username='Marcos', password_hash='27927972', email_address='marcos@gmail.com')
db.session.add(u1)
db.session.commit()

item1 = Item(name="Iphone 10 ", price=500, barcode='8989289282982', description='desc')
item1.owner = User.query.filter_by(username='Marcos').first().id
item2 = Item(name="Iphone 7 ", price=300, barcode='8985285282981', description='desc1')
item2.owner = User.query.filter_by(username='Marcos').first().id
db.session.add(item1)
db.session.add(item2)
db.session.commit()

print(User.query.filter_by(username='Marcos').first())
print(Item.query.all())
