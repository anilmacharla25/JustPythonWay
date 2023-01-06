import subprocess

def is_screen_locked():
    result = subprocess.run(["dbus-send", "--type=method_call", "--print-reply", "--dest=org.gnome.ScreenSaver", "/org/gnome/ScreenSaver", "org.gnome.ScreenSaver.GetActive"], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8").strip() == "method return time=0 boolean true"
