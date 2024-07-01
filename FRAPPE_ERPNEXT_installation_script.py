import os
import subprocess
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

def run_command(command, shell=True, env=None, as_user=None):
    try:
        if as_user:
            command = f"sudo -H -u {as_user} bash -c '{command}'"
        subprocess.run(command, shell=shell, check=True, env=env)
    except subprocess.CalledProcessError as e:
        print_colored(f"Error executing command: {e}", Fore.RED)
        sys.exit(1)

def prompt_user(message):
    return input(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")

def get_sudo_user():
    return os.environ.get('SUDO_USER')

def main():
    print_colored("Elliot Brenya Sarfo Frappe-ERPNext V15 Installation Script", Fore.GREEN)
    print_colored("========================================", Fore.GREEN)

    # Ensure script is run with sudo
    if os.geteuid() != 0:
        print_colored("This script must be run with sudo privileges. Please run it again with sudo.", Fore.RED)
        sys.exit(1)

    sudo_user = get_sudo_user()
    if not sudo_user:
        print_colored("Unable to determine the sudo user. Please run this script using sudo.", Fore.RED)
        sys.exit(1)

    # Update and upgrade system
    print_colored("\nUpdating and upgrading system packages", Fore.CYAN)
    run_command("apt update && apt upgrade -y")

    # Install necessary packages
    print_colored("\nInstalling necessary packages", Fore.CYAN)
    run_command("apt-get install -y git python3-dev python3-setuptools python3-pip python3.11-venv software-properties-common mariadb-server libmysqlclient-dev redis-server curl")

    # Configure MariaDB
    print_colored("\nConfiguring MariaDB", Fore.CYAN)
    run_command("mysql_secure_installation")

    # Edit MariaDB configuration
    print_colored("\nEditing MariaDB configuration", Fore.CYAN)
    config = """
[server]
user = mysql
pid-file = /run/mysqld/mysqld.pid
socket = /run/mysqld/mysqld.sock
basedir = /usr
datadir = /var/lib/mysql
tmpdir = /tmp
lc-messages-dir = /usr/share/mysql
bind-address = 127.0.0.1
query_cache_size = 16M
log_error = /var/log/mysql/error.log

[mysqld]
innodb-file-format=barracuda
innodb-file-per-table=1
innodb-large-prefix=1
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci      
 
[mysql]
default-character-set = utf8mb4
"""
    with open("/etc/mysql/mariadb.conf.d/50-server.cnf", "w") as f:
        f.write(config)
    run_command("service mysql restart")

    # Remove existing Node.js if installed
    print_colored("\nRemoving existing Node.js (if any)", Fore.CYAN)
    run_command("apt-get remove -y nodejs")

    # Install Node.js and Yarn
    print_colored("\nInstalling Node.js and Yarn", Fore.CYAN)
    run_command("curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -")
    run_command("apt-get install -y nodejs")

    # Install wkhtmltopdf
    print_colored("\nInstalling wkhtmltopdf", Fore.CYAN)
    run_command("apt-get install -y xvfb libfontconfig wkhtmltopdf")

    # Install frappe-bench
    print_colored("\nInstalling frappe-bench", Fore.CYAN)
    run_command("pip3 install frappe-bench")

    # Initialize frappe bench
    print_colored("\nInitializing frappe bench", Fore.CYAN)
    home_dir = os.path.expanduser(f'~{sudo_user}')
    os.chdir(home_dir)
    bench_init = f'export PATH="$HOME/.nvm/versions/node/v18.20.3/bin:$PATH" && bench init frappe-bench --frappe-branch version-15 --python python3.11'
    run_command(bench_init, as_user=sudo_user)

    # Change to frappe-bench directory
    os.chdir(f"{home_dir}/frappe-bench")

    # Create a new site
    print_colored("\nCreating a new site", Fore.CYAN)
    site_name = prompt_user("Enter the site name (e.g., example.com): ")
    run_command(f'export PATH="$HOME/.nvm/versions/node/v18.20.3/bin:$PATH" && bench new-site {site_name}', as_user=sudo_user)
    run_command(f"bench --site {site_name} add-to-hosts")

    # Install ERPNext
    print_colored("\nInstalling ERPNext", Fore.CYAN)
    run_command('export PATH="$HOME/.nvm/versions/node/v18.20.3/bin:$PATH" && bench get-app erpnext --branch version-15', as_user=sudo_user)
    run_command(f'export PATH="$HOME/.nvm/versions/node/v18.20.3/bin:$PATH" && bench --site {site_name} install-app erpnext', as_user=sudo_user)

    # Use the new site
    print_colored("\nUsing the new site", Fore.CYAN)
    run_command(f'bench use {site_name}', as_user=sudo_user)

    # Set permissions
    print_colored("\nSetting permissions", Fore.CYAN)
    run_command(f'chmod o+rx /home/{sudo_user}')

    print_colored("\nInstallation complete! You can now run 'bench start' to start the server.", Fore.GREEN)
    print_colored("Please note: You may need to logout and log back in for all changes to take effect.", Fore.YELLOW)

if __name__ == "__main__":
    main()
