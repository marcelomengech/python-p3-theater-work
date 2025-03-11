from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    
    # Relationship: one role can have many auditions
    auditions = relationship('Audition', back_populates='role')
    
    def __repr__(self):
        return f"<Role(id={self.id}, character_name='{self.character_name}')>"

    def actors(self):
        # Returns list of actor names for this role
        return [audition.actor for audition in self.auditions]
    
    def locations(self):
        # Returns list of locations from auditions for this role
        return [audition.location for audition in self.auditions]
    
    def lead(self):
        # Find the first hired actor
        hired_auditions = [a for a in self.auditions if a.hired]
        if hired_auditions:
            return hired_auditions[0]
        return None
    
    def understudy(self):
        # Find the second hired actor
        hired_auditions = [a for a in self.auditions if a.hired]
        if len(hired_auditions) >= 2:
            return hired_auditions[1]
        return None


class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    
    # Relationship: each audition belongs to one role
    role = relationship('Role', back_populates='auditions')

    def __repr__(self):
        return f"<Audition(id={self.id}, actor='{self.actor}', location='{self.location}', hired={self.hired})>"

    def call_back(self):
        # Change hired status to True
        self.hired = True
