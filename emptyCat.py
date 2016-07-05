#!/usr/bin/env python
#-*- coding: utf-8 -*-

################ INIT ########################
#Import db module
from wmflabs import db
#Init db module
conn = db.connect('cswiki')

#Define functions
#Print HTML header
def header():
	print """
<!DOCTYPE html>
<html lang="cs-cz">
	<head>
		<meta charset="utf-8" />
		<title>Titulek</title>
	</head>
	<body>
	"""

#Print HTML tail
def tail():
	print """
	</body>
</html>
	"""

################## PROGRAM ##################
header()

#Fetch data from DB
cur = conn.cursor()
with cur:
	sql = 'select CONCAT("Category:", page_title, "<br />") from page where page_namespace=14 and page_title not in(select cl_to from categorylinks) and page_id not in (select tl_from from templatelinks where tl_title="Metakategorie") and page_title not like "%Údržba%" and page_id not in (select tl_from from templatelinks where tl_title="Údržbová_kategorie") and page_title not like "Narození%" and page_title not like "Úmrtí%"'
	cur.execute(sql)
	data = cur.fetchall()

#Print it in HTML-form
print "<ol>"
for row in data:
	print "<li>" + row[0] + "</li>"
print "</ol>"

tail()
