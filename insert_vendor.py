import psycopg2
from config import load_config

def insert_vendor(vendor_name):
  """ Insert a new vendor into the vendors table. """

  sql = """INSERT INTO vendors(vendor_name)
            VALUES(%s) RETURNING vendor_id;"""
  vendor_id = None
  config = load_config()

  try:
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:
        # excute the INSERT statement
        cur.execute(sql, (vendor_name,))

        # get the generated id back
        rows = cur.fetchone()
        print('rows', rows)
        print('cur', cur)
        if rows:
          vendor_id = rows[0]

        # commit the changes to the database
        print('conn', conn)
      conn.commit()

  except (psycopg2.DatabaseError, Exception) as error:
    print(error)
  finally:
    return vendor_id


def insert_many_vendors(vendor_list):
  """ Insert many vendors inot the vendors table """

  sql = """INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING *;"""

  config = load_config()

  try:
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:
        # execute the INSERT statement
        cur.executemany(sql, vendor_list)

      # commit the changes to the db
      conn.commit()
    
  except (psycopg2.DatabaseError, Exception) as error:
    print(error)

if __name__ == '__main__':
  i = insert_vendor("3M Co.")
  print(i)

  insert_many_vendors([
    ('AKM Semiconductor Inc.',),
    ('Asahi Glass Co Ltd.',),
    ('Daikin Industries Ltd.',),
    ('Foster Electric Co Ltd.',),
    ('Dynacast Electric Co. Ltd.',),
    ('Murata Manufacturing Co. Ltd.',),
  ])
  

