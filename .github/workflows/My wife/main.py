from wife_manager import WifeManager

# 创建管理类实例
manager = WifeManager()

# 自动添加预设老婆信息
manager.add_wife("第五人格", "克洛伊", 27, "8.25", "有品位的奢侈品，高档食物", 162)
manager.add_wife("崩坏三", "丽塔", 22, "3.1", "完美的料理，干净的工作环境", 168)
manager.add_wife("赛马娘", "米浴", 6, "3.5", "蓝蔷薇，美好的事物", 145)

def user_add_wife():
    print("\n========== 添加老婆信息 ==========")
    name = input("请输入老婆姓名（唯一标识）：").strip()
    ip = input("请输入角色ip：").strip()
    old = input("请输入老婆年龄：").strip()
    birthday = input("请输入老婆生日：").strip()
    love = input("请输入老婆喜好：").strip()
    height = input("请输入老婆身高：").strip()

    if not (name and ip and old and birthday and love and height):
        print("❌ 所有信息不能为空，请重新输入！")
        return

    success, msg = manager.add_wife(ip, name, old, birthday,love,height)  # 调用实例方法
    print(msg)

def user_delete_wife():
    if manager.get_wife_count() == 0:
        print("\n❌ 暂无该老婆的信息喵，无需删除！")
        return
    target_name = input("\n请输入要删除的老婆姓名：").strip()
    success, msg = manager.delete_wife_by_name(target_name)
    print(msg)

def show_menu():
    print("\n========== 老婆信息管理系统 ==========")
    print("1. 添加老婆信息")
    print("2. 删除老婆信息")
    print("3. 查看所有老婆信息")
    print("4. 查看老婆信息总数")
    print("0. 退出系统")
    return input("请选择操作序号：").strip()

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            user_add_wife()
        elif choice == "2":
            user_delete_wife()
        elif choice == "3":
            manager.show_all_wives()  # 调用实例方法
        elif choice == "4":
            print(f"\n📊 当前老婆信息总数：{manager.get_wife_count()}")
        elif choice == "0":
            print("\n👋 退出系统，拜拜喵")
            break
        else:
            print("\n❌ 无效选择，请输入0-4的序号！")

if __name__ == "__main__":
    main()