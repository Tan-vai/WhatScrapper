import platform
import subprocess
from colorama import Fore, Style

# Perform a git pull
try:
    subprocess.run(['git', 'pull'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"{Fore.RED}[{Fore.GREEN}●{Fore.RED}]{Fore.GREEN} Checking For Updates...{Style.RESET_ALL}")
except subprocess.CalledProcessError as e:
    print(f"{Fore.RED}[{Fore.YELLOW}!{Fore.RED}]{Fore.YELLOW} Failed to fetch updates: {e}{Style.RESET_ALL}")

# Check system architecture
bit = platform.architecture()[0]
if bit == '64bit':
    print(f"{Fore.RED}[{Fore.GREEN}●{Fore.RED}]{Fore.GREEN} 64Bit Found{Style.RESET_ALL}")
    try:
        import whatscrapper
    except ImportError as e:
        print(f"{Fore.RED}[{Fore.YELLOW}!{Fore.RED}]{Fore.YELLOW} Failed to load whatscrapper module: {e}{Style.RESET_ALL}")
