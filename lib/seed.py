from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Role, Audition

# Create database connection
engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a role
new_role = Role(character_name="Hamlet")
session.add(new_role)
session.commit()

# Create auditions for the role
audition1 = Audition(
    actor="John Smith", 
    location="Stage 1",
    phone=1234567890,
    role_id=new_role.id
)
audition2 = Audition(
    actor="Jane Doe", 
    location="Stage 2",
    phone=2345678901,
    role_id=new_role.id
)
session.add_all([audition1, audition2])
session.commit()

# Test the call_back method
audition1.call_back()
session.commit()

# Improved display of role information
print(f"Role: {new_role.character_name}")
print(f"Actors: {new_role.actors()}")
print(f"Locations: {new_role.locations()}")

# Get the lead and display more detailed information
lead = new_role.lead()
if lead:
    print(f"Lead: {lead.actor} (Phone: {lead.phone}, Location: {lead.location})")
else:
    print("Lead: No actor has been hired for this role")

# Get the understudy and display more detailed information
understudy = new_role.understudy()
if understudy:
    print(f"Understudy: {understudy.actor} (Phone: {understudy.phone}, Location: {understudy.location})")
else:
    print("Understudy: no actor has been hired for understudy for this role")

# Let's hire a second actor
audition2.call_back()
session.commit()

# Display updated understudy information
understudy = new_role.understudy()
if understudy:
    print(f"After hiring second actor, understudy: {understudy.actor} (Phone: {understudy.phone}, Location: {understudy.location})")
else:
    print("After hiring second actor, understudy: No actor has been hired for understudy for this role")