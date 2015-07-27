#!/usr/bin/env python3
"""
pywri
"""
import os, sys, textwrap, configparser, datetime, argparse

global ConfigFile
DefaultPath = os.path.expanduser("~/.pywri.conf")
if os.path.exists(DefaultPath):
	ConfigFile = DefaultPath
global config
config = configparser.ConfigParser()

def main():
	parser = argparse.ArgumentParser(description="PyWri: A journal tool.", prog="PyWri")
	parser.add_argument('-d', '--dir',
		action='store', dest='ArgDir', default=None,
		help='Specify a journal directory.')
	parser.add_argument('--config',
		action='store', dest='ArgConfig', default=None,
		help='Specify an alternate config file.')
	args = parser.parse_args()
	
	JournalDir = args.ArgDir

	global ConfigFile
	if args.ArgConfig:
		ConfigFile = args.ArgConfig
	
	if JournalDir is None:
		JournalDir = ReadConfig('journal','JournalDir')
	
	print(JournalDir)
	print(ConfigFile)

	print("It didn't fail.")
	quit()	

def ReadConfig(key,val):
	if ConfigFile is None:
		print("No config file is selected.")
	try:
		config.read(ConfigFile)
		result = config[key][val]
		return result
	except:
		print("Error reading config file.")

def user_exit():
	print("\nUser exited.")
	quit()

def query_tool(query):
	try:
		result = input(query)
		return result
	except KeynoardInterrupt:
		user_exit()
	except:
		print("\nSyntax error.")
		quit()

main()
