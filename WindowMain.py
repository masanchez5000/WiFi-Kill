#!/usr/bin/python2
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from DialogInterfaces import DialogInterfaces
from utils.Sniffer import Sniffer


class WindowMain:
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file("WindowMain.glade")
		self.builder.connect_signals(self)
		self.window = self.builder.get_object("window_main")
		self.log_text = self.builder.get_object("window_main_notebook_log_text")
		self.log_text_buff = self.log_text.get_buffer()
		self.networks_liststore = self.builder.get_object("window_main_liststore_networks")
		self.sniffer_thread = Sniffer()
		self.__loop()

	def __loop(self):
		self.window.show_all()
		Gtk.main()

	def networks_clear(self):
		self.networks_liststore.clear()

	def networks_append(self, interface):
		self.networks_liststore.append(interface)

	def log_append(self, text):
		end_iter = self.log_text_buff.get_end_iter()
		self.log_text_buff.insert(end_iter, text)

	def on_destroy(self, *args):
		self.log_append("[+] Stopping sniffer...\n")
		self.sniffer_thread.stop()
		Gtk.main_quit(*args)

	def window_main_toolbar_interfaces_clicked(self, button):
		DialogInterfaces()

	def window_main_toolbar_scan_clicked(self, button):
		self.log_append("[+] Starting sniffer...\n")
		self.sniffer_thread.start()

	def window_main_toolbar_networks_update_clicked(self, button):
		nets = self.sniffer_thread.get_networks()
		self.networks_clear()
		for n in nets:
			self.networks_append(n.get_as_tuple())

