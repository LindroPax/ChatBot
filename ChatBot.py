import sys  
import time  
  
def process_input(user_input):   
    processed_input = user_input.replace("吗", "").replace("?", "!")  
    return processed_input  
  
# 选择语言  
language = input("选择语言/choose language: 中文/english:").strip().lower()  
  
if language == "中文":  
    # Chinese
    Re = input("输入Y以继续访问Ai: ").strip().lower()  
    if Re != 'y':  
        print("进程即将被杀死")  
        for i in range(3, 0, -1):  
            print(f"还有{i}秒中断程序")  
            time.sleep(1)  
        print("程序已被中断,再见:)")  
        sys.exit(0)  
    else:  
        print("Ai已上线")  
  
    keep_running = True  
  
    while keep_running:  
        user_input = input("请向我提问(想要离开请说退出、我走了或滚): ")  
        cleaned_input = user_input.strip().lower()  
  
        if cleaned_input in ["退出", "我走了"]:  
            print("Ai已离开。")  
            sys.exit(0)  
        elif cleaned_input == "滚":  
            print("ai伤心的离开")  
            sys.exit(0)  
        else:  
            print("Ai:", process_input(user_input))  
  
elif language == "english":  
    # English  
    Re = input("Enter 'Y' to continue accessing Ai: ").strip().lower()  
    if Re != 'y':  
        print("Process will be terminated soon")  
        for i in range(3, 0, -1):  
            print(f"{i} seconds remaining to interrupt the program")  
            time.sleep(1)  
        print("Program has been interrupted, goodbye :)")  
        sys.exit(0)  
    else:  
        print("Ai is online")  
  
    keep_running = True  
  
    while keep_running:  
        user_input = input("Ask me a question (to leave, say 'exit', 'i'm leaving' or 'go away'): ")  
        cleaned_input = user_input.strip().lower()  
  
        if cleaned_input in ["exit", "i'm leaving"]:  
            print("Ai has left.")  
            sys.exit(0)  
        elif cleaned_input == "go away":  
            print("Ai leaves with sadness")  
            sys.exit(0)  
        else:  
            print("Ai:", process_input(user_input))  
  
else:   
    print("不支持的语言选择，程序将退出。/Unsupported language selection and the program will exit.")  
    sys.exit(0)
