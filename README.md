# BaiduTongjiAPI

百度统计 API 的 Python 封装

## 支持范围

|   账号类型   | 支持情况 |
| :----------: | :------: |
| 百度商业账号 |    ❌     |
|   百度账号   |    ✅     |

|                      API                       | 支持情况 |
| :--------------------------------------------: | :------: |
|                   Token 刷新                   |    ✅     |
|                    站点列表                    |    ✅     |
|               网站概况(趋势数据)               |    ✅     |
|               网站概况(地域分布)               |    ✅     |
| 网站概况(来源网站、搜索词、入口页面、受访页面) |    ✅     |
|                    趋势分析                    |    ✅     |
|                    实时访客                    |    ✅     |
|                    推广方式                    |    ❌     |
|                  百度推广趋势                  |    ❌     |
|                    全部来源                    |    ✅     |
|                    搜索引擎                    |    ✅     |
|                     搜索词                     |    ✅     |
|                    外部链接                    |    ✅     |
|                  指定广告跟踪                  |    ❌     |
|                    受访页面                    |    ✅     |
|                    入口页面                    |    ✅     |
|                    受访域名                    |    ✅     |
|                    地域分布                    |    ✅     |
|                地域分布(按国家)                |    ✅     |

## Doc

百度统计官方文档：

* https://tongji.baidu.com/api/manual/
* https://tongji.baidu.com/api/debug/#

具体使用详见源代码，下面是对项目结构：

```
baidutongji
├── __init__.py
├── api.py          # API 定义
├── data.py         # 可选参数数据结构
└── metrics.py      # 各 API 筛选指标数据结构
```

使用样例：

* 查询站点今天的网站概况（趋势数据）报表：
  ```python
  import baidutongji
  
  baidutongji.getTimeTrendRpt('{ACCESS_TOKEN}', '{SITE_ID}', datetime.date.today(), datetime.date.today(), TimeTrendRptMetrics(pv_count=True, visitor_count=True, ip_count=True, bounce_ratio=True, avg_visit_time=True))
  ```
  或者可以简化：
  ```python
  import baidutongji
  
  baidutongji.getTimeTrendRpt('{ACCESS_TOKEN}', '{SITE_ID}', datetime.date.today(), datetime.date.today(), TimeTrendRptMetrics().setAllTrue())
  ```
* 查询 `2022/01/01 ~ 2022/01/10` 与 `2022/04/01 ~ 2022/04/10` 趋势分析对比报表，指定时间粒度以天为单位，筛选用户为老用户，访问设备为 PC，地区为上海市：
  ```python
  import baidutongji
  
  baidutongji.getTrendTime('{ACCESS_TOKEN}', '{SITE_ID}', datetime.date(2022, 1, 1), datetime.date(2022, 1, 10), TrendTimeMetrics().setAllTrue(), datetime.date(2022, 4, 1), datetime.date(2022, 4, 10), Source.ALL, ClientDevice.PC, VisitorType.RETURN, TimeGran.DAY, Region(RegionType.PROVINCE, '上海'))
  ```
