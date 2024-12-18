import psycopg2
from config import load_config


def add_parts(part_name, vendor_list):

  # statement for inserting a new row into parts table
  insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"

  # statement for inserting a new row into vendor_parts table
  assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s);"

  conn = None

  config = load_config()

  try:
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:
        # insert a new part, 
        cur.execute(insert_part, (part_name,))

        # get the part id
        row = cur.fetchone()
        if row:
          part_id = row[0]
        else:
          raise Exception('Could not get the part id!')
        
        # assign parts provided by vendors
        for vendor_id in vendor_list:
          cur.execute(assign_vendor, (vendor_id, part_id))

        # commit the transaction
        conn.commit() # permanently apply all changes to the database
  except (psycopg2.DatabaseError, Exception) as error:
    if conn:
      conn.rollback() # Discard if any changes
    print(error)

if __name__== '__main__':
  add_parts('SIM Tray', (5, 8))