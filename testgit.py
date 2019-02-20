## updated by Frank at 2018-11-05
## apply for  for

import pandas as pd
import funct_lao as fl
from datetime import datetime,timedelta


# 定义时间
today = datetime.now()
# today = datetime(2018, 7, 1)
firstday_thismonth = datetime(today.year, today.month, 1)
firstday_thismonth_s = datetime.strftime(firstday_thismonth, "%Y-%m-%d")
lastday_lastmonth_d = firstday_thismonth - timedelta(days=1)
ym = "".join([str(lastday_lastmonth_d.year), str(lastday_lastmonth_d.month).zfill(2)])
ymd = datetime.strftime(today, "%Y%m%d")
'''数据获取'''
# 积分明细
data_itg = fl.data_released("".join(["data_itg", "_", ym]))
# 兑换明细
data_exc = fl.data_released("".join(["data_exc", "_", ym]))
## 产品信息
data_prodinfo = fl.data_released("".join(["data_prodinfo", "_", ym]))
## 门店信息
data_storeinfo = fl.data_released("".join(["data_storeinfo", "_", ym]))
# 全部会员信息
data_meminfo_whole = fl.data_released("".join(["data_meminfo_whole", "_", ym]))
# 会员首次积分日期
data_meminfo = fl.data_released("".join(["data_meminfo", "_", ym]))

'''数据处理'''


'''数据统计'''


'''数据导出'''