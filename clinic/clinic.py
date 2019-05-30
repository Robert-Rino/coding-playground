from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

engine = create_engine("sqlite:///clinic.db")
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Appointment(Base):
    __tablename__ = 'appointment'
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patiant_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Integer)

    doctor = relationship('Doctor')
    user = relationship('User')


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    s = Session()
    u1 = User(name='user1', email='user1@gmail.com')
    u2 = User(name='user2', email='user2@gmail.com')
    d1 = Doctor(name='doctor1')
    d2 = Doctor(name='doctor2')
    s.add_all([u1, u2, d1, d2])
    s.commit()

    a1 = Appointment(doctor_id=1, patiant_id=2, date=12345)
    s.add(a1)
    s.commit()


