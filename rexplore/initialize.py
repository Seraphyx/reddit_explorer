import mysql
import configparser




def initialize(config_path):
	'''
	Import a config .ini file.
	It should have the following definition:
	'''
	config = configparser.ConfigParser()
	config.read(config_path)

	