from sqlalchemy import create_engine, Integer, Float, String, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship, sessionmaker
from datetime import datetime, timezone

Base = declarative_base()

engine = create_engine('sqlite:///clinic.db')

Session = sessionmaker(bind=engine)
session = Session()



class Owners(Base):
    __tablename__ = 'owners'

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(360), unique=True)

    #relationship to pets

class Pets(Base):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    species: Mapped[str] = mapped_column(String(200))
    breed: Mapped[str] = mapped_column(String(200))
    age: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'))

    #relationship to owner
    #relationship to vets
    #relationship to appointments (if you do the asso. model)

class Veterinarians(Base):
    __tablename__ = 'veterinarians'

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    specialization: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(360), unique=True)

    #relationship to pets
    #relationship tp appointments
    

#Appointment junct table
class Appointments(Base):
    __tablename__ = 'appointments'

    id: Mapped[int] = mapped_column(primary_key = True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'))
    veterinarian_id: Mapped[int] = mapped_column(Integer, ForeignKey('veterinarians.id'))
    appointment_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    notes: Mapped[str] = mapped_column(String(400))
    status: Mapped[str] = mapped_column(String(200)) #Scheduled, Completed, Cancelled

    #Relationship to pet
    #Relationship to vet

