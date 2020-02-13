
import time
from pywinauto import Application

cpuz = Application(backend='uia').start('C:\Program Files\CPUID\CPU-Z\cpuz.exe')

cpuz_window = cpuz.window()

date = cpuz_window.child_window(class_name="Static")
window_textbox = cpuz_window.child_window(title="Validate", control_type='Button').click_input()
