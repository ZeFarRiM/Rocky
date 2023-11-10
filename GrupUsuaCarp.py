nomusu=input("Nombre del usuario: ")
nomgru=input("Nombre del grupo:   ")
nomcar=input("Nombre de carpeta:  ")
import os
os.system('useradd '+nomusu)
os.system('smbpasswd -a '+nomusu)
os.system('groupadd '+nomgru)
os.system('usermod -g '+nomgru+' '+nomusu)
os.system('mkdir -p /home/'+nomcar)
os.system('chmod -R 770 /home/'+nomcar)
os.system('chcon -t samba_share_t /home/'+nomcar)
os.system('chown -R root:'+nomgru+' /home/'+nomcar)
os.system('systemctl restart smb nmb')

