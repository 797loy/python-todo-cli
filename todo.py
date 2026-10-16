# python-todo-cli：一个零依赖的命令行待办清单
# 只用标准库 json，适合练习 git clone -> 运行 -> 读代码
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(tasks):
    title = input("任务内容：").strip()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("已添加任务！")


def list_tasks(tasks):
    if not tasks:
        print("清单是空的，先加一个任务吧。")
        return
    print("-" * 30)
    for i, t in enumerate(tasks, start=1):
        mark = "[x]" if t["done"] else "[ ]"
        print(i, mark, t["title"])
    print("-" * 30)


def complete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    n = int(input("完成第几个任务？输入序号："))
    if 1 <= n <= len(tasks):
        tasks[n - 1]["done"] = True
        save_tasks(tasks)
        print("已标记完成！")
    else:
        print("序号超出范围。")


def main():
    tasks = load_tasks()
    while True:
        print("\n===== 待办清单 =====")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 完成任务")
        print("4. 退出")
        choice = input("选择（1-4）：").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("再见，任务已保存。")
            break
        else:
            print("请输入 1-4。")


if __name__ == "__main__":
    main()