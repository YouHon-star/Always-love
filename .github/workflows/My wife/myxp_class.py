class MyXP:
    #老婆信息模版喵
    def __init__(self,ip,name,old,birthday,love,height):
        self.ip=ip
        self.name = name
        self.old = old
        self.birthday = birthday
        self.love = love
        self.height = height

    def show_info(self):
        print(f"IP: {self.ip}")
        print(f"姓名: {self.name}")
        print(f"年龄: {self.old}")
        print(f"生日: {self.birthday}")
        print(f"喜欢: {self.love}")
        print(f"身高: {self.height}")

        # 销毁对象（其实从来不删老婆信息只是练习喵）
   # def __del__(self):
     #print(f"{self.name}该老婆信息已销毁喵撒有哪啦呜呜呜")

#     #创建对象，引用变量，指向对象实例
# wife1 = MyXP("第五人格", "克洛伊", 27, "8.25",'有品位的奢侈品，高档食物',162)
# wife1.show_info()
#
# wife2 = MyXP("崩坏三", "丽塔", 22, "3.1","完美的料理，干净的工作环境",168)
# wife2.show_info()
#
# wife3 = MyXP("赛马娘", "米浴", 6, "3.5","蓝蔷薇，美好的事物",145)
# wife3.show_info()
#
