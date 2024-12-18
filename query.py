import psycopg2
from config import load_config


def get_vendors():
  """ Retrieve data from the vendors table"""

  config = load_config()

  try:
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:
        cur.execute('SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name;')
        print('The number of parts: ', cur.rowcount)
        
        # fetchs the next row in the result set, it returns single row data
        '''row = cur.fetchone()

        while row is not None:
          print(row)

          row = cur.fetchone() # return None when no row available
        '''
        # Using fetchall() method
        rows = cur.fetchall() # returns all rows, or empty list
        for row in rows:
          print('using fetchall: ', row)

  except (psycopg2.DatabaseError, Exception) as error:
    print(error)


if __name__== '__main__':
  get_vendors()