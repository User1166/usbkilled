
def izin_verilen():
    import os
    commands = "start color c && echo izin verilen cihaz"
    os.system(commands)

def cikarildi():
    import os
    commands = "start color a && echo cikarildi"
    os.system(commands)


def eklendi():
    import os
    commands = "start color b && echo takıldı,eklendi"
    os.system(commands)
