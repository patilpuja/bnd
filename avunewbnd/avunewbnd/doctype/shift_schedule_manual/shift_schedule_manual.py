
# -*- coding: utf-8 -*-
# Copyright (c) 2018, pranali and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from avunewbnd.api.data_list import load_data
import ast


class ShiftScheduleManual(Document):
	def onload(self):
		dlist=load_data()
		#frappe.msgprint("hii")
		self.get("__onload").data_list = dlist








@frappe.whitelist()
def passing_templatedata_to_python(data):
	#frappe.msgprint("function is working")
	d=ast.literal_eval(data)
	#frappe.msgprint(str(d))
	
	for i in range(0,len(d)):
		#date= frappe.utils.data.formatdate (d[i]["Day"], "yyyy-MM-dd")
		doc = frappe.get_doc({

  "doctype": "Shift Schedule",
     "shift_time": d[i]["Shift"],
     "employee_name":d[i]["Employee"],
     "store": d[i]["Store"],
     "attendance_date" : d[i]["Day"],
     "company": d[i]["Company"],
     "employee" : d[i]["Empid"],
     "naming_series" : "SHT-"
     
	})
		doc.insert(ignore_permissions=True)
		doc.submit()
	
	
	frappe.msgprint("Done");
	return "Done"
	
	


@frappe.whitelist()
def load_existing_data(from_date,to_date,start_date):
	fdate = frappe.utils.data.format_datetime (from_date, "yyyyMMdd")
	tdate = frappe.utils.data.format_datetime (to_date, "yyyyMMdd")
	sdate = frappe.utils.data.format_datetime (start_date, "yyyyMMdd")
	#frappe.msgprint("fdate  "+fdate+" todate  "+tdate)
	myt_sql="CALL getschedule("+fdate+", "+tdate+", "+sdate+");"
	#frappe.msgprint(str(myt_sql))
	lastweekdetails=frappe.db.sql(myt_sql, as_dict=1)
	#frappe.msgprint(lastweekdetails)
	return lastweekdetails
