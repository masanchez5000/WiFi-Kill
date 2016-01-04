#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import subprocess


class SystemChecks:
	@staticmethod
	def pre_test():
		try:
			import gi
			gi.require_version('Gtk', '3.0')
			from gi.repository import Gtk
		except:
			raise Exception("[!] Error: This program requires python Gtk+ 3.0 installed!")

	@staticmethod
	def post_test():
		SystemChecks.__check_root()
		SystemChecks.__check_modules()
		SystemChecks.__check_binaries()
		SystemChecks.__check_services()
		

	@staticmethod
	def __check_root():		
		if os.geteuid() != 0:
			raise Exception("No elevated permissions. Please run as root.")

	@staticmethod
	def __check_modules():
		try:
			import scapy.all
		except:
			raise Exception("This program requires scapy python modules. Please install them.")

	@staticmethod
	def __check_binaries():
		if not SystemChecks.__check_cmd("ifconfig"):
			raise Exception("Could not locate \"ifconfig\" executable, please install or add to path.")
		if not SystemChecks.__check_cmd("iwconfig"):
			raise Exception("Could not locate \"iwconfig\" executable, please install or add to path.")
		print("[D] SystemChecks.__check_binaries(): TODO: iwconfig and ifconfig in debian is in /sbin/ and not in path...")

	@staticmethod
	def __check_services():
		if not SystemChecks.__check_service("NetworkManager"):
			raise Exception("\"NetworkManager\" service is running and may interfere with the program.")

	@staticmethod
	def __check_cmd(cmd):
		return subprocess.call("type " + cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

	@staticmethod
	def __check_service(serv):
		if SystemChecks.__check_cmd("systemctl"):
			# Systemctl is present...
			process = subprocess.Popen(['systemctl', 'status', serv+".service"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			process.wait()
			output = process.communicate()[0]
			return output.find('running') == -1
		return True

