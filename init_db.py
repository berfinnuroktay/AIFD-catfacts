from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class CatFact(Base):
    __tablename__ = 'cat_facts'

    id = Column(String, primary_key=True)
    text = Column(String, nullable=False)
    user = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

    def __repr__(self):
        return f"<CatFact(id={self.id}, text={self.text[:30]}...)>"

def init_db():
    engine = create_engine('sqlite:///cat_facts.db')
    Base.metadata.create_all(engine)
    print("Database initialized.")

if __name__ == "__main__":
    init_db()