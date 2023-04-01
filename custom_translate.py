# -*- coding: utf-8 -*-
import os, sys, re
from googletrans import Translator

def custom_translate(target_file_path):
	# 引数のファイルパスから必要な情報を取得
	file_name, file_ext = os.path.splitext(target_file_path)
	output_file_path = file_name + '_en' + file_ext

	# 引数のファイルが.txtでなければ何もしない	
	if not file_ext == ".txt":	
		exit()
	
	# 引数のファイルを配列で読み込み
	try:
		with open(target_file_path) as f:
			comments = f.readlines()
	except FileNotFoundError as err:
		print(err)
		exit()
		
	# 内容が無ければ何もしない
	if len(comments) == 0:	
		exit()
	
	replased_comments = []
	for comment in comments:
		translated_comment = Translator().translate(comment, dest='en').text
		replased_comments.append(custom_replase(translated_comment))

	# 元のファイルと同改装に_en.txtとして書き出す
	with open(output_file_path, mode='w+') as f:
		for replased_comment in replased_comments:
			f.write('{}\n'.format(replased_comment))
	
def custom_replase(comment):
	# 対象と置換後を辞書で登録。対象の大文字小文字は気にしなくて良い
	replace_str_dic = {
		'imus': 'THE IDOLM@STERr'
	}

	for key in replace_str_dic:
			regex = re.compile(r'{}'.format(key), re.IGNORECASE)
			comment = re.sub(regex, replace_str_dic[key], comment)
	
	return comment

if __name__ == '__main__':
	if len(sys.argv) != 2:
		exit()

	custom_translate(sys.argv[1])
