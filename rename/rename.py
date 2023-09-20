import os
import tkinter as tk

def rename_files():
    directory = directory_entry.get()
    old_str = old_str_entry.get()
    new_str = new_str_entry.get()

    # 获取指定目录下的所有文件名
    files = os.listdir(directory)

    for filename in files:
        # 检查文件名是否包含待替换的字符串
        if old_str in filename:
            # 生成新的文件名
            new_filename = filename.replace(old_str, new_str)

            # 构建旧文件路径和新文件路径
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            try:
                # 重命名文件
                os.rename(old_path, new_path)
                result_label.config(text=f"已将文件 {filename} 重命名为 {new_filename}")
            except OSError as e:
                result_label.config(text=f"重命名文件 {filename} 失败: {str(e)}")

# 创建主窗口
root = tk.Tk()
root.title("文件重命名工具")

# 创建标签和输入框
directory_label = tk.Label(root, text="目录路径:")
directory_label.pack()
directory_entry = tk.Entry(root)
directory_entry.pack()

old_str_label = tk.Label(root, text="待替换的字符串:")
old_str_label.pack()
old_str_entry = tk.Entry(root)
old_str_entry.pack()

new_str_label = tk.Label(root, text="替换的字符串:")
new_str_label.pack()
new_str_entry = tk.Entry(root)
new_str_entry.pack()

# 创建按钮和结果标签
rename_button = tk.Button(root, text="重命名文件", command=rename_files)
rename_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
