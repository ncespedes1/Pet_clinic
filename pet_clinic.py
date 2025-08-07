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

    pets: Mapped[list['Pets']] = relationship('Pets', back_populates='owner')

class Pets(Base):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    species: Mapped[str] = mapped_column(String(200), nullable=False) #Dog, Cat, Bird, etc.
    breed: Mapped[str] = mapped_column(String(200))
    age: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'))

    owner: Mapped['Owners'] = relationship('Owners', back_populates='pets')
    #relationship to vets
    appointments: Mapped[list['Appointments']] = relationship('Appointments', back_populates='pet')

class Veterinarians(Base):
    __tablename__ = 'veterinarians'

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    specialization: Mapped[str] = mapped_column(String(200)) #General, Surgery, Dermatology
    email: Mapped[str] = mapped_column(String(360), unique=True)

    #relationship to pets
    appointments: Mapped[list['Appointments']] = relationship('Appointments', back_populates='veterinarian')
    

class Appointments(Base):
    __tablename__ = 'appointments'

    id: Mapped[int] = mapped_column(primary_key = True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'))
    veterinarian_id: Mapped[int] = mapped_column(Integer, ForeignKey('veterinarians.id'))
    appointment_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    notes: Mapped[str] = mapped_column(String(400))
    status: Mapped[str] = mapped_column(String(200)) #Scheduled, Completed, Cancelled

    pet: Mapped['Pets'] = relationship('Pets', back_populates='appointments')
    veterinarian: Mapped['Veterinarians'] = relationship('Veterinarians', back_populates='appointments')


Base.metadata.create_all(bind=engine)


#============== Adding Data =================


#Creating at least 3 new_owners and adding them to the db
new_owners = [
    Owners(name = "Shaggy Rogers", phone = "555-123-1969", email= "norvillerogers@mysteryinc.com"),
    Owners(name = "Charlie Brown", phone = "555-111-1950", email= "peanuts@email.com"),
    Owners(name = "Madame Adelaide Bonfamille", phone = "555-444-1910", email= "arisocats@email.com"),
    Owners(name = "Harry Potter", phone = "555-777-1997", email= "yerawizard@email.com"),
    Owners(name = "John Arbuckle", phone = "555-222-1978", email= "lasagna@email.com")
]
# session.add_all(new_owners)
# session.commit()


new_pets = [
    Pets(name = "Snoopy", species = "Dog", breed= "Beagle", age=5, owner_id=2),
    Pets(name = "Scooby-Doo", species = "Dog", breed= "Great Dane", age=9, owner_id=1),
    Pets(name = "Hedwig", species = "Owl", breed= "Snowy Owl", age=7, owner_id=4),
    Pets(name = "Garfield", species = "Cat", breed= "Domestic Shorthair", age=10, owner_id=5),
    Pets(name = "Odie", species = "Dog", breed= "Mixed", age=4, owner_id=5),
    Pets(name = "Duchess", species = "Cat", breed= "Turkish Angora", age=9, owner_id=3),
    Pets(name = "Marie", species = "Cat", breed= "Turkish Angora", age=0, owner_id=3),
    Pets(name = "Berlioz", species = "Cat", breed= "Turkish Angora", age=0, owner_id=3),
    Pets(name = "Toulouse", species = "Cat", breed= "Turkish Angora", age=0, owner_id=3),
    Pets(name = "Thomas O'Malley", species = "Cat", breed= "Domestic Shorthair", age=7, owner_id=3)
]

# session.add_all(new_pets)
# session.commit()


#Creating a 2 new_vets and adding them to the db
new_vets = [
    Veterinarians(name = "John Dolittle", specialization = "General", email= "talkinganimals@email.com"),
    Veterinarians(name = "James Herriot", specialization = "Surgery", email= "allpetsbigandsmall@email.com")
]

# session.add_all(new_vets)
# session.commit()

new_appts = [
    Appointments(pet_id = 6, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 10, 30, 0), notes = "Well behaved, model cat. No previous problems.", status = "Scheduled"),
    Appointments(pet_id = 7, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 10, 45, 0), notes = "Checkup, no known problems. Warning: Do not mess up her bow.", status = "Scheduled"),
    Appointments(pet_id = 8, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 11, 15, 0), notes = "To avoid distractions, keep away from his brother. Likes to bite", status = "Scheduled"),
    Appointments(pet_id = 9, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 11, 30, 0), notes = "To avoid distractions, keep away from his brother. Likes to bite", status = "Scheduled"),
    Appointments(pet_id = 10, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 11, 45, 0), notes = "Adopted alleyway cat. Needs thorough checkup. Seems to be unfamiliar with vets.", status = "Scheduled"),
    Appointments(pet_id = 1, veterinarian_id = 1, appointment_date = datetime(2025, 9, 15, 10, 45, 0), notes = "Address the dog directly, not the owner", status = "Scheduled"),
    Appointments(pet_id = 2, veterinarian_id = 2, appointment_date = datetime(2025, 9, 25, 11, 30, 0), notes = "Clear the office, he will eat everything", status = "Cancelled"),
    Appointments(pet_id = 4, veterinarian_id = 2, appointment_date = datetime(2025, 7, 30, 10, 30, 0), notes = "Low motivation to exercise. Has history of eating too much lasagna. Check blood report.", status = "Completed"),
    Appointments(pet_id = 5, veterinarian_id = 2, appointment_date = datetime(2025, 7, 30, 11, 30, 0), notes = "Struggles to keep tongue in mouth. Check for dryness. Very sweet dog.", status = "Completed"),
    Appointments(pet_id = 3, veterinarian_id = 1, appointment_date = datetime(2025, 7, 15, 10, 30, 0), notes = "Well behaved. Has shown wing fatigue before.", status = "Completed")
]
# session.add_all(new_appts)
# session.commit()

# print("hello testing")


