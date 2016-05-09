#!/bin/bash

echo -e '<!DOCTYPE html>\n<html lang="cs-cz">\n<head>\n<meta charset="utf-8" />\n<title>Titulek</title>\n</head>\n<body>\n'
echo 'select CONCAT("Category:", page_title, "<br/>") from page where page_namespace=14 and page_title not in(select cl_to from categorylinks) and page_id not in (select tl_from from templatelinks where tl_title="Metakategorie") and page_title not like "%Údržba%" and page_id not in (select tl_from from templatelinks where tl_title="Údržbová_kategorie") and page_title not like "Narození%" and page_title not like "Úmrtí%"' | sql cswiki | sed '1d'
echo -e '</body>\n</html>'
