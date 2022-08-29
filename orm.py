from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()


class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer, nullable=True)

    def __init__(self, name, number):
       self.name = name
       self.number = number

    def __str__(self):
        return f'{self.id}) {self.name}: {self.number}'


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

region = Region('Екатеринбург', 65)


session.add(region)

region = Region('Воронеж', 36)

session.add(region)

session.commit()

region.name = 'Тула'

session.commit()

session.delete(region)

session.commit()

for i in range(10):
    region = Region(f'region {i}', i)
    session.add(region)

session.commit()


regions_query = session.query(Region)

print(type(regions_query))

for region in regions_query:
    print(region.name)

regions = session.query(Region).all()

print(type(regions))

for region in regions_query:
    print(region.name)


regions = session.query(Region).filter(Region.name == 'Москва' and Region.id > 14).all()

print(type(regions))
print(regions)

for region in regions:
    print(region)
    print(region.id)
    print(region.name)
    print(region.number)