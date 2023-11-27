import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from subprocess import Popen, PIPE
import os
from datetime import datetime
import webbrowser
import urllib.request
import webbrowser
from tkinter import messagebox
import json
import language_data



roslyn_path = './Roslyn'
source_file_path = './Program.cs'

def compile_cs(run_after=False):
    lang = language_var.get()
    console_output.configure(state='normal')
    console_output.delete(1.0, tk.END)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    console_output.insert(tk.END, language_data.texts["compilation_start"][lang].format(current_time))

    options = build_compile_options()
    csc_path = os.path.join(roslyn_path, 'csc.exe')
    output_path = os.path.join(roslyn_path, 'Data', 'Program.exe')
    command = [csc_path, source_file_path, '/out:' + output_path] + options

    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
    output, errors = process.communicate()
    console_output.insert(tk.END, output)
    if errors:
        console_output.insert(tk.END, errors)

    console_output.configure(state='disabled')
    
    if not errors:
        console_output.insert(tk.END, language_data.texts["compilation_success"][lang], language_data.texts["compilation_success"][lang])
        console_output.configure(state='normal')
        console_output.insert(tk.END, language_data.texts["program_location"][lang].format(output_path))
        console_output.configure(state='disabled')
        if run_after:
            os.startfile(output_path)


def build_compile_options():
    options = []
    if optimize_var.get() == 1:
        options.append('/optimize')
    if unsafe_var.get() == 1:
        options.append('/unsafe')
    if checked_var.get() == 1:
        options.append('/checked')
    if debug_info_var.get():
        options.append(f'/debug:{debug_info_var.get()}')
    if platform_var.get():
        options.append('/platform:' + platform_var.get())
    if no_warnings_var.get() == 1:
        options.append('/nowarn')
    if doc_var.get():
        options.append('/doc:' + doc_var.get())
    if define_var.get():
        options.append('/define:' + define_var.get())
    if reference_var.get():
        options.append('/reference:' + reference_var.get())
    if warn_level_var.get():
        options.append('/warn:' + warn_level_var.get())
    if nullable_var.get() == 1:
        options.append('/nullable')
    if lang_version_var.get():
        options.append('/langversion:' + lang_version_var.get())
    if lib_path_var.get():
        options.append('/lib:' + lib_path_var.get())
    if no_stdlib_var.get() == 1:
        options.append('/nostdlib')
    if additional_options_entry.get():
        options += additional_options_entry.get().split()
    return options


def open_file_directory():
    os.startfile(os.path.dirname(os.path.abspath(roslyn_path+"/Data")))

def clear_console():
    console_output.configure(state='normal')
    console_output.delete(1.0, tk.END)
    console_output.configure(state='disabled')

def show_settings():
    lang = language_var.get()

    settings_window = tk.Toplevel()
    settings_window.title(language_data.texts["settings_window_title"][lang])

    roslyn_label = tk.Label(settings_window, text=language_data.texts["roslyn_path_label"][lang])
    roslyn_label.pack(padx=5, pady=5)
    roslyn_entry = tk.Entry(settings_window)
    roslyn_entry.insert(0, roslyn_path)
    roslyn_entry.pack(padx=50, pady=5, fill='x', expand=True)

    def save_settings():
        global roslyn_path, source_file_path
        roslyn_path = roslyn_entry.get()
        source_file_path = source_file_entry.get()
        settings_window.destroy()

    source_file_label = tk.Label(settings_window, text=language_data.texts["source_file_path_label"][lang])
    source_file_label.pack(padx=5, pady=5)
    source_file_entry = tk.Entry(settings_window)
    source_file_entry.insert(0, source_file_path)
    source_file_entry.pack(padx=50, pady=5, fill='x', expand=True)

    save_button = ttk.Button(settings_window, text=language_data.texts["save_button"][lang], command=save_settings)
    save_button.pack(pady=10)


def get_blog_url():
    messagebox.showinfo("uwu","这个功能还没开喔 问就是懒！|This function hasn't been opened yet, but it's lazy!|這個功能還沒開喔 問就是懶！")

"""     try:
        url = 'https://github.com/TheD0ubleC/RoslynGUI/'
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            blog_url = data['blog_url']

            if blog_url:
                webbrowser.open(blog_url)
            else:
                messagebox.showinfo("博客信息", "暂时没有博客。")
    except Exception as e:
        messagebox.showerror("博客信息", f"获取博客链接时发生错误：{e}") """




def check_for_updates():
    messagebox.showinfo("uwu","这个功能还没开喔 问就是懒！|This function hasn't been opened yet, but it's lazy!|這個功能還沒開喔 問就是懶！")

    """ lang = language_var.get()
    try:
        url = 'https://github.com/TheD0ubleC/RoslynGUI/'
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            latest_version = data['tag_name']
            current_version = "1.0.0" 
            if current_version != latest_version:
                update_available = messagebox.askyesno(
                    language_data.texts["update_available_title"][lang], 
                    language_data.texts["update_available_message"][lang].format(latest_version)
                )
                if update_available:
                    webbrowser.open(data['html_url'])
            else:
                messagebox.showinfo(language_data.texts["no_update_title"][lang], language_data.texts["no_update_message"][lang])
    except Exception as e:
        messagebox.showerror(language_data.texts["update_check_error"][lang], language_data.texts["update_check_error"][lang].format(e)) """

def switch_language(event=None):
    lang = language_var.get()
    compile_button.config(text=language_data.texts["compile_button"][lang])
    run_button.config(text=language_data.texts["run_button"][lang])
    open_dir_button.config(text=language_data.texts["open_dir_button"][lang])
    clear_console_button.config(text=language_data.texts["clear_console_button"][lang])
    settings_button.config(text=language_data.texts["settings_button"][lang])
    version_button.config(text=language_data.texts["version_button"][lang])
    language_label.config(text=language_data.texts["language_label"][lang])
    console_output_frame.config(text=language_data.texts["console_output_frame"][lang])
    options_frame.config(text=language_data.texts["options_frame"][lang])
    console_radio.config(text=language_data.texts["app_type_console"][lang])
    window_radio.config(text=language_data.texts["app_type_window"][lang])
    optimize_check.config(text=language_data.texts["optimize_compile"][lang])
    nullable_check.config(text=language_data.texts["nullable_ref"][lang])
    no_stdlib_check.config(text=language_data.texts["no_standard_lib"][lang])
    unsafe_check.config(text=language_data.texts["allow_unsafe_code"][lang])
    checked_check.config(text=language_data.texts["check_overflow_underflow"][lang])
    no_warnings_check.config(text=language_data.texts["suppress_all_warnings"][lang])
    debug_info_label.config(text=language_data.texts["debug_info_label"][lang])
    platform_label.config(text=language_data.texts["platform_label"][lang])
    additional_options_label.config(text=language_data.texts["additional_options_label"][lang])
    doc_label.config(text=language_data.texts["xml_doc_label"][lang])
    define_label.config(text=language_data.texts["define_symbols_label"][lang])
    reference_label.config(text=language_data.texts["reference_label"][lang])
    warn_level_label.config(text=language_data.texts["warning_level_label"][lang])
    lang_version_label.config(text=language_data.texts["language_version_label"][lang])
    lib_path_label.config(text=language_data.texts["library_path_label"][lang])


def show_version_info():
    lang = language_var.get()
    version_window = tk.Toplevel()
    version_window.title(language_data.texts["version_window_title"][lang])
    tk.Label(version_window, text=language_data.texts["copyright"][lang]).pack(padx=10, pady=10)
    tk.Label(version_window, text=language_data.texts["version_number"][lang]).pack(padx=10, pady=10)
    tk.Label(version_window, text=language_data.texts["license_info"][lang]).pack(padx=10, pady=10)
    github_button = ttk.Button(version_window, text=language_data.texts["github_button"][lang], command=lambda: open_link('https://github.com/yourgithub'))
    github_button.pack(side=tk.LEFT, padx=5, pady=5)
    blog_button = ttk.Button(version_window, text=language_data.texts["blog_button"][lang], command=get_blog_url)
    blog_button.pack(side=tk.LEFT, padx=5, pady=5)
    check_update_button = ttk.Button(version_window, text=language_data.texts["check_update_button"][lang], command=check_for_updates)
    check_update_button.pack(side=tk.LEFT, padx=5, pady=5)

def open_link(url):
    webbrowser.open(url)

app = tk.Tk()
app.title("RoslynGUI Tools")
language_options = ['简体中文', 'English', '繁體中文','日本語']
language_var = tk.StringVar(value=language_options[0])
debug_options = ['none', 'full', 'pdbonly']
platform_options = ['AnyCPU', 'x86', 'x64', 'Itanium']
options_frame = ttk.LabelFrame(app, text="编译选项")
options_frame.pack(padx=10, pady=10, fill='x', expand=True)
app_type_var = tk.StringVar(value='console')
console_radio = ttk.Radiobutton(options_frame, text="控制台程序", variable=app_type_var, value='console')
console_radio.grid(row=0, column=0, padx=5, pady=5 )
window_radio = ttk.Radiobutton(options_frame, text="窗口程序", variable=app_type_var, value='window')
window_radio.grid(row=0, column=1, padx=0, pady=0)
optimize_var = tk.IntVar()
optimize_check = ttk.Checkbutton(options_frame, text="优化编译", variable=optimize_var)
optimize_check.grid(row=0, column=2, padx=0, pady=0)
nullable_var = tk.IntVar()
nullable_check = ttk.Checkbutton(options_frame, text="可空引用", variable=nullable_var)
nullable_check.grid(row=0, column=3, padx=0, pady=0)
no_stdlib_var = tk.IntVar()
no_stdlib_check = ttk.Checkbutton(options_frame, text="无标准库", variable=no_stdlib_var)
no_stdlib_check.grid(row=0, column=4, padx=0, pady=0)
unsafe_var = tk.IntVar()
unsafe_check = ttk.Checkbutton(options_frame, text="允许不安全代码", variable=unsafe_var)
unsafe_check.grid(row=0, column=5, padx=0, pady=0)
checked_var = tk.IntVar()
checked_check = ttk.Checkbutton(options_frame, text="检查溢出/下溢", variable=checked_var)
checked_check.grid(row=0, column=6, padx=0, pady=0)
no_warnings_var = tk.IntVar()
no_warnings_check = ttk.Checkbutton(options_frame, text="禁止所有警告", variable=no_warnings_var)
no_warnings_check.grid(row=0, column=7, padx=0, pady=0)
debug_info_var = tk.StringVar(value=debug_options[1])
debug_info_label = tk.Label(options_frame, text="调试信息:")
debug_info_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
debug_info_menu = ttk.Combobox(options_frame, textvariable=debug_info_var, values=debug_options)
debug_info_menu.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
platform_var = tk.StringVar(value=platform_options[0])
platform_label = tk.Label(options_frame, text="平台:")
platform_label.grid(row=1, column=2, padx=5, pady=5, sticky='w')
platform_menu = ttk.Combobox(options_frame, textvariable=platform_var, values=platform_options)
platform_menu.grid(row=1, column=3, padx=5, pady=5, sticky='ew')
additional_options_label = tk.Label(options_frame, text="附加选项:")
additional_options_label.grid(row=3, column=4, padx=5, pady=5, sticky='w')
additional_options_entry = tk.Entry(options_frame)
additional_options_entry.grid(row=3, column=5, columnspan=3, padx=5, pady=5, sticky='ew')
doc_var = tk.StringVar()
doc_label = tk.Label(options_frame, text="XML 文档:")
doc_label.grid(row=2, column=0, padx=5, pady=5)
doc_entry = tk.Entry(options_frame, textvariable=doc_var)
doc_entry.grid(row=2, column=1, padx=5, pady=5)
define_var = tk.StringVar()
define_label = tk.Label(options_frame, text="定义符号:")
define_label.grid(row=2, column=2, padx=5, pady=5)
define_entry = tk.Entry(options_frame, textvariable=define_var)
define_entry.grid(row=2, column=3, padx=5, pady=5)
reference_var = tk.StringVar()
reference_label = tk.Label(options_frame, text="引用:")
reference_label.grid(row=2, column=4, padx=5, pady=5)
reference_entry = tk.Entry(options_frame, textvariable=reference_var)
reference_entry.grid(row=2, column=5, columnspan=3, padx=5, pady=5, sticky='ew')
warn_level_var = tk.StringVar()
warn_level_label = tk.Label(options_frame, text="警告级别:")
warn_level_label.grid(row=3, column=0, padx=5, pady=5)
warn_level_entry = tk.Entry(options_frame, textvariable=warn_level_var)
warn_level_entry.grid(row=3, column=1, padx=5, pady=5)
lang_version_var = tk.StringVar()
lang_version_label = tk.Label(options_frame, text="语言版本:")
lang_version_label.grid(row=1, column=4, padx=5, pady=5)
lang_version_entry = ttk.Combobox(options_frame, textvariable=lang_version_var, values=['7.3', '7.2', '7.1', '7.0', '6.0', '5.0', '4.0', '3.0'])
lang_version_entry.grid(row=1, column=5, padx=5, pady=5)
lib_path_var = tk.StringVar()
lib_path_label = tk.Label(options_frame, text="库路径:")
lib_path_label.grid(row=3, column=2, padx=5, pady=5)
lib_path_entry = tk.Entry(options_frame, textvariable=lib_path_var)
lib_path_entry.grid(row=3, column=3, padx=5, pady=5)
console_output_frame = ttk.LabelFrame(app, text="控制台输出")
console_output_frame.pack(padx=10, pady=5, fill='both', expand=True)
console_output = tk.Text(console_output_frame, state='disabled', height=10)
console_output.pack(padx=5, pady=5, fill='both', expand=True)
buttons_and_language_frame = ttk.Frame(app)
buttons_and_language_frame.pack(padx=10, pady=5, fill='x', expand=True)
compile_button = ttk.Button(buttons_and_language_frame, text="编译", command=lambda: compile_cs())
compile_button.pack(side=tk.LEFT, padx=5, pady=5)
run_button = ttk.Button(buttons_and_language_frame, text="编译并运行", command=lambda: compile_cs(True))
run_button.pack(side=tk.LEFT, padx=5, pady=5)
open_dir_button = ttk.Button(buttons_and_language_frame, text="打开文件目录", command=open_file_directory)
open_dir_button.pack(side=tk.LEFT, padx=5, pady=5)
clear_console_button = ttk.Button(buttons_and_language_frame, text="清空控制台", command=clear_console)
clear_console_button.pack(side=tk.LEFT, padx=5, pady=5)
settings_button = ttk.Button(buttons_and_language_frame, text="设置", command=show_settings)
settings_button.pack(side=tk.LEFT, padx=5, pady=5)
version_button = ttk.Button(buttons_and_language_frame, text="版本信息", command=show_version_info)
version_button.pack(side=tk.LEFT, padx=5, pady=5)
language_label = tk.Label(buttons_and_language_frame, text="Language:")
language_label.pack(side=tk.LEFT, padx=5, pady=5)
language_options = ['简体中文', 'English','繁體中文','日本語']
language_var = tk.StringVar(value=language_options[0])
language_menu = ttk.Combobox(buttons_and_language_frame, textvariable=language_var, values=language_options)
language_menu.pack(side=tk.LEFT, padx=5, pady=5)
language_menu.bind("<<ComboboxSelected>>", switch_language)
app.mainloop()