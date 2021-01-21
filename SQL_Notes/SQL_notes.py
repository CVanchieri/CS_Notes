import psycopg2
from pandas import DataFrame 

""" database connection """
### connect to an SQl(postgres) database with psycopg2 ###
### set credetials ###
AWSdatabase = '>database name<'
AWSuser = '>user name<'
AWSpassword = '>password<'
AWShost = 'host url'
AWSport = '>port<'
sql_AWS = 'postgresql+psycopg2://>database name<:>password<@host url:>port</>user name<'
## # build the connection ###
connection = psycopg2.connect(database=AWSdatabase,
                              user=AWSuser,
                              password=AWSpassword,
                              host=AWShost,
                              port=AWSport)
### set the cursor connection ##s#
cur = connection.cursor()


""" connection commands  """
### rollback after an error ###
connection.rollback()
### always save changes ###
connection.commit()
### close the connection ###
connection.close()


""" sql SELECT basic commands """
### selecting columns ### 
### SELECT all data from a table ###
sql_query_all_data = "SELECT * FROM >table name<" # query ALL(*) data from the table 
cur.execute(sql_query_all_data) # use cursor to execute query
records_all = cur.fetchall() # fetchall from cursor to get all data
records_one = cur.fetchone() # fetchone from cursor to get 1st index data
### create a dataframe from the data ###
df = DataFrame(records_all)  # set as dataframe 
df.columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5'] # label the columns 
df.head() # show the dataframe

### SELECT specific columns from a table ###
sql_query_columns = "SELECT column_1, column_2, column_3 FROM >table name<" 
cur.execute(sql_query_columns) # use cursor to execute query

### SELECT columns and additional data not in a table ###
sql_query_data_not_in_table = "SELECT column_1, 'value_x' FROM >table name<"
cur.execute(sql_query_data_not_in_table) # use cursor to execute query

""" sql SELECT with conditonals WHERE, AND, OR commands """
### conditionals ### 
### SELECT columns with WHERE conditionals ###
sql_query_condtionals_single = "SELECT column_1, column_2 FROM >table name< WHERE value > x"
cur.execute(sql_query_condtionals_single) # use cursor to execute query

### SELECT columns with multiple WHERE conditionals with AND ###
sql_query_condtionals_multi_and = "SELECT column_1, column_2 FROM >table name< WHERE value > x AND value < y "
cur.execute(sql_query_condtionals_multi_and) # use cursor to execute query

### SELECT columns with multiple WHERE conditionals with OR ###
sql_query_condtionals_multi_or = "SELECT column_1, column_2 FROM >table name< WHERE value > x OR value < y " 
cur.execute(sql_query_condtionals_multi_or) # use cursor to execute query

""" sql SELECT with ORDER BY commands """
### SELECT columns with order with ORDER BY ###
sql_query_orderby = "SELECT column_1, column_2 FROM >table name< ORDER BY column_2 DESC " 
cur.execute(sql_query_orderby) # use cursor to execute query

""" sql SELECT with JOIN commands """
### join ### 
### SELECT columns from table and join with another table ###
sql_query_and_join = "SELECT column_1, column_2 FROM >table_1 name< LEFT JOIN >table_2 name< USING(column_2)" 
### types of JOIN ###
# JOIN, returns rows with a match in both tables 
# LEFT JOIN, returns all rows from left table with matches from right table, no matches left table is still returned
# RIGHT JOIN, returns all rows from right table with matches from left table, no matches right table is still returned
# FULL JOIN, returns any records with a match in either table
cur.execute(sql_query_and_join) # use cursor to execute query

""" sql SELECT with ALIAS commands """
### alias ### 
### SELECT columns from tables and give them temporary names ###
sql_query_with_alias= "SELECT A.column_1, A.column_2, B.column_1, B.column_2 FROM >table_1 name< A >table_2 name< B" 
### use cases ### 
# if quering more than one table easy way to seperate tables
# if tables have columns with same names this can seperate the tables 
cur.execute(sql_query_with_alias) # use cursor to execute query

""" sql SELECT with UNION commands """
### union ### 
### SELECT columns to append rows data to eachother, results only matching columns+rows ### 
sql_query_union = """
                    SELECT column_1, column_2 FROM >table_1 name< 
                    UNION
                    SELECT column_1, column_2 FROM >table_2 name<
                  """
### condtions for use ### 
# returns results where there is a unique row
# must have same number and name of columns
cur.execute(sql_query_union) # use cursor to execute query

### SELECT columns to append rows data to eachother, results all columns+rows and duplicates ### 
sql_query_union_all = """
                    SELECT column_1, column_2 FROM >table_1 name< 
                    UNION ALL
                    SELECT column_1, column_2 FROM >table_2 name<
                    """
### condtions for use ### 
# returns results where there is a unique row
# must have same number and name of columns
cur.execute(sql_query_union_all) # use cursor to execute query


""" sql CREATE TABLE  """
### create a table, set columns names, primary key, value types(size) ###
sql_create_table = """CREATE TABLE >table name< (  
column_1 INTEGER PRIMARY KEY,  
column_2 VARCHAR(20),  
column_3 VARCHAR(30),  
column_4 CHAR(1),  
column_5 DATE);"""
# always specify a primary key
### value types ###
# https://www.w3schools.com/sql/sql_datatypes.asp
cur.execute(sql_create_table) # use cursor to execute

""" sql ALTER TABLE  """
### ALTER a table, add, remove, change, replace table info ###
sql_alter_table = """ALTER TABLE >table name<  ADD column_5 >value type<"""
# if an alter has conflict with the data it will throw an error, example changing string type to an integer
cur.execute(sql_alter_table) # use cursor to execute

""" sql copy TABLE  """
### copy a table and data into a new table ###
sql_copy_table = """SELECT * INTO >new table name<  FROM >table name<"""
# copies all data and schema to the new table
cur.execute(sql_copy_table) # use cursor to execute

### copy a table and data into a new table ###
sql_copy_table_schema = """SELECT * INTO >new table name<  FROM >table name< WHERE value1 <> value_2"""
# copies only the tables schema to the new table not the data
# use a false conditional statement to ignore the data
cur.execute(sql_copy_table_schema) # use cursor to execute


""" sql INSERT commands  """
### insert ### 
### insert values into all columns in table ###
sql_insert_values_all = """INSERT INTO >table name< VALUES ("value_1", "value_2", "value_3", "value_4", "value_5");"""
# can not use conditionals with INSERT
cur.execute(sql_insert_values_all) # use cursor to execute insert command

### insert values into specific columnns in table ###
sql_insert_values_specific = """
                            INSERT INTO >table name< (column_1, column_2, column_3)
                            VALUES ("value_1", "value_2", "value_3");
                            """ 
cur.execute(sql_insert_values_specific) # use cursor to execute 

### insert values into specific columnns in table ###
data_list = [ ("value_1", "value_2", "value_3", "value_4"),
               ("value_1", "value_2", "value_3", "value_4"),
               ("value_1", "value_2", "value_3", "value_4") ]
for v in data_list:
    format_string = """INSERT INTO >table name< (column_1, column_2, column_3, column_4)
                        VALUES (NULL, "{val1}", "{val2}", "{val3}", "{val4}");""" # value placement is based on column index

    sql_insert_values_from_list = format_string.format(val1=v[0], val2=v[1], val3=v[3], val4=v[4])
    cur.execute(sql_insert_values_from_list) # use cursor to execute 

    
""" sql UPDATE commands  """
### update ### 
### update all specific row values ###
sql_update_row_value = """UPDATE >table name< SET column_1 = "value_1", column_2 = "value_2";"""
### conditions for use ###
# must specify table, column, value
# will update all values based on parameter
cur.execute(sql_update_row_value) # use cursor to execute

### update specific row values with conditional ###
sql_update_row_value_conditional = """UPDATE >table name< SET column_1 = "value_1", column_2 = "value_2" WHERE column_1 = "value_3";"""
cur.execute(sql_update_row_value_conditional) # use cursor to execute

### update specific row values with multiple conditionals ###
sql_update_row_value_multi_conditionals = """UPDATE >table name< SET column_1 = "value_1", column_2 = "value_2" WHERE (column_1 = "value_3") AND column_2 = "value_4) OR column_1 = 'value_5;"""
cur.execute(sql_update_row_value_multi_conditionals) # use cursor to execute


""" sql UPSERT commands  """
### upsert ### 
### when inserting a value it will update that value if already exists ###
sql_upsert_values = """
                    INSERT INTO >table name< (column_1, column_2)
                    VALUES("value_1", value_2)
                    ON DUPLICATE KEY UPDATE column_2 = value_2;
                    """
### conditions for use ###
# works with MySQL may not work Postgres
# if inserting a value that already exists will throw error 
cur.execute(sql_upsert_values) # use cursor to execute


""" sql DELETE all data command  """
### delte all data in a table ###
sql_delete_all_data= """DELETE FROM >table name<;"""
# will delete all data from table but not the table itself 
cur.execute(sql_delete_all_data) # use cursor to execute drop command

### delte specific data in a table ###
sql_delete_specific_data= """DELETE FROM >table name< WHERE column_1 = "value_1";"""
# use conditionals to delete more specific data
cur.execute(sql_delete_specific_data) # use cursor to execute drop command


""" sql DROP TABLE commands  """
### drop an entire table ###
sql_drop_table = """DROP TABLE >table name<;"""
cur.execute(sql_drop_table) # use cursor to execute drop command
