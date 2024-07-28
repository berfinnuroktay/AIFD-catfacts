import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from init_db import CatFact  # Import the CatFact model from init_db.py
from typing import List, Dict


def fetch_cat_facts() -> List[Dict]:
    """Fetch cat facts from the API."""
    url = "https://cat-fact.herokuapp.com/facts"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_db_session():
    """Create and return a database session."""
    engine = create_engine('sqlite:///cat_facts.db')
    Session = sessionmaker(bind=engine)
    return Session()


def insert_cat_facts(session, facts: List[Dict]) -> None:
    """Insert cat facts into the database."""
    for fact in facts:
        cat_fact = CatFact(
            id=fact['_id'],
            text=fact['text'],
            user=fact['user'],
            created_at=fact['createdAt'],
            updated_at=fact['updatedAt']
        )
        session.merge(cat_fact)  # merge will insert or update
    session.commit()


def display_cat_facts(session) -> None:
    """Display cat facts from the database."""
    facts = session.query(CatFact).all()

    print("Cat Facts from the Database:")
    for fact in facts:
        print(f"ID: {fact.id}")
        print(f"Fact: {fact.text}")
        print(f"User: {fact.user}")
        print(f"Created At: {fact.created_at}")
        print(f"Updated At: {fact.updated_at}")
        print("-" * 50)


def main():
    try:
        # Fetch cat facts from the API
        cat_facts = fetch_cat_facts()

        # Get database session
        session = get_db_session()

        # Insert cat facts into the database
        insert_cat_facts(session, cat_facts)

        # Display cat facts from the database
        display_cat_facts(session)

    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if session:
            session.close()


if __name__ == "__main__":
    main()