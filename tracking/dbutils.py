import traceback


from django.db import connections,connection,transaction

def table_exists(cur,schema,table_name,log=False):
    cur.execute("SELECT count(*) FROM pg_catalog.pg_class a join pg_catalog.pg_namespace b on a.relnamespace = b.oid WHERE b.nspname='{}' and a.relname='{}' and a.relkind='r'".format(schema,table_name))
    row = cur.fetchone()
    exists =  False if int(row[0]) == 0 else True
    if log:
        print("The table({}.{}) {} exist".format(schema,table_name,"does" if exists else "doesn't"))
    return exists

def create_table(conn,schema,table_name,create_sql,log=False):
    with conn.cursor() as cur:
        if not table_exists(cur,schema,table_name,log=log):
            #table doesn't exist, create it.
            try:
                cur.execute(create_sql)
                if log :
                    print("Succeed to create the table({}.{}) with sql({})".format(schema,table_name,create_sql))
            except:
                print("Failed to create the table({}.{}) with sql({}).{}".format(schema,table_name,create_sql,traceback.format_exc()))
                if not table_exists(cur,schema,table_name):
                    raise

def execute(conn,sql,log=False):
    with conn.cursor() as cur:
        cur.execute(sql )
        rows = cur.rowcount
        if log:
            print("{1} rows are affected by executing the sql ({0}).".format(sql,rows))
        return rows

def executeDDL(conn,sql,log=False):
    with conn.cursor() as cur:
        cur.execute(sql )
        if log:
            print("succeed to execute the sql ({0}).".format(sql))

def count(conn,schema=None,table=None,sql=None,log=False):
    with conn.cursor() as cur:
        cur.execute(sql if sql else "SELECT count(*) from {}.{}".format(schema,table) )
        rows = int(cur.fetchone()[0])
        if log:
            print("{1} rows are retrieved by sql ({0})".format(sql,rows))

        return rows

def get(conn,sql,log=False):
    """
    Return the found row  if have; otherwise return None
    """
    with conn.cursor() as cur:
        cur.execute(sql)
        row = cursor.fetchone()
        if log:
            if row:
                print("found one row by sql ({0}),{1}".format(sql,row))
            else:
                print("no row found by sql ({0})".format(sql))


        return row

def executeFile(filename,batch=100):
    with open(filename,"r") as f:
        transaction.set_autocommit(True)
        rows = 0
        sqls = []
        with connection.cursor() as cur:
            sql = f.readline()
            while sql:
                sql = sql.strip()
                if sql:
                    sqls.append(sql)
                    if len(sqls) == batch:
                        cur.execute("\n".join(sqls))
                        rows += len(sqls)
                        sqls.clear()
                        if rows % 1000 == 0:
                            print("processed {} lines".format(rows))
                sql = f.readline()

            cur.execute("\n".join(sqls))
            rows += len(sqls)
            print("processed {} lines".format(rows))


        
   

