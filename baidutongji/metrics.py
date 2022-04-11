class BaiduTongjiMetrics(object):
	def getMetrics(self):
		"""
		获取站点指标
		:return:
		"""
		ret = []
		for key, value in self.__dict__.items():
			if isinstance(value, bool) and value:
				ret.append(key)
		return ','.join(ret)
	
	def setAllTrue(self):
		"""
		设置所有指标为True
		:return:
		"""
		for key, value in self.__dict__.items():
			if isinstance(value, bool):
				self.__dict__[key] = True
		return self


class TimeTrendRptMetrics(BaiduTongjiMetrics):
	def __init__(self, pv_count=False, visitor_count=False, ip_count=False, bounce_ratio=False, avg_visit_time=False, trans_count=False):
		self.pv_count, self.visitor_count, self.ip_count, self.bounce_ratio, self.avg_visit_time, self.trans_count = pv_count, visitor_count, ip_count, bounce_ratio, avg_visit_time, trans_count


class DistrictRptMetrics(BaiduTongjiMetrics):
	def __init__(self, pv_count=False):
		self.pv_count = pv_count


class CommonTrackRptMetrics(BaiduTongjiMetrics):
	def __init__(self, pv_count=False):
		self.pv_count = pv_count


class TrendTimeMetrics(BaiduTongjiMetrics):
	def __init__(self, pv_count=False, pv_ratio=False, visit_count=False, visitor_count=False, new_visitor_count=False, new_visitor_ratio=False, ip_count=False, bounce_ratio=False, avg_visit_time=False, avg_visit_pages=False, trans_count=False, trans_ratio=False, avg_trans_cost=False, income=False, profit=False, roi=False):
		self.pv_count, self.pv_ratio, self.visit_count, self.visitor_count, self.new_visitor_count, self.new_visitor_ratio, self.ip_count, self.bounce_ratio, self.avg_visit_time, self.avg_visit_pages, self.trans_count, self.trans_ratio, self.avg_trans_cost, self.income, self.profit, self.roi = pv_count, pv_ratio, visit_count, visitor_count, new_visitor_count, new_visitor_ratio, ip_count, bounce_ratio, avg_visit_time, avg_visit_pages, trans_count, trans_ratio, avg_trans_cost, income, profit, roi


class TrendLatestMetrics(BaiduTongjiMetrics):
	def __init__(self, area=False, source=False, access_page=False, keyword=False, searchword=False, is_ad=False, visitorId=False, ip=False, visit_time=False, visit_pages=False, start_time=False):
		self.area, self.source, self.access_page, self.keyword, self.searchword, self.is_ad, self.visitorId, self.ip, self.visit_time, self.visit_pages, self.start_time = area, source, access_page, keyword, searchword, is_ad, visitorId, ip, visit_time, visit_pages, start_time


class SourceMetrics(BaiduTongjiMetrics):
	def __init__(self, pv_count=False, pv_ratio=False, visit_count=False, visitor_count=False, new_visitor_count=False, new_visitor_ratio=False, ip_count=False, bounce_ratio=False, avg_visit_time=False, avg_visit_pages=False, trans_count=False, trans_ratio=False):
		self.pv_count, self.pv_ratio, self.visit_count, self.visitor_count, self.new_visitor_count, self.new_visitor_ratio, self.ip_count, self.bounce_ratio, self.avg_visit_time, self.avg_visit_pages, self.trans_count, self.trans_ratio = pv_count, pv_ratio, visit_count, visitor_count, new_visitor_count, new_visitor_ratio, ip_count, bounce_ratio, avg_visit_time, avg_visit_pages, trans_count, trans_ratio


class VisitToppageMetrics(BaiduTongjiMetrics):
	def __init__(self, pv_count=False, visitor_count=False, ip_count=False, visit1_count=False, outward_count=False, exit_count=False, average_stay_time=False, exit_ratio=False):
		self.pv_count, self.visitor_count, self.ip_count, self.visit1_count, self.outward_count, self.exit_count, self.average_stay_time, self.exit_ratio = pv_count, visitor_count, ip_count, visit1_count, outward_count, exit_count, average_stay_time, exit_ratio


class VisitLandingpageMetrics(BaiduTongjiMetrics):
	def __init__(self, visit_count=False, visitor_count=False, new_visitor_count=False, new_visitor_ratio=False, ip_count=False, bounce_ratio=False, avg_visit_time=False, avg_visit_pages=False, trans_count=False, trans_ratio=False, out_pv_count=False):
		self.visit_count, self.visitor_count, self.new_visitor_count, self.new_visitor_ratio, self.ip_count, self.bounce_ratio, self.avg_visit_time, self.avg_visit_pages, self.trans_count, self.trans_ratio, self.out_pv_count = visit_count, visitor_count, new_visitor_count, new_visitor_ratio, ip_count, bounce_ratio, avg_visit_time, avg_visit_pages, trans_count, trans_ratio, out_pv_count


class VisitTopdomainMetrics(BaiduTongjiMetrics):
	def __init__(self, pv_count=False, pv_ratio=False, visit_count=False, visitor_count=False, new_visitor_count=False, new_visitor_ratio=False, ip_count=False, bounce_ratio=False, avg_visit_pages=False, average_stay_time=False):
		self.pv_count, self.pv_ratio, self.visit_count, self.visitor_count, self.new_visitor_count, self.new_visitor_ratio, self.ip_count, self.bounce_ratio, self.avg_visit_pages, self.average_stay_time = pv_count, pv_ratio, visit_count, visitor_count, new_visitor_count, new_visitor_ratio, ip_count, bounce_ratio, avg_visit_pages, average_stay_time
