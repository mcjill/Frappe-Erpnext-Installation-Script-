# 🚀 ERPNext Installation Script 🛠️

- 👋 Hi, I'm Elliot Brenya Sarfo!
- 📧 Email: elliotbrenyasarfo@gmail.com
- 🔗 LinkedIn: https://www.linkedin.com/in/elliot-brenya-sarfo/
- 🐦 Twitter: https://x.com/elliot_mlaidv

This script automates the installation of Frappe-ERPNext Version 15 on Ubuntu 22.04 LTS. It ensures all dependencies are installed, configures the necessary services, and sets up ERPNext with specified versions of Node.js, npm, and yarn.

## 📋 Prerequisites

- Ubuntu 22.04 LTS
- Sudo privileges

## 🌟 Script Features

- 🔄 Updates and upgrades system packages
- 📦 Installs necessary packages (git, Python, MariaDB, Redis, curl, etc.)
- 🗄️ Configures MariaDB
- 📥 Installs specific versions of Node.js, npm, and yarn
- 🖨️ Installs wkhtmltopdf
- 🛠️ Installs and sets up frappe-bench
- 🌐 Creates a new ERPNext site
- 🔒 Configures system permissions

## 💻 Installation

1. Clone the repository or download the script
   ```bash
     git clone https://github.com/mcjill/Frappe-Erpnext-Installation-Script-.git
     cd Frappe-Erpnext-Installation-Script-
   ```

2. Make the script executable
   ```bash
   chmod +x install_erpnext.py
   ```

3. Run the script with sudo
   ```bash
   sudo ./install_erpnext.py
   ```

## 🚀 Usage

1. 🖥️ The script will prompt you to enter the site name (e.g., `example.com`). Enter the desired site name.
2. 🔧 The script will automatically:
   - Update and upgrade system packages
   - Install necessary packages
   - Configure MariaDB
   - Remove any existing Node.js installation
   - Install Node.js v18.20.3, npm v10.7.0, and yarn v1.22.22
   - Install wkhtmltopdf
   - Install frappe-bench
   - Initialize frappe bench
   - Create a new site
   - Install ERPNext on the new site
   - Use the new site
   - Set the necessary permissions
3. 🏁 After the script completes, you can start the ERPNext server using:
   ```bash
   cd ~/frappe-bench
   chmod o+rx /home/user_name
   bench start
   ```

## ⚠️ Important Notes

- Ensure the script is run with sudo privileges
- The script prompts for the site name and MySQL root password during execution
- You may need to logout and log back in for all changes to take effect

## 🔧 Troubleshooting

- If you encounter any errors during the script execution, please refer to the error messages for troubleshooting
- Make sure to follow the prompts correctly, especially for the MySQL root password configuration

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 🙏 Acknowledgements

- ERPNext Team
- Frappe Framework

---
