
# -*- coding: utf-8 -*-

"Nightly Tools Developers."

from pickle import dump

def generate_docs(file,
	title,
	description1,
	alias,
	description2,
	examples,
	copyright,
	license,
	epilog):

	nd = {
		'title': title,
		'__description__': description1,
		'alias': alias,
		'description': description2,
		'examples': examples,
		'copyright': copyright,
		'license': license,
		'epilog': epilog,
		}

	with open(''.join([file, '.nd']), 'wb') as file:
		dump(nd, file)

