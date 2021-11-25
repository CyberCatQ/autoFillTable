from mailmerge import MailMerge
from datetime import datetime
import os
import json
date = datetime.now()
year = date.year
month = date.month
day = date.day

fields = {'No',              # 红色编号
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
          'money_cent',      # 大写金额：角
          'money_h',         # 大写金额：佰
          'money_one',       # 大写金额：元
          'money_penny',     # 大写金额：分
          'money_t',         # 大写金额：仟
          'money_ten',       # 大写金额：拾
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

default_dic = {}
for index in fields:
    default_dic[index] = ''

number_dict = {
    '1': '一',
    '2': '二',
    '3': '三',
    '4': '四',
    '5': '五',
    '6': '六',
    '7': '七',
    '8': '八',
    '9': '九',
    '0': '零',
}


def table_generate(data_dict: dict, file_name=''):
    date = data_dict['dateEdit'].split(':')
    data_dict['date_day'] = date[2]
    data_dict['date_month'] = date[1]
    data_dict['date_year'] = date[0]
    
    for key, value in data_dict.items():
        data_dict[key] = str(value)
        
    default_dic.update(data_dict)
    if not os.path.exists('template.docx'):
        raise FileNotFoundError('No template.docx found.')
        
    template = MailMerge('template.docx')
    template.merge(
        count = default_dic['count'],
        date_month = default_dic['date_month'],
        date_day = default_dic['date_day'],
        money_one = default_dic['money_one'],
        package = default_dic['package'],
        transfer_fee = default_dic['transfer_fee'],
        start_add = default_dic['start_add'],
        money_h = default_dic['money_h'],
        agency_fund = default_dic['agency_fund'],
        delivery_cost = default_dic['delivery_cost'],
        code = default_dic['code'],
        payment_method = default_dic['payment_method'],
        network_department = default_dic['network_department'],
        money = default_dic['money'],
        goods_name = default_dic['goods_name'],
        money_t = default_dic['money_t'],
        money_penny = default_dic['money_penny'],
        date_year = default_dic['date_year'],
        add = default_dic['add'],
        weight = default_dic['weight'],
        people_name = default_dic['people_name'],
        money_cent = default_dic['money_cent'],
        phone_number = default_dic['phone_number'],
        self_fee = default_dic['self_fee'],
        money_tt = default_dic['money_tt'],
        money_ten = default_dic['money_ten'],
        No = default_dic['No']
    )
    template.write(file_name)


def number_transfer(number: str):
    number = str(number)
    listnum = list(number)
    result = []
    for i in listnum:
        if i == '.':
            continue
        result.append(number_dict[i])

    return result

    
