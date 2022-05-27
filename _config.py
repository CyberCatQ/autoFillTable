import os
from datetime import datetime

__version__ = '1.2.0'
date = datetime.now()
year = str(date.year)
month = str(date.month)
day = str(date.day)
now = year + month.rjust(2, '0') + day.rjust(2, '0')
program_file_path = os.path.dirname(os.path.abspath(__file__))

fields = {'Code_No',         # 红色编号
          'add',             # 送货地址
          'agency_fund',     # 代收款
          'code',            # 单号
          'count',           # 数量
          'date_day',        # 日期：日
          'date_month',      # 日期：月
          'date_year',       # 日期：年
          'delivery_cost',   # 配送费
          'goods_name',      # 品名
          'money',           # 金额(小写)
          'money_cent',      # 大写金额：分
          'money_h',         # 大写金额：佰
          'money_one',       # 大写金额：元
          'money_dime',     # 大写金额：角
          'money_t',         # 大写金额：仟
          'money_ten',       # 大写金额：拾1
          'money_tt',        # 大写金额：万
          'network_department',  # 网络单位
          'package',         # 包装
          'payment_method',  # 支付方式
          'people_name',     # 收货人姓名
          'phone_number',    # 电话
          'self_fee',        # 自提费
          'start_add',       # 始发站
          'transfer_fee',    # 中转费
          'weight'}          # 重量
          
number_dict = {
    '1': '壹',
    '2': '贰',
    '3': '叁',
    '4': '肆',
    '5': '伍',
    '6': '陆',
    '7': '柒',
    '8': '捌',
    '9': '玖',
    '0': '零'
}

class ParseConfig:
    def __init__(self) -> None:
        pass
    
    def parse(self):
        raise NotImplementedError

class ShunJieCfg(ParseConfig):
    def __init__(self) -> None:
        super().__init__()
        self.ADDRESS = '重庆'
        self.CO_NAME = '顺捷'
    
    def parse(self, words_result, number_result):
        parse_result = []

        for index, name in enumerate(words_result):
            _index = index * 3
            if name == '合计':
                continue
            parse_result.append({'name': name, 'count': number_result[_index], 'weight': number_result[_index + 1], 'agency_fund_value': number_result[_index + 2]})
        
        return parse_result

