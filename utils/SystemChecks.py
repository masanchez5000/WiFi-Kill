#!/usr/bin/python2
# -*- coding: utf-8 -*-

class SystemChecks:
	@staticmethod
	def pre_test():
		print("[D] SystemChecks.pre_test(): TODO: Implement!")
		# TODO: Chek if GTK is installed...

	@staticmethod
	def post_test():
		SystemChecks.__check_root()
		SystemChecks.__check_modules()
		SystemChecks.__check_binaries()
		

	@staticmethod
	def __check_root():		
		# TODO: Are we root? -> If not show a dialog and raise an exception...
		print("[D] SystemChecks.__check_root(): TODO: Implement!")

	@staticmethod
	def __check_modules():
		# TODO: Is scapy installed?
		print("[D] SystemChecks.__check_modules(): TODO: Implement!")

	@staticmethod
	def __check_binaries():
		print("[D] SystemChecks.__check_binaries(): TODO: Implement!")
		# TODO: Is iwconfig present? -> sudo apt-get install wireless-tools
		# TODO: WTF? iwconfig in debian is in /sbin/iwconfig and not in path...
