import paramiko
import time
from rich.console import Console
from rich.text import Text
console = Console()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting........")
ssh_client.connect(hostname="127.0.0.1",port=22,
			username="sachin",password="1234")
stdin,stdout,stderr = ssh_client.exec_command("free -m\n")
console.print(Text("free memory :",style="bold red"))
console.print(Text(stdout.read().decode(),style="bold blue"))
time.sleep(2)
stdin,stdout,stderr = ssh_client.exec_command("uptime  | grep -o 'load.*'\n")
console.print(Text("load average :",style="bold red"))
console.print(Text(stdout.read().decode(),style="bold blue"))
time.sleep(2)
stdin,stdout,stderr = ssh_client.exec_command("ip route list\n")
console.print(Text("routing table:",style="bold red"))
console.print(Text(stdout.read().decode(),style="bold blue"))
time.sleep(2)
stdin,stdout,stderr = ssh_client.exec_command("uptime -s\n")
console.print(Text("uptime:",style="bold red"))
console.print(Text(stdout.read().decode(),style="bold blue"))
time.sleep(2)

if ssh_client.get_transport().is_active() == True:
	print("Disconnecting.........")
	ssh_client.close()