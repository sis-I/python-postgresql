import psycopg2
from config import load_config


def update_vendor(vendor_id, vendor_name):
  """ Update vendor name based on the vendor id"""

  update_row_count = 0

  sql = """ UPDATE vendors SET vendor_name = %s
              WHERE vendor_id = %s;"""
  
  config = load_config()

  try:
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:
        # execute the UPDATE statement
        cur.execute(sql, (vendor_name, vendor_id))
        update_row_count = cur.rowcount

      # commit the changes to the db
      conn.commit()

  except (psycopg2.DatabaseError, Exception) as error:
    print(error)
  
  finally:
    return update_row_count


if __name__ == '__main__':
  u_row = update_vendor(5, '3M Corp')
  print(u_row)
