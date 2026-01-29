# wife_manager
from myxp_class import MyXP

class WifeManager:
    def __init__(self):
        # 创建一个字典，存储老婆
        # 键：老婆的名字（name），MyXP类的实例（包含该老婆的所有信息）
        self.wife_objects = {}

    def add_wife(self, ip, name, old, birthday,love,height):
        #添加新老婆，写入该老婆的参数（所属ip，名字，年龄，生日等）
        if name in self.wife_objects:
            #如果该老婆信息已存在库中则显示以下
            return False, f"❌ {name}的信息已存在，无需重复添加~"
        try:
            # 将年龄参数转换成整数类型，确保输入为数字
            old = int(old)
        except ValueError:
            return False, f"❌ 年龄必须是数字，请重新输入！"
        self.wife_objects[name] = MyXP(ip, name, old, birthday,love,height)
        return True, f"✅ {name}的信息已添加成功！"

    def delete_wife_by_name(self, target_name):
        if target_name in self.wife_objects:
            del self.wife_objects[target_name]
            return True, f"✅ {target_name}的信息已提交删除！"
        else:
            return False, f"❌ 未找到{target_name}的信息，删除失败~"

    def show_all_wives(self):
        if not self.wife_objects:
            print("\n📜 暂无任何老婆信息~")
            return
        print("\n========== 当前已添加的老婆列表 ==========")
        for name, obj in self.wife_objects.items():
            obj.show_info()

    def get_wife_count(self):
        return len(self.wife_objects)