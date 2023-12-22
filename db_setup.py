import os, sqlite3
import pandas as pd

# create respective sql files for each table
# data directory
data_dir = os.path.join('.', 'data')


def create_sql(directory):
    for file in os.listdir(directory):
        file = file.split('.')[0]
        if not os.path.exists(f'models/schemas/{file}.sql'):
            with open(f'models/schemas/{file}.sql', 'w') as f:
                f.write(f'-- {file} table\n')
            print(f'{file}.sql created!')
        else:
            print(f'{file}.sql already exists!')


# create_sql(data_dir)

def write_to_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    filenames = list(map(lambda x: x.split('.')[0], os.listdir(data_dir)))
    for file in filenames:
        with open(f'models/schemas/{file}.sql', 'r') as f:
            print(f'--CREATE QUERY FOR {file} TABLE--')
            create_query = f.read()
            print(create_query)
            cur.execute(f"DROP TABLE IF EXISTS {file}")
            cur.execute(create_query)
        df = pd.read_csv(f'{data_dir}/{file}.csv')
        df.to_sql(file, conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()
    print('Database created!')

write_to_db()
