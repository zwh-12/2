def get_constellation(month, day):
    """
    星座日期范围：
    白羊座: 3.21 - 4.19
    金牛座: 4.20 - 5.20
    双子座: 5.21 - 6.21
    巨蟹座: 6.22 - 7.22
    狮子座: 7.23 - 8.22
    处女座: 8.23 - 9.22
    天秤座: 9.23 - 10.23
    天蝎座: 10.24 - 11.22
    射手座: 11.23 - 12.21
    摩羯座: 12.22 - 1.19
    水瓶座: 1.20 - 2.18
    双鱼座: 2.19 - 3.20
    """
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "白羊座"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "金牛座"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "双子座"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "巨蟹座"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "狮子座"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "处女座"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "天秤座"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "天蝎座"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "射手座"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "摩羯座"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "水瓶座"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "双鱼座"
    return None

def is_valid_date(month, day):
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month[month - 1]:
        return False
    return True

def main():
    fortune_data = {
        "白羊座": "财运上升，注意休息",
        "金牛座": "感情运势良好，工作有贵人相助",
        "双子座": "思维敏捷，适合学习新技能",
        "巨蟹座": "家庭和睦，适合与家人沟通",
        "狮子座": "事业运势旺盛，领导力强",
        "处女座": "细节决定成败，桃花运佳",
        "天秤座": "人际关系和谐，适合社交活动",
        "天蝎座": "直觉敏锐，适合做重要决定",
        "射手座": "旅行运佳，适合拓展视野",
        "摩羯座": "事业稳步上升，适合制定长期计划",
        "水瓶座": "创意灵感涌现，适合艺术创作",
        "双鱼座": "浪漫氛围浓厚，适合表达情感"
    }
    
    print("=" * 50)
    print("        星座运势查询系统")
    print("=" * 50)
    
    while True:
        birthday = input("\n请输入您的生日（格式：月-日，如 3-21）：").strip()
        
        try:
            parts = birthday.split("-")
            if len(parts) != 2:
                print("生日格式错误，请输入 月-日（如 3-21）")
                continue
            
            month = int(parts[0])
            day = int(parts[1])
            
            if not is_valid_date(month, day):
                print("生日格式错误，请输入 月-日（如 3-21）")
                continue
            
            constellation = get_constellation(month, day)
            fortune = fortune_data.get(constellation, "运势未知")
            
            print(f"\n你的星座是{constellation}，今日运势：{fortune}")
            
        except ValueError:
            print("生日格式错误，请输入 月-日（如 3-21）")
            continue
        
        continue_flag = False
        while True:
            continue_query = input("\n是否继续查询其他生日？（输入 y 继续，n 退出）：").strip().lower()
            if continue_query == "y":
                continue_flag = True
                break
            elif continue_query == "n":
                print("\n感谢使用星座运势查询系统！")
                break
            else:
                print("输入无效，请输入 y 或 n")
        if not continue_flag:
            break

if __name__ == "__main__":
    main()
