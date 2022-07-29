import setuptools


def read(path):
	with open(path, 'r', encoding='utf-8') as f:
		content = f.read()
	return content


def make_email(prefix, domain):
	return f'{prefix}@{domain}'


setuptools.setup(
	name = 'baidutongji',
	version = '0.1.6',
	author = 'JeffersonQin',
	author_email = make_email('1247006353', 'qq.com'),
	packages = ['baidutongji'],
	url = 'https://github.com/JeffersonQin/BaiduTongjiAPI',
	license = 'MIT License',
	description = '百度统计 API Python 封装',
	long_description = read('README.md'),
	long_description_content_type='text/markdown',
	keywords = ['stats', 'api', 'baidu'],
	install_requires = [
		'requests'
	]
)
