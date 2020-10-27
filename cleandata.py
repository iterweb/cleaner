from tkinter import *

import clear_methods


root = Tk()

status_recycle_bin = IntVar()
status_cookies = IntVar()
status_recent = IntVar()
status_win_temp = IntVar()
status_local_temp = IntVar()
status_win_caches = IntVar()
status_win_wer = IntVar()
status_win_history = IntVar()
status_micr_windows = IntVar()
status_microsoft = IntVar()
status_loc_crashdamps = IntVar()
status_D3DSCache = IntVar()
status_ElevatedDiagnostics = IntVar()
status_SquirrelTemp = IntVar()
status_Package_Cache = IntVar()
status_Packages = IntVar()
status_LocalLow = IntVar()
status_m_Protect = IntVar()
status_Proof = IntVar()
status_clear_log = IntVar()
status_bloskhosts = IntVar()


def cleaning():
    if status_bloskhosts.get() == 1:
        clear_methods.add_block_hosts()
    if status_clear_log.get() == 1:
        clear_methods.clear_all_logs()
    if status_Proof.get() == 1:
        clear_methods.clear_proof()
    if status_m_Protect.get() == 1:
        clear_methods.clear_m_protect()
    if status_LocalLow.get() == 1:
        clear_methods.clear_locallow()
    if status_Packages.get() == 1:
        clear_methods.clear_packages()
    if status_Package_Cache.get() == 1:
        clear_methods.clear_package_cache()
    if status_SquirrelTemp.get() == 1:
        clear_methods.clear_squirreltemp()
    if status_ElevatedDiagnostics.get() == 1:
        clear_methods.clear_elevated_diagnostics()
    if status_D3DSCache.get() == 1:
        clear_methods.clear_d3dscache()
    if status_loc_crashdamps.get() == 1:
        clear_methods.clear_loc_crashdamps()
    if status_microsoft.get() == 1:
        clear_methods.clear_microsoft()
    if status_micr_windows.get() == 1:
        clear_methods.clear_mirs_windows()
    if status_win_history.get() == 1:
        clear_methods.clear_win_history()
    if status_win_wer.get() == 1:
        clear_methods.clear_win_wer()
    if status_recycle_bin.get() == 1:
        clear_methods.clear_recycle_bin()
    if status_cookies.get() == 1:
        clear_methods.clear_cookies()
    if status_recent.get() == 1:
        clear_methods.clear_recent()
    if status_win_temp.get() == 1:
        clear_methods.clear_win_temp()
    if status_local_temp.get() == 1:
        clear_methods.clear_local_temp()
    if status_win_caches.get() == 1:
        clear_methods.clear_win_caches()


root.title('Clean Data')
root.iconbitmap('logo_clean.ico')
root.geometry('400x208')
root.resizable(False, False)


window_top = LabelFrame(root, text='Для корректной очистки, закройте все открытые приложения', fg='red', font='Times '
                                                                                                              '11')
window_top.place(x=1, width=398, height=200, anchor='nw')

#window_top

cb_recycle_bin = Checkbutton(window_top, text='Корзина', variable=status_recycle_bin)
cb_recycle_bin.place(x=2, y=2, width=65, height=15, anchor='nw')

cookies = Checkbutton(window_top, text='Cookies', variable=status_cookies)
cookies.place(x=72, y=2, width=60, height=15, anchor='nw')

windows_recent = Checkbutton(window_top, text='Recent', variable=status_recent)
windows_recent.place(x=137, y=2, width=57, height=15, anchor='nw')

windows_temp = Checkbutton(window_top, text='WindowsTemp', variable=status_win_temp)
windows_temp.place(x=200, y=2, width=97, height=15, anchor='nw')

app_local_temp = Checkbutton(window_top, text='LocalTemp', variable=status_local_temp)
app_local_temp.place(x=297, y=2, width=97, height=15, anchor='nw')

windows_caches = Checkbutton(window_top, text='WinCaches', variable=status_win_caches)
windows_caches.place(x=20, y=22, width=100, height=15, anchor='nw')

windows_wer = Checkbutton(window_top, text='WinWER', variable=status_win_wer)
windows_wer.place(x=108, y=22, width=90, height=15, anchor='nw')

windows_hist = Checkbutton(window_top, text='WinHistory', variable=status_win_history)
windows_hist.place(x=188, y=22, width=90, height=15, anchor='nw')

windows_micr = Checkbutton(window_top, text='MicWin', variable=status_micr_windows)
windows_micr.place(x=272, y=22, width=90, height=15, anchor='nw')

windows_microsoft = Checkbutton(window_top, text='Microsoft', variable=status_microsoft)
windows_microsoft.place(x=10, y=42, width=90, height=15, anchor='nw')

local_crashdamps = Checkbutton(window_top, text='CrashDumps', variable=status_loc_crashdamps)
local_crashdamps.place(x=95, y=42, width=90, height=15, anchor='nw')

local_D3DSCache = Checkbutton(window_top, text='D3DSCache', variable=status_D3DSCache)
local_D3DSCache.place(x=185, y=42, width=90, height=15, anchor='nw')

local_ElevatedDiagnostics = Checkbutton(window_top, text='Diagnostics', variable=status_ElevatedDiagnostics)
local_ElevatedDiagnostics.place(x=275, y=42, width=90, height=15, anchor='nw')

local_SquirrelTemp = Checkbutton(window_top, text='SquirrelTemp', variable=status_SquirrelTemp)
local_SquirrelTemp.place(x=0, y=62, width=90, height=15, anchor='nw')

local_Package_Cache = Checkbutton(window_top, text='PackCache', variable=status_Package_Cache)
local_Package_Cache.place(x=90, y=62, width=85, height=15, anchor='nw')

local_Packages = Checkbutton(window_top, text='Packages', variable=status_Packages)
local_Packages.place(x=170, y=62, width=75, height=15, anchor='nw')

local_LocalLow = Checkbutton(window_top, text='LocalLow', variable=status_LocalLow)
local_LocalLow.place(x=240, y=62, width=90, height=15, anchor='nw')

roaming_Protect = Checkbutton(window_top, text='Protect', variable=status_m_Protect)
roaming_Protect.place(x=330, y=62, width=60, height=15, anchor='nw')

roaming_Proof = Checkbutton(window_top, text='Proof', variable=status_Proof)
roaming_Proof.place(x=0, y=82, width=60, height=15, anchor='nw')

clear_log = Checkbutton(window_top, text='Удалить логи', variable=status_clear_log)
clear_log.place(x=2, y=110, width=90, height=15, anchor='nw')

blockhosts = Checkbutton(window_top, text='Внести изминения в файл hosts', variable=status_bloskhosts)
blockhosts.place(x=2, y=130, width=250, height=15, anchor='nw')


btn = Button(window_top, text='Клик', fg='red', command=cleaning)
btn.place(x=295, y=155, width=60, height=18, anchor='nw')


root.mainloop()

