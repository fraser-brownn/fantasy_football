### set environment variable PGPASSWORD to user password - psql will automatically read it in

### build a database called fantasy football first

psql postgres -h 127.0.0.1 -d fantasy_football -f create_elements_table.sql

poetry run python insert_dataframes.py
