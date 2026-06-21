#问题板

from rich.console import Console
from rich.table import Table
from rich import box
import logging
from rapidfuzz import process
import json
from pathlib import Path
from datetime import datetime

#logging配置（未使用）
logging.basicConfig(
    level=logging.INFO
)

#通用打印函数（解决打印美观问题）
console = Console()
def print_students(students,title="学生成绩表"):
    """打印学生列表，中文完美对齐"""
    if not students:
        console.print("[yellow]暂无数据[/yellow]")
        return
    # 创建表格
    table = Table(
        title=title,
        box=box.ROUNDED,          # 圆角边框，类似 rounded_grid
        show_header=True,
        header_style="bold cyan",
        border_style="grey50",
    )
    # 添加列
    for key in students[0]:
        table.add_column(key, justify="center", no_wrap=True)
    # 添加行
    for stu in students:
        table.add_row(*[str(v) for v in stu.values()])
    console.print(table)

p = Path('E:\students.json')

#加载数据
def load():
    if p.exists():
        return json.loads(p.read_text())
    else:
        print('数据文件不存在，返回空列表')
        return []

students = load()
print('欢迎使用学生成绩管理系统，当前系统中有',len(students),'位学生')


#数值校验（范围0-100）
class ScoreError(ValueError):
    def __init__(self, value,reason):
        self.value = value
        self.reason = reason
        super().__init__(f'{reason},请重新输入')

def validate_score(score):
    if score>100 or score<0:
        raise ScoreError(score,'成绩范围在0-100之间')

#计算总分、平均分
def sum_avg(chinese_score,english_score,math_score):
    sum = chinese_score+english_score+math_score
    average = round(sum/3,2)   #四舍五入，保留一位
    return sum,average

#新增
def add():
    print(f'\n======新增学生信息=====\n')
    print('请输入学生信息：')
    while True:
        sid = input('学号：')
        if sid != '':
            break
        else:
            print('学号不能为空，请重新输入')
    while True:    
        if select_by_sid(sid) != []:
            #学号已存在
            r = input('\n该学号已存在，是否进行覆盖（y/n）：')
            if r == 'y':
                #进行覆盖修改操作
                update(sid)
                input('\n按 Enter 键继续...')
                break
            elif r == 'n':
                #跳过，不新增
                print('\n已取消新增')
                break
            else:
                print('输入无效，请重新输入')
                continue
        else:
            #学号不存在
            while True:
                name = input('姓名：')
                if name != '':
                    break
                else:
                    print('姓名不能为空，请重新输入')
            while True:
                try:
                    chinese_score = float(input('语文成绩：'))
                    validate_score(chinese_score)
                    english_score = float(input('英语成绩：'))
                    validate_score(english_score)
                    math_score = float(input('数学成绩：'))
                    validate_score(math_score)
                    break
                except ScoreError as e:
                    print(e)
                except ValueError:
                    print(f'成绩必须是数值格式,请重新输入')
            c = sum_avg(chinese_score,english_score,math_score)
            data = {'学号':sid,'姓名':name,'语文':chinese_score,'英语':english_score,'数学':math_score,'总分':c[0],'平均分':c[1]}
            students.append(data)
            print(f'\n  🎖️ 学生{name}({sid})添加成功')
            break

#查询全部
def select():
    if len(students) == 0:
        print('\n当前系统中无学生数据')
    else:
        print_students(students)
        print(f'\n共{len(students)}名学生')

#根据学号查询
def select_by_sid(target):
    result = [s for s in students if s['学号'] == target]
    return result


#修改成绩方法
def update_score(account_name,stu_data):
        old_score = stu_data[0][account_name]
        while True:
            try:
                new_score = float(input('请输入新成绩：'))
                validate_score(new_score)
                break
            except ScoreError as e:
                print(e)
            except ValueError:
                print(f'成绩必须是数值格式,请重新输入')
        stu_data[0][account_name] = new_score
        print(f'{stu_data[0]['姓名']}的{account_name}成绩已更新：{old_score}->{new_score}')
        s = sum_avg(stu_data[0]['语文'],stu_data[0]['英语'],stu_data[0]['数学'])
        stu_data[0]['总分'] = s[0]
        stu_data[0]['平均分'] = s[1]
        print_students(stu_data,'修改后学生信息')
        input('\n按 Enter 键继续...')    

#修改
def update(*sid):
    print(f'======修改学生成绩=====\n')
    if len(students) == 0:
        print('当前系统中无学生数据')
    else:
        if sid != ():
            u_sid = sid[0]
        else:
            u_sid = input('请输入要修改的学生学号：')
        #返回结果为：[{}] 单条数据
        r = select_by_sid(u_sid)
        if r == []:
            print(f'\n暂未查询到该学生信息')
        else:
            print_students(r,'当前学生信息')
        while True:    
            print('\n请选择要修改的科目')
            print(f'1.语文（当前：{r[0]['语文']}）\n2.英语（当前：{r[0]['英语']}）\n3.数学（当前：{r[0]['数学']}）\n4.退出修改')
            account_code = input('\n请输入科目编号：')
            if account_code == '1':
                update_score('语文',r)
            elif account_code == '2':
                update_score('英语',r)
            elif account_code == '3':
                update_score('数学',r)
            elif account_code == '4':
                print('退出修改')
                break
            else:
                print('输入无效，请重新输入')
                continue
        print(f'\n🎖️学生信息修改成功')


#删除
def delete():
    print(f'======删除学生信息=====\n')
    if len(students) == 0:
        print('当前系统中无学生数据')
    else:
        u_sid = input('请输入要删除的学生学号：')
        #返回结果为：[{}] 单条数据
        r = select_by_sid(u_sid)
        if r == []:
            print(f'\n暂未查询到该学生信息')
        else:
            print_students(r,'当前学生信息')
            while True:    
                q = input('\n是否确认删除？（y/n）：')
                if q == 'y':
                    #删除
                    try:
                        students.remove(r[0])
                        print('\n删除成功👌')
                        input('\n按 Enter 键继续...')
                        break
                    except ValueError as e:
                        print('系统中不存在该信息')
                elif q == 'n':
                    #不删除
                    print('\n已取消删除')
                    break
                else:
                    print('输入无效，请重新输入')
                    continue

#按姓名关键字模糊查找
def select_by_name(key):
    if not key:
        print('\n查询全部学生')
        return students;
    names = [s['姓名'] for s in students]
    #按姓名精确匹配
    exact = [s for s in students if key in s['姓名']]
    if exact:
        return exact
    #按姓名关键字模糊匹配,返回 (匹配项, 相似度, 原始索引)只取超过阈值的
    matches = process.extract(key,names,score_cutoff=50)
    indeces = [idx for _,_,idx in matches]
    return [students[i] for i in indeces]

#精确查找
def select_info():
    print(f'======查询学生信息=====\n')
    if len(students) == 0:
        print('当前系统中无学生数据')
    else:
        while True:
            print('\n1.按学号精确查找\n2.按姓名模糊查找\n3.退出查找')
            choice = input('请选择查询方式：')
            if choice == '1':
                #按学号精确查找
                u_sid = input('请输入要查询的学生学号：')
                #返回结果为：[{}] 单条数据
                r = select_by_sid(u_sid)
                print_students(r,'按学号精确查找')
                input('\n按 Enter 键继续...')
            elif choice == '2':
                #按姓名模糊查找
                key = input('请输入姓名关键字：')
                r = select_by_name(key)
                print_students(r,'按姓名模糊查找')
                print(f'\n共{len(r)}名学生')
                input('\n按 Enter 键继续...')
            elif choice == '3':
                print('退出查找')
                break
            else:
                print('输入无效，请重新输入')
                continue

#排序方法
def sort_method(account_name,reverse):
    return sorted(students,key = lambda s:s[account_name],reverse=reverse)

#排序
def sort():
    print(f'======成绩排序=====\n')
    fields = {
        '1':'学号',
        '2':'姓名',
        '3':'语文',
        '4':'英语',
        '5':'数学',
        '6':'总分'
    }
    while True:
        print('\n排序依据：')
        for k,v in fields.items():
            print(f'{k}.按{v}')
        print('7.取消排序')
        b = input('请输入排序依据：')
        if b == '7':
            print('\n取消排序\n')
            break
        if b not in fields:
            print('排序依据无效，请重新输入')
            continue
        while True:            
            print('排序方式：1.升序（从低到高）2.降序（从高到低）')            
            m = input('请输入排序方式：')            
            if m in ('1', '2'):                
                break            
            print('排序方式无效，请重新输入')
        reverse = (m == '2')        
        s = sort_method(fields[b], reverse)        
        print_students(s)        
        input('按 Enter 键继续')
            

#保存数据
def save():
    print(f'======保存数据=====\n')
    try:
        size = p.write_text(json.dumps(students,indent=2, ensure_ascii=False))
        print(f'正在保存{len(students)}条记录\n')
        now = datetime.now()
        print(f'👌数据已保存至students.json\n')
        print(f"文件大小：{size/1024}kb\n保存时间：{now}")
    except Exception as e:
        print(f'文件保存失败：{e}')

    


while True:
    print('\n1.查询全部信息\n2.新增学生信息\n3.修改学生成绩\n4.删除学生信息\n5.查询学生信息\n6.成绩排序\n7.保存数据\n8.退出系统')
    choice = input('请输入你要进行的操作\n')
    if choice == '1':
        select()
        input('\n按 Enter 键返回菜单...')
    elif choice == '2':
        add()
        input('\n按 Enter 键返回菜单...')
    elif choice == '3':
        update()
        input('\n按 Enter 键返回菜单...')
    elif choice == '4':
        delete()
        input('\n按 Enter 键返回菜单...')
    elif choice == '5':
        select_info()
        input('\n按 Enter 键返回菜单...')
    elif choice == '6':
        sort()
        input('\n按 Enter 键返回菜单...')
    elif choice == '7':
        save()
        input('\n按 Enter 键返回菜单...')
    elif choice == '8':
        print('\n感谢使用，下次再见😘\n')
        break
    else:
        print('输入无效，请重新输入')
        continue


