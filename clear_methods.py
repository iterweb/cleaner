import shutil
import os

import hosts


user_name = os.getlogin()


recycle_bin = r'c:\$Recycle.Bin'
Proof = r'c:\Users\%s\AppData\Roaming\Microsoft\Proof' % user_name
m_Protect = r'c:\Users\%s\AppData\Roaming\Microsoft\Protect' % user_name
LocalLow = r'c:\Users\%s\AppData\LocalLow\Microsoft' % user_name
Packages = r'c:\Users\%s\AppData\Local\Packages' % user_name
Package_Cache = r'c:\Users\%s\AppData\Local\Package Cache' % user_name
SquirrelTemp = r'c:\Users\%s\AppData\Local\SquirrelTemp' % user_name
ElevatedDiagnostics = r'c:\Users\%s\AppData\Local\ElevatedDiagnostics' % user_name
D3DSCache = r'c:\Users\%s\AppData\Local\D3DSCache' % user_name
loc_crashdamps = r'c:\Users\%s\AppData\Local\CrashDumps' % user_name
microsoft = r'c:\Users\%s\AppData\Local\Microsoft' % user_name
mirs_windows = r'c:\Users\%s\AppData\Local\Microsoft\Windows' % user_name
win_history = r'c:\Users\%s\AppData\Local\Microsoft\Windows\History' % user_name
win_wer = r'c:\Users\%s\AppData\Local\Microsoft\Windows\WER' % user_name
win_caches = r'c:\Users\%s\AppData\Local\Microsoft\Windows\Caches' % user_name
local_temp = r'c:\Users\%s\AppData\Local\Temp' % user_name
win_temp = r'c:\Windows\Temp'
recent = r'c:\Users\%s\AppData\Roaming\Microsoft\Windows\Recent' % user_name
cookie = r'c:\Users\%s\AppData\Roaming\Microsoft\Windows\Cookies' % user_name


def clear_cookies():
    if os.path.exists(cookie) == True:
        print('ОЧИСТКА: папки Cookies\n%s' % cookie)
        shutil.rmtree(cookie, ignore_errors=True)
    else:
        print('ОШИБКА!\nПапка Cookies НЕ найдена!!!')


def clear_recent():
    if os.path.exists(recent) == True:
        print('ОЧИСТКА: папки Recent\n%s ' % recent)
        shutil.rmtree(recent, ignore_errors=True)
    else:
        print('ОШИБКА!\nПапка Recent НЕ найдена!!!')


def clear_win_temp():
    if os.path.exists(win_temp) == True:
        print('ОЧИСТКА: папки Windows Temp\n%s' % win_temp)
        shutil.rmtree(win_temp, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Windows Temp НЕ найдена!!!')


def clear_local_temp():
    if os.path.exists(local_temp) == True:
        print('ОЧИСТКА: папки Local Temp\n%s' % local_temp)
        shutil.rmtree(local_temp, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Local Temp НЕ найдена!!!')


def clear_win_caches():
    if os.path.exists(win_caches) == True:
        print('ОЧИСТКА: папки Windows Caches\n%s' % win_caches)
        shutil.rmtree(win_caches, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Windows Caches НЕ найдена!!!')


def clear_win_wer():
    if os.path.exists(win_wer) == True:
        print('ОЧИСТКА: папки Windows WER\n%s' % win_wer)
        shutil.rmtree(win_wer, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Windows WER НЕ найдена!!!')


def clear_win_history():
    if os.path.exists(win_history) == True:
        print('ОЧИСТКА: папки Windows History\n%s' % win_history)
        shutil.rmtree(win_history, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Windows History НЕ найдена!!!')


def clear_mirs_windows():
    if os.path.exists(mirs_windows) == True:
        print('ОЧИСТКА: папки Microsoft Windows\n%s' % mirs_windows)
        shutil.rmtree(mirs_windows, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Microsoft Windows НЕ найдена!!!')


def clear_microsoft():
    if os.path.exists(microsoft) == True:
        print('ОЧИСТКА: папки Microsoft\n%s' % microsoft)
        shutil.rmtree(microsoft, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Microsoft НЕ найдена!!!')


def clear_loc_crashdamps():
    if os.path.exists(loc_crashdamps) == True:
        print('ОЧИСТКА: папки CrashDumps\n%s' % loc_crashdamps)
        shutil.rmtree(loc_crashdamps, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория CrashDumps НЕ найдена!!!')


def clear_d3dscache():
    if os.path.exists(D3DSCache) == True:
        print('ОЧИСТКА: папки D3DSCache\n%s' % D3DSCache)
        shutil.rmtree(D3DSCache, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория D3DSCache НЕ найдена!!!')


def clear_elevated_diagnostics():
    if os.path.exists(ElevatedDiagnostics) == True:
        print('ОЧИСТКА: папки ElevatedDiagnostics\n%s' % ElevatedDiagnostics)
        shutil.rmtree(ElevatedDiagnostics, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория ElevatedDiagnostics НЕ найдена!!!')


def clear_squirreltemp():
    if os.path.exists(SquirrelTemp) == True:
        print('ОЧИСТКА: папки SquirrelTemp\n%s' % SquirrelTemp)
        shutil.rmtree(SquirrelTemp, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория SquirrelTemp НЕ найдена!!!')


def clear_package_cache():
    if os.path.exists(Package_Cache) == True:
        print('ОЧИСТКА: папки Package Cache\n%s' % Package_Cache)
        shutil.rmtree(Package_Cache, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Package Cache НЕ найдена!!!')


def clear_packages():
    if os.path.exists(Packages) == True:
        print('ОЧИСТКА: папки Packages\n%s' % Packages)
        shutil.rmtree(Packages, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Packages НЕ найдена!!!')


def clear_locallow():
    if os.path.exists(LocalLow) == True:
        print('ОЧИСТКА: папки LocalLow\n%s' % LocalLow)
        shutil.rmtree(LocalLow, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория LocalLow НЕ найдена!!!')


def clear_m_protect():
    if os.path.exists(m_Protect) == True:
        print('ОЧИСТКА: папки Protect\n%s' % m_Protect)
        shutil.rmtree(m_Protect, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Protect НЕ найдена!!!')


def clear_proof():
    if os.path.exists(Proof) == True:
        print('ОЧИСТКА: папки Proof\n%s' % Proof)
        shutil.rmtree(Proof, ignore_errors=True)
    else:
        print('ОШИБКА!\nДиректория Proof НЕ найдена!!!')


def clear_all_logs():
    events = []
    os.system('wevtutil el > events.txt')
    with open('events.txt') as file:
        for l in file.readlines():
            events.append('"%s"' % l.replace("\n", ''))
        for event in events:
            print(event)
            os.system('wevtutil cl %s' % event)


def add_block_hosts():
    for host in hosts.hosts_list:
        f = open('C:\Windows\System32\drivers\etc\hosts', 'a')
        print(host)
        f.write(host + '\n')
        f.close


def clear_recycle_bin():
    print('ОЧИСТКА: Корзины\n%s' % recycle_bin)
    shutil.rmtree(recycle_bin, ignore_errors=True)