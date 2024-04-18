from urllib.parse import urlparse
from termcolor import colored
from datetime import datetime
import socket
import requests
import subprocess
import time

subprocess.run(["clear"])

rat_color = "white"

path_color = "red"

now = datetime.now()

print("""
RatPath v 1.0 beta (https://github.com/deneuv) 
AVAILABLE TARGETS:
 Can force IPS,Domains,URLS..etc
 Ex: 190.199.1.2, example.com , https://example.com/example?id=12
METHODS:
 Be creative, works with Id's,param's,Path's, etc..
 Ex: &cd=10 , &id=1 , path/50 , &param=500 , etc..
INFORMATION:
 can return the content, server name, file type, whether the page is empty, 
 response size, etc..
""")

print(colored( "                                                        ","green") + colored("d8b",f"{path_color}"))
print(colored( "                      d8P",f"{rat_color}") + colored("                         d8P   ?88",f"{path_color}"))
print(colored( "                   d888888P",f"{rat_color}") + colored("                    d888888P  88b",f"{path_color}"))
print(colored( "  88bd88b d888b8b    ?88'",f"{rat_color}") + colored("  ?88,.d88b, d888b8b    ?88'    888888b  ",f"{path_color}"))
print(colored( "  88P'  `d8P' ?88    88P ",f"{rat_color}") + colored("   `?88'  ?88d8P' ?88    88P     88P `?8b",f"{path_color}"))
print(colored( " d88     88b  ,88b   88b",f"{rat_color}") + colored('     88b  d8P88b  ,88b   88b    d88   88P',f"{path_color}"))
print(colored( "d88'     `?88P'`88b  `?8b",f"{rat_color}") + colored("    888888P'`?88P'`88b  `?8b  d88'   88b",f"{path_color}") + colored ("  v 1.0 Beta","green"))
print(colored( "                             ","green") + colored("88P'                                ",f"{path_color}"))
print(colored( "                             ","green") + colored("?8P'                                ",f"{path_color}"))
print()
illegal = colored("illegal","yellow")
print(colored("[!]","red")+colored(f" legal opinion: We do not recommend using RatPath for {illegal} purposes,\n we are not responsible for anything you do :)","white"))


started_time = now.strftime(colored("%H:%M:%S","blue"))
print(colored("\n[~]","blue")+colored(f" started at: ({started_time})\n","white"))


target = str(input(colored("[+]","blue")+colored(" target:","white")))

param = str(input(colored("\n[+]","blue")+colored(" param:","white")))

query = f"{target}{param}"

print(colored("saved query.","green"))

try:
   init_range = int(input(colored("\n[+]","blue")+colored(" Interval X:","white")))
   final_range = int(input(colored("[+]","blue")+colored(" Interval Y:","white")))
except Exception:
   print(colored("Something wrong , please try again.","yellow"))

print(colored("starting..","blue"))
time.sleep(1)


for line in range(init_range,final_range):
    query_format = f"{target}{param}{line}"
    parsed_url = urlparse(query_format)
    host = parsed_url.netloc
    status = requests.get(query_format)
    body = len(status.content)
    content_type = status.headers.get('Content-Type')
    server = requests.head(query_format)
    server_name = server.headers.get('Server')
    ip_address = socket.gethostbyname(host)
    print(colored(f"""Results for ""","yellow")+f"""{target}{param}{line}
    Internet Protocol:{ip_address}
    Host:{host}
    Server:{server_name}
    Content Type:{content_type}
    Status code: <status:{status.status_code}>
    Body size:{body}
    """)




