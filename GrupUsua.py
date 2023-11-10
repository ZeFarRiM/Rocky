nomusu=input("Nombre del usuario: ")
nomgru=input("Nombre del grupo:   ")
import os
os.system('useradd '+nomusu)
os.system('smbpasswd -a '+nomusu)
os.system('usermod -g '+nomgru+' '+nomusu)
os.system('systemctl restart smb nmb')
