import psycopg2
from config import load_config


def insert_many_parts(part_list):
  """ Insert parts in the parts table"""

  sql = """INSERT INTO parts(part_name) VALUES(%s) RETURNING *;"""

  config = load_config()

  try:
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:

        # execute INSERT statement
        cur.executemany(sql, part_list)


      conn.commit()

  except (psycopg2.DatabaseError, Exception) as error:
    print(error)



def insert_many_vendor_parts(vendor_part_list):
  """Insert vendor parts relation in vendor_parts table """

  sql = """INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s);"""

  config = load_config()

  try:
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:
        # execute INSERT statement
        for vendor_part in vendor_part_list:
          print(vendor_part)
          cur.execute(sql, (vendor_part[0], vendor_part[1]))
      
      conn.commit()

  except (psycopg2.DatabaseError, Exception) as error:
    print(error)


if __name__== '__main__':
  # insert_many_parts(
  #   [
  #     ('Antenna',),
  #     ('Home Button',),
  #     ('LTE Modem',),
  #     ('SIM Tray',),
  #     ('Speaker',),
  #     ('Vibrator',),
  #   ]
  # )

  insert_many_vendor_parts(
    [
      (5, 1),
      (10, 1),
      (9, 2),
      (12, 2),
      (9, 3),
      (7, 3),
      (6, 4),
      (11, 5),
      (8, 6),
    ]
  )