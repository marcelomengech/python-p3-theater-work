from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Role, Audition

# Create database connection
engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def seed_data(session):
    # Create multiple roles
    roles = [
        Role(character_name="Hamlet"),
        Role(character_name="Ophelia"),
        Role(character_name="Macbeth"),
        Role(character_name="Lady Macbeth")
    ]
    session.add_all(roles)
    session.commit()

    # Create auditions for each role
    auditions = [
        Audition(actor="John Smith", location="Stage 1", phone=1234567890, role_id=roles[0].id),
        Audition(actor="Jane Doe", location="Stage 2", phone=2345678901, role_id=roles[0].id),
        Audition(actor="Alice Cooper", location="Stage 3", phone=3456789012, role_id=roles[1].id),
        Audition(actor="Bob Johnson", location="Stage 4", phone=4567890123, role_id=roles[2].id),
        Audition(actor="Eve White", location="Stage 5", phone=5678901234, role_id=roles[2].id),
        Audition(actor="Sophia Green", location="Stage 6", phone=6789012345, role_id=roles[3].id)
    ]
    session.add_all(auditions)
    session.commit()

    # Hire actors for roles (callback to mark as hired)
    auditions[0].call_back()  # Hire John Smith for Hamlet
    auditions[1].call_back()  # Hire Jane Doe for Hamlet
    auditions[3].call_back()  # Hire Bob Johnson for Macbeth
    auditions[4].call_back()  # Hire Eve White for Macbeth
    auditions[5].call_back()  # Hire Sophia Green for Lady Macbeth
    session.commit()

    # Print out details for each role
    for role in roles:
        print(f"Role: {role.character_name}")
        print(f"Actors: {role.actors()}")
        print(f"Locations: {role.locations()}")

        # Get the lead and display more detailed information
        lead = role.lead()
        if lead:
            print(f"Lead: {lead.actor} (Phone: {lead.phone}, Location: {lead.location})")
        else:
            print("Lead: No actor has been hired for this role")

        # Get the understudy and display more detailed information
        understudy = role.understudy()
        if understudy:
            print(f"Understudy: {understudy.actor} (Phone: {understudy.phone}, Location: {understudy.location})")
        else:
            print("Understudy: No actor has been hired for understudy for this role")

if __name__ == "__main__":
    seed_data(session)
