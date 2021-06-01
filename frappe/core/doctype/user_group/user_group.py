# -*- coding: utf-8 -*-
# Copyright (c) 2021, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class UserGroup(Document):
	def after_insert(self):
		frappe.cache().delete_key('user_groups')

	def on_trash(self):
		frappe.cache().delete_key('user_groups')
