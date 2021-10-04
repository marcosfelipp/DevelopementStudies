from market import db
from market import Item

db.create_all()
item1 = Item(name="Iphone 10 ", price=500, barcode='8989289282982', description='desc')
item2 = Item(name="Iphone 7 ", price=300, barcode='8985285282981', description='desc1')
db.session.add(item1)
db.session.add(item2)
db.session.commit()

print(Item.query.all())