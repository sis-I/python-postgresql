import psycopg2
from config import load_config


def get_parts(vendor_id):
  
  """
- create a new function called get_parts_by_vendors() from psql shell
after going directly to 'suppliers' database [$ psql -U postgres -d suppliers]

CREATE OR REPLACE FUNCTION get_parts_by_vendor(id INTEGER)
  RETURNS TABLE(part_id INTEGER, part_name VARCHAR) AS
$$
BEGIN
 RETURN QUERY

 SELECT parts.part_id, parts.part_name
 FROM parts
 INNER JOIN vendor_parts on vendor_parts.part_id = parts.part_id
 WHERE vendor_id = id;

END; $$

LANGUAGE plpgsql;

- Get pats provided by a vendor specified by the vendor_id
"""
  parts = []

  # read database configuration
  params = load_config()

  try:
    # connect to the postgerSQL db
    with psycopg2.connect(**params) as conn:
      with conn.cursor() as cur:
        # create a cursor object for execution
        # cur = conn.cursor()

        # pass the name of the function 
        # and the optionally pass values to the callproc()
        cur.callproc('get_parts_by_vendor', (vendor_id,))

        # process the result set
        row = cur.fetchone()
        while row is not None:
          parts.append(row)
          row = cur.fetchone()


  except (psycopg2.DatabaseError, Exception) as error:
    print(error)
  finally:
    return parts


if __name__=='__main__':
  parts = get_parts(5)
  print(parts)

