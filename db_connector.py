# A variety of helper methods that assist with basic sqlite3 functionality

import sqlite3

# FUNCTION: insert(cursor, table, columns, values, multi=False)
# USAGE: insert(c, 'therapists', ['pt_id', 'name', 'summary', 'phone'], info)
# -------------------------------------------------------------
# Simplifies the insertion process. Given a cursor, the string name of a table,
# a list of strings of the relevant columns, and the values to be inserted (either a list
# or a list of tuples for multi=True), inserts the given values into the specified columns 
# of the table. Use multi and the aforementioned formatting for multiple inserts.
# ADD "REPLACE" FUNCTIONALITY!

def insert(cursor, table, values, columns=None, multi=False):
	if columns is not None:
		query = '''INSERT INTO %s(%s) VALUES (%s)''' % (table, ', '.join(columns), ', '.join(['?'] * len(columns)))
	else:
		if multi:
			col_len = len(values[0])
		else:
			col_len = len(values)
		query = '''INSERT INTO %s VALUES (%s)''' % (table, ', '.join(['?'] * col_len))
	#print query #for debug
	if multi:
		cursor.executemany(query, values)
	else:
		cursor.execute(query, values)



# FUNCTION: select(cursor, columns, table, distinct=False, where=None, order_by=None, limit=None)
# USAGE: select(c, ['therapist_id'], 'therapists', where='pt_id=' + str(info[0]))
# -------------------------------------------------------------
# Simplifies the selection process by constructing a select query around the
# given cursor, list of column names, table name, and optional parameters. If
# distinct=True, then the select is performed with the keyword "distinct". If
# optional clauses are specified (as strings), the query is performed with the 
# clauses. Remember to get the results from the cursor; this function does not 
# return results. THIS IS NOT INJECTION-SAFE!!!

def select(cursor, columns, table, distinct=False, where=None, order_by=None, limit=None):
	query = 'SELECT '
	if distinct:
		query += ' DISTINCT '
	query += '%s FROM %s' % (', '.join(columns), table)
	if where:
		query += ' WHERE ' + where
	if order_by:
		query += ' ORDER BY ' + order_by
	if limit:
		query += ' LIMIT ' + str(limit)
	#print query #for debug
	cursor.execute(query)






# FUNCTION: 
# USAGE: 
# -------------------------------------------------------------
# 