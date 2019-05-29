# coding:utf-8

import unittest

import easyquotation


class TestSina(unittest.TestCase):
    def setUp(self):
        self._sina = easyquotation.use("sina")

    def test_get_stock_data(self):
        stocks = self._sina.stocks(['000001'])
        self.assertEqual(len(stocks), 1)

    def test_extract_stock_name(self):
        """
        fix https://github.com/shidenggui/easyquotation/issues/51
        """
        stock = self._sina.format_response_data(MOCK_DATA)
        stock_name = stock['000002']['name']
        self.assertEqual(stock_name, "万 科Ａ")

    def test_skip_empty_quotation_stock(self):
        """
        有些股票的行情返回为 var hq_str_sz160923="";
        这时候应该跳过解析
        :return:
        """
        excepted = {
            "160922": {
                "ask1": 1.11,
                "ask1_volume": 3100,
                "ask2": 1.13,
                "ask2_volume": 100,
                "ask3": 1.169,
                "ask3_volume": 2900,
                "ask4": 1.17,
                "ask4_volume": 12000,
                "ask5": 0.0,
                "ask5_volume": 0,
                "bid1": 1.053,
                "bid1_volume": 42000,
                "bid2": 1.05,
                "bid2_volume": 7500,
                "bid3": 0.0,
                "bid3_volume": 0,
                "bid4": 0.0,
                "bid4_volume": 0,
                "bid5": 0.0,
                "bid5_volume": 0,
                "buy": 1.053,
                "close": 1.074,
                "date": "2019-04-08",
                "high": 0.0,
                "low": 0.0,
                "name": "恒生中小",
                "now": 0.0,
                "open": 0.0,
                "sell": 1.11,
                "time": "09:41:45",
                "turnover": 0,
                "volume": 0.0,
            },
            "160924": {
                "ask1": 1.077,
                "ask1_volume": 400,
                "ask2": 1.134,
                "ask2_volume": 900,
                "ask3": 1.16,
                "ask3_volume": 9300,
                "ask4": 1.196,
                "ask4_volume": 1000,
                "ask5": 0.0,
                "ask5_volume": 0,
                "bid1": 1.034,
                "bid1_volume": 42000,
                "bid2": 1.031,
                "bid2_volume": 300,
                "bid3": 1.009,
                "bid3_volume": 700,
                "bid4": 0.992,
                "bid4_volume": 500,
                "bid5": 0.99,
                "bid5_volume": 8000,
                "buy": 1.034,
                "close": 1.095,
                "date": "2019-04-08",
                "high": 0.0,
                "low": 0.0,
                "name": "恒指LOF",
                "now": 0.0,
                "open": 0.0,
                "sell": 1.077,
                "time": "09:41:36",
                "turnover": 0,
                "volume": 0.0,
            },
        }

        result = self._sina.format_response_data([MOCK_EMPTY_STOCK_DATA])
        self.maxDiff = None
        self.assertDictEqual(result, excepted)


MOCK_DATA = 'var hq_str_sz000002="万 科Ａ,27.300,27.620,27.150,27.420,27.010,27.140,27.150,19027744,516971294.900,200,27.140,15200,27.130,45400,27.120,63400,27.110,210700,27.100,2000,27.150,3000,27.170,2900,27.180,22200,27.190,7700,27.200,2019-05-29,14:37:09,00"; \n'
MOCK_EMPTY_STOCK_DATA = """var hq_str_sz160922="恒生中小,0.000,1.074,0.000,0.000,0.000,1.053,1.110,0,0.000,42000,1.053,7500,1.050,0,0.000,0,0.000,0,0.000,3100,1.110,100,1.130,2900,1.169,12000,1.170,0,0.000,2019-04-08,09:41:45,00";
var hq_str_sz160923="";
var hq_str_sz160924="恒指LOF,0.000,1.095,0.000,0.000,0.000,1.034,1.077,0,0.000,42000,1.034,300,1.031,700,1.009,500,0.992,8000,0.990,400,1.077,900,1.134,9300,1.160,1000,1.196,0,0.000,2019-04-08,09:41:36,00";
var hq_str_sz000002="万 科Ａ,27.300,27.620,27.150,27.420,27.010,27.140,27.150,19027744,516971294.900,200,27.140,15200,27.130,45400,27.120,63400,27.110,210700,27.100,2000,27.150,3000,27.170,2900,27.180,22200,27.190,7700,27.200,2019-05-29,14:37:09,00"; 
"""
