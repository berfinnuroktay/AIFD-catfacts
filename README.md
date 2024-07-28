# Documentation

## Required Packages

If you have not already installed the necessary packages, please install them by running the following commands:

```bash
pip install requests
pip install sqlalchemy
```

## Database Initialization

The database is already initialized with the name `cat_facts.db`. If you want to start the process from the beginning, follow these steps:

1. Delete `cat_facts.db` (either by running `rm cat_facts.db` or moving it to the trash).
2. Run the command `python init_db.py` to initialize the database.
3. Run the command `python cat_facts_manager.py` to display the cat facts retrieved from the URL.

Enjoy your cat facts!

