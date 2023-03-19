# -*- coding: utf-8 -*-
"""

Author: lowdill

"""

import yahoo_fin.stock_info as yfin
import pandas as pd
from datetime import date, timedelta

stDt = "12/04/2006"
stock_als = "^GSPC"
intTime = "1mo"
tdyDt = date.today() + timedelta(days=-1)


snp_test = yfin.get_data(stock_als, 
                         start_date=stDt, 
                         end_date=tdyDt, 
                         index_as_date = True, 
                         # interval="1wk")
                         interval=intTime)

print(snp_test)