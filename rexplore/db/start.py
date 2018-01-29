import configparser
import _mysql
from _mysql_exceptions import *

from rexplore import db

'''
For documentation:
	http://mysqlclient.readthedocs.io/user_guide.html?highlight=mysql_options#introduction
'''

def config(config_path):
	config = configparser.ConfigParser()
	config.read(config_path)
	return config


def read_sql(sql_path, **kwargs):
	
	with open(sql_path, 'r') as file:
		query = file.read()
		for param in kwargs:
			query = query.replace('$' + param, kwargs[param])
		return query


class initialize(object):
	def __init__(self, config_path):
		self.config = config(config_path)
		# self.con()

	def connect(self):
		return _mysql.connect(
			host=self.config.get('MySql','host'),
			port=self.config.getint('MySql','port'),
			user=self.config.get('MySql','user'),
			passwd=self.config.get('MySql','password'),
			db=self.config.get('MySql','db'))

	def create_schema(self):

		con = self.connect()

		print('=== Creating [%s.user] table' % self.config.get('MySql','db'))
		create_user = read_sql('sql/CREATE_user.sql')
		con.query(create_user)

		print('=== Creating [%s.comment] table' % self.config.get('MySql','db'))
		create_user = read_sql('sql/CREATE_comment.sql')
		con.query(create_user)
		

		con.close()


	def insert_single(self, table, values_dict):

		# Initialize		
		con = self.connect()
		sql = "INSERT INTO " + self.config.get('MySql','db') + "." + table + " "
		first = True
		values = []

		con.escape_string("'")

		for col, value in values_dict.items():
			if first:
				sql += "(" + col 
				first = False
			else:
				sql += ", " + col

			if isinstance(value, str):
				values.append("'" + value + "'")
			else:
				values.append(value)

		values = "(" + ', '.join(str(val) for val in values) + ");"
		sql += ") VALUES " + values

		self.run_sql(con, sql)
		con.close()

	def insert_single_comment(self, table, values_dict):

		list_key = [key for key in values_dict]
		list_val = [_mysql.escape_string(val).decode("""utf-8""", """ignore""") if isinstance(val, str) else val for key, val in values_dict.items()]
		list_val = ["""'""" + val + """'""" if isinstance(val, str) else val for val in list_val]

		# Initialize		
		con = self.connect()
		query = ("""INSERT INTO """ + self.config.get('MySql','db') + """.""" + table + """ """ +
			"""(""" + """,""".join(["""%s"""] * len(list_key)) + """) """ +
			"""VALUES """ +
			"""(""" + """,""".join(["""%s"""] * len(list_val)) + """)""")

		query = (query % tuple(list_key + list_val))
		self.run_sql(con, query)
		con.close()

	def insert_user(self, user_obj):
		user_values = db.clean_user(user_obj)
		self.insert_single('user', user_values)

	def insert_comment(self, comment_obj):
		comment_values = db.clean_comment(comment_obj)
		self.insert_single_comment('comment', comment_values)


	def run_sql(self, connection, sql):
		try:
			return connection.query(sql)
		except IntegrityError as e:
			print(e)
		


if __name__ == '__main__':


	init = initialize('../../config/config.ini')
	init.create_schema()

	# sq = read_sql('sql/CREATE_user.sql', **{
	# 	'user_id': 'hello',
	# 	'db':'date'})
	# print(sq)