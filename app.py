# 线上和线下
# 线上一个一个项目
# 药品线上销售过程
# 生产----》用户
# 实现一个进--》存储到仓库
# 销----》销售
# 存----》商品的实时状态

# 需求：
# 1、写一个药品进货记录（字典），有药品编号、药品名称、药品的分类、药品的单价、进货时间、进货人属性
# 2、写一个药品的销售字典，有药品编号、药品名称、药品分类、药品单价、药品总价、销售时间、销售人属性

# 3、写一个药品库存放记录字典，有药品编号、药品名称、药品分类、药品单价、入库时间、库存管理人属性
# 4、写一个用户身份的字典，区分用户权限

# 操作：
# 1、登录药品进销存模块；
# 2、药品购入（对进货记录、库存记录进行添加）
# 3、销售药品（对销售记录、库存记录，进行添加）
# 4、药品入库（对库存记录进行添加和修改）
# 5、药品统计

# 通过输入药品名称，得到以下内容：

# 药品名称、药品购入数量、购入人、药品销售数量、销售人、药品库存数量、保管人
# 统计所有的库存药品销售情况（按照销售数量进行降序）
# 药品名称、药品销售数量、药品总价、药品销售比例



'''
商品进销存
'''


import time,datetime
# print('%s' % datetime.datetime.now())
# print('%s' % time.time())

# now_time=time.time()
# print(now_time*1000)

'''
商品进销系统
'''

user = {
    'admin': [
        {
            'uname':'admin',
            'upasswd':'123456'

        },
        {
            'uname':'solder',
            'upasswd':'123456'
        },
        {
            'uname':'buyer',
            'upasswd':'123456'
        }

    ]
}




'''
菜单管理界面,用于不同管理的程序入口
'''

def menu():
    print('*********************************')
    print('*1.登录药品采购平台             *')
    print('*2.采购药品                     *')
    print('*3.药品入库                     *')
    print('*4.药品销售                     *')
    print('*5.药品统计                     *')
    print('*6.退出                         *')
    print('*********************************')

'''
判断用户身份、验证用户名密码
返回状态 True or False
'''

def check_access(uname,upasswd):
    for item in user['admin']:
        if uname == item['uname']:
            # print('uname:%s,uu:%s'%(uname,item['uname']))
            flag = (upasswd == item['upasswd'])
            break
        else:
            flag = False
    return flag
'''
function:采购商品记录
parameter:
return:none
description:将采购的商品进行序列化，并将结果保存到采购字典中

'''
buy_dict={}
def buy_record(buy_time,**kw):
    buy_dict[buy_time]=kw
    


'''
function:入库商品记录
parameter:
return:none
description:将采购的商品入库，并将结果保存到库存字典中,如果当前库存有记录，
'''
stock_dict = {}
def stock_record(buy_time,stocker,stock_time):
    if buy_time in buy_dict.keys():
        kw = buy_dict[buy_time].copy()
        print('*************************************')
        # 入库记录是以药品编号作为记录
        m_id =kw.pop('mid')
        kw['stocker'] = stocker
        kw['stocktime'] = stock_time
        stock_dict[m_id] = kw
    else:
        print('输入采购时间有误！！！')


def main():
    while True:
        menu()
        user_input=input('请输入你的选择：')
        if '1' == user_input:
            user_name = input('请输入用户名：')
            user_password = input('请输入密码：')
            # 判断用户名、密码是否正确
            results = check_access(uname,upassword)
            if results:
                print('登录成功，请继续选择其他操作')
            else:
                print('用户名或密码不正确，请重新登录')
        elif '2' == user_input:
            buy_time = input('请输入采购时间，按照YYYYMMDD格式输入：')
            m_name = input('请输入药品名称：')
            m_id = input('请输入药品编号：')
            m_price = input('请输入药品单价：')
            m_buyer = input('请输入药品的采购者：')
            m_type = input('请输入药品分类：')
            m_number = input('请输入药品采购数量：')
            buy_record(buy_time,mname=m_name,mid=m_id,mprice=m_price,mbuyer=m_buyer,mtype=m_type,mnumber=m_number)
            print(buy_dict) 


        elif '3' == user_input:
            buy_time = input('请输入采购时间，按照YYYYMMDD格式输入：')
            # 库存管理员
            stocker = input('请输入库存管理员：')
            # 入库时间
            stocker_time = input('请输入入库时间，按照YYYYMMDD格式输入：')
            stock_record(buy_time,stocker,stocker_time)
            print(stock_dict)
        else:
            pass

if __name__ == "__main__":
    main()












'''
商品进销存系统
'''
user = {
    'admin':[
        {'uname':'admin',
         'upasswd':'123456'
        },
        {'uname':'solder',
         'upasswd':'123456'
        },
        {'uname':'buyer',
         'upasswd':'123456'
        }
    ]
}


# #菜单管理界面,用于不同管理的程序入口
# def menu():
#     print('*************************')
#     print('*1.登录药品采购平台     *')
#     print('*2.采购药品             *')
#     print('*3.药品入库             *')
#     print('*4.药品销售             *')
#     print('*5.药品统计             *')
#     print('*6.退出                 *')
#     print('*************************')

# #判断用户身份  验证用户密码
# #返回状态 true or false
# def chek_access(uname,upasswd):
#     flag = False
#     for item in user['admin']:
#         if uname == item['uname']:
#             print(item)
#             flag = (upasswd ==item['upasswd'])
#             # break
#         else:
#             flag = False
#     return flag
# '''
# function:采购商品记录
# parameter:
# return: none
# description:将采购的商品进行序列化，并将结果保存到采购字典中
# '''
# buy_dict = {}
# #**kw = {key1 : val,key2:val2...}   key1 = val,key2=val2...
# def buy_record(buy_time,**kw):
#     buy_dict[buy_time] = kw
# '''
# function:入库
# parameter:
# return: none
# description:将采购的商品进行入库，并将结果保存到库存字典中,如果当前库存里面有记录
# '''
# stock_dict = {}
# def stock_record(buy_time,stocker,stock_time):
#     if buy_time in buy_dict.keys():
#         kw = buy_dict[buy_time].copy()
#         #入库记录是以药品编号作为记录
#         m_id = kw.pop('mid')
#         kw['stocker'] = stocker
#         kw['stockertime'] = stock_time
#         stock_dict[m_id] = kw
#     else:
#         print('输入采购时间有误')

# def main():
#     while True:
#         menu()
#         user_input = input('请输入你的选择：')
#         if '1'==user_input:
#             user_name = input('请输入用户名：')
#             user_passwd = input('请输入密码：')
#             #判断用户名和密码是否正确
#             results = chek_access(user_name,user_passwd)
#             if results:
#                 print('登录成功，请继续选择其他操作')
#             else:
#                 print('用户名或密码不正确，请重新登录')
        
#         elif '2' == user_input:
#             buy_time = input('请输入采购时间，按照YYMMDD格式输入：')
#             m_name = input('请输入药品名：')
#             m_id = input('请输入药品编号：')
#             m_price = input('请输入要药品单价：')
#             m_buyer = input('请输入采购者：')
#             m_type = input('请输入药品的分类：')
#             m_number = input('请输入药品的采购数量：')
#             buy_record(buy_time, mname=m_name,mid=m_id,mprice=m_price,mbuyer=m_buyer,mtype=m_type,mnumber=m_number)
#             print(buy_dict)
#         elif '3' == user_input:
#             buy_time = input('请输入采购时间，按照YYMMDD格式输入：')
#             #库存管理员
#             stocker = input('请输入库管理员：')
#             #入库时间
#             stocker_time = input('请输入入库时间，按照YYMMDD格式输入：')
#             stock_record(buy_time,stocker,stocker_time)
#             print(stock_dict)
#         else:
#             pass

# if __name__ == "__main__":
#     main()
