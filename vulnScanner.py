import portScan
import termcolor

target_IP = input(termcolor.colored('[+] Enter Target IP Address / Name: ', 'blue'))
port_numbers = int(input(termcolor.colored('[+] Enter Number Of Ports (100 for first 100 ports): ', 'blue')))
vuln_file = input(termcolor.colored('[+] Enter Path To The File With Vulnerable Softwares: ', 'blue'))
print('\n')

target = portScan.PortScan(target_IP, port_numbers)
target.scan()

with open(vuln_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print(termcolor.colored('[!!] VULNERABLE BANNER: ', 'green') + banner + termcolor.colored(' ON PORT: ', 'green') + str(target.open_ports[count]))
        count += 1