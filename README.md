# Open Data Project
This project aims to visualize the various cancellations of public transport in Switzerland
throughout the year 2022 and its seasons. The project's content is mostly in German.

This is a SvelteKit app so refer to the SvelteKit documentation for additional help with running it.
In general, you run it like any other Vite app:
```sh
npm install
npm run dev
```

In order for the app to correctly work you have to have the data and build the database beforehand.
There is a Python script (`setup_db.py`) to help you with that. The database schema is also given
in `setup_db.sql`.
Once you have the database file (called `open_data.db` and placed in the `./data` directory) everything in the app should correctly display.

Alternatively, there is already a database in the repository.
