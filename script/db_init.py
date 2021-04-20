from project.lib.db_pool import DbConnectionPool

connectionPool = DbConnectionPool(database='../db/main.db', capacity=1)
with connectionPool.get_resource() as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE users (first_name text, last_name text, phone text)')
    cursor.execute("INSERT INTO users VALUES ('Ivan', 'Ivanov', '+79111111111')")
    cursor.execute("INSERT INTO users VALUES ('John', 'Doe', '+449111111111')")
    cursor.execute("INSERT INTO users VALUES ('Johann', 'Schmidt', '+499111111111')")
    cursor.execute("INSERT INTO users VALUES ('Yar', 'Selezen', '+79780570183')")
    connection.commit()
    cursor.close()
