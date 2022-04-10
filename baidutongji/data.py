from enum import Enum


__all__ = ['Source', 'ClientDevice', 'VisitorType', 'TimeGran', 'DomainType', 'RegionType', 'Region']


PROVINCE_LIST = ["", "北京", "上海", "天津", "广东", "福建", "海南", "安徽", "贵州", "甘肃", "广西", "河北", "河南", "黑龙江", "湖北", "湖南", "吉林", "江苏", "江西", "辽宁", "内蒙古", "宁夏", "青海", "山东", "山西", "陕西", "四川", "西藏", "新疆", "云南", "浙江", "重庆", "香港", "台湾", "澳门"]


class Source(Enum):
	"""
	来源
	"""
	DIRECT = 'through'
	SEARCH = 'search'
	LINK = 'link'
	ALL = None


class ClientDevice(Enum):
	"""
	设备
	"""
	PC = 'pc'
	MOBILE = 'mobile'
	ALL = None


class VisitorType(Enum):
	"""
	访客类型
	"""
	NEW = 'new'
	RETURN = 'old'
	ALL = None


class TimeGran(Enum):
	"""
	时间粒度
	"""
	HOUR = 'hour'
	DAY = 'day'
	WEEK = 'week'
	MONTH = 'month'


class DomainType(Enum):
	"""
	域名类型
	"""
	SOCIAL_MEDIA = 1
	NAVIGATION_SITES = 2
	EMAIL = 4
	ALL = None


class RegionType(Enum):
	"""
	地域类型
	"""
	CHINA = 'china'
	PROVINCE = 'province'
	ALL = None


class Region(object):
	"""
	地域
	"""
	def __init__(self, region_type: RegionType, province_name: str = None):
		"""地区实例化方法

		Args:
			region_type (RegionType): 地区种类
			province_name (str, optional): 若为省，输入省的中文. Defaults to None.
		"""
		self.region_type = region_type
		self.province_name = province_name
	
	def __str__(self):
		if self.region_type == RegionType.CHINA:
			return 'china'
		elif self.region_type == RegionType.PROVINCE:
			return f'province,{PROVINCE_LIST.index(self.province_name)}'
		else:
			return ''