#archinstall
import sys
args = sys.argv
options = [[args[i],args[i+1]] for i in range(1,len(args),2)]
for option in options:
	match option:
		case ["g", gfx]:
			if gfx == "n": gfx_driver = "Nvidia";
			elif gfx == "i": gfx_driver = "Intel (open-source)";
			elif gfx == "a": gfx_driver = "AMD / ATI (open-source)"; 
			elif gfx == "o": gfx_driver = "All open-source (default)";
			else:
				print("choose graphics: n[vidia], a[md], o[pen-source = most compatible]")
				exit()
		case ["h", hostname]:
			if hostname == "":
				print("choose hostname eg: arch")
				exit()
		case ["k", keyboard_language]:
			if keyboard_language == "":
				print("choose keyboard_language eg: us")
				exit()
		case ["u", username]:
			if username == "":
				print("choose username")
				exit()
		case ["p", passwd]:
			if passwd == "":
				print("choose password")
				exit()
		case ["s", system]:
			sys_encoding, sys_language = system.split(".")
			if sys_encoding == "" or sys_language == "":
				print("choose language eg: en_US.utf-8")
				exit()
		case ["t", timezone]:
			if timezone == "":
				print("choose timezone eg: Europe/Zurich, posix/CET")
				exit()
		case _:
			print("'python archjson.py g o h arch k us d wm u s p arch s en_US.utf-8 t Europe/Zurich'")
			exit()
#print configuration
print("\n{}".join(["\t--- configuration ---",gfx_driver.replace("(default)",""),hostname,keyboard_language,username,passwd,sys_encoding,sys_language,timezone]).format("gfx-driver\t\t","hostname\t\t","keyboard_language\t","username\t\t","password\t\t","sys-encoding\t\t","sys-language\t\t","timezone\t\t"))
json = '''
{{
    "audio": "pipewire",
    "bootloader": "systemd-bootctl",
    "custom-commands": [
        "cd /home/{}; git clone https://aur.archlinux.org/paru.git",
        "chown -R {}:{} /home/{}/paru",
        "usermod -aG docker {}",
        "echo 'exec awesome' >> /home/{}/.xinitrc",
		"git clone https://github.com/zmaske/arch ~/arch",
        "sh ~/arch/zsh.sh {}"
    ],
    "filesystem": "ext4",
    "gfx-driver": "{}",
    "harddrive": {{
        "path": "/dev/sda"
    }},
    "hostname": "{}",
    "kernels": [
        "linux-zen"
    ],
    "keyboard_language": "{}",
	"mirror-region": "Worldwide",
    "nic": {{
        "NetworkManager": true
    }},
    "ntp": true,
    "packages": ["docker", "git", "wget", "zsh", "vim", "neofetch", "htop", "openssh", "powerline", "powerline-fonts"],
    "profile": "awesome",
    "services": ["docker"],
    "superusers": {{
        "{}": {{
            "!password": "{}"
        }}
    }},
    "sys-encoding": "{}",
    "sys-language": "{}",
    "timezone": "{}",
    "users": {{}}
}}
'''.format(username,username,username,username,username,username,username,\
	gfx_driver,hostname,keyboard_language,username,passwd,sys_encoding,sys_language,timezone)

archjson = open("arch.json", "w", newline='')
archjson.write(json[1:-1])
archjson.close()