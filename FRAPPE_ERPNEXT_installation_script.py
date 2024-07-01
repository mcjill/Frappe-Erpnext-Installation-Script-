elliot@frappe:~/frappe-bench$ 
elliot@frappe:~/frappe-bench$ 
elliot@frappe:~/frappe-bench$ cd ..
elliot@frappe:~$ rm -rf install_erpnext.py 
elliot@frappe:~$ rm -rf frappe-bench 
elliot@frappe:~$ nano install_erpnext.py
elliot@frappe:~$ chmod o+rx /home/elliot/
elliot@frappe:~$ sudo ./install_erpnext.py
sudo: ./install_erpnext.py: command not found
elliot@frappe:~$ ls
install_erpnext.py
elliot@frappe:~$ sudo ./install_erpnext.py
sudo: ./install_erpnext.py: command not found
elliot@frappe:~$ chmod +x install_erpnext.py
elliot@frappe:~$ sudo ./install_erpnext.py
Elliot Brenya ERPNext Installation Script
========================================

Updating and upgrading system packages
Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                                 
Hit:2 https://deb.nodesource.com/node_18.x nodistro InRelease                                                                    
Hit:3 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease     
Hit:4 http://ca.archive.ubuntu.com/ubuntu jammy InRelease                    
Hit:5 http://ca.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:6 http://ca.archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
5 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
Get more security updates through Ubuntu Pro with 'esm-apps' enabled:
  redis-server redis-tools
Learn more about Ubuntu Pro at https://ubuntu.com/pro
The following packages have been kept back:
  python3-update-manager ubuntu-advantage-tools ubuntu-pro-client ubuntu-pro-client-l10n update-manager-core
0 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.

Installing necessary packages
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
redis-server is already the newest version (5:6.0.16-1ubuntu1).
curl is already the newest version (7.81.0-1ubuntu1.16).
git is already the newest version (1:2.34.1-1ubuntu1.11).
libmysqlclient-dev is already the newest version (8.0.37-0ubuntu0.22.04.3).
python3-dev is already the newest version (3.10.6-1~22.04).
python3-setuptools is already the newest version (59.6.0-1.2ubuntu0.22.04.1).
software-properties-common is already the newest version (0.99.22.9).
mariadb-server is already the newest version (1:10.6.18-0ubuntu0.22.04.1).
python3-pip is already the newest version (22.0.2+dfsg-1ubuntu0.4).
python3.11-venv is already the newest version (3.11.9-1+jammy1).
0 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.

Configuring MariaDB

NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!

In order to log into MariaDB to secure it, we'll need the current
password for the root user. If you've just installed MariaDB, and
haven't set the root password yet, you should just press enter here.

Enter current password for root (enter for none): 
OK, successfully used password, moving on...

Setting the root password or using the unix_socket ensures that nobody
can log into the MariaDB root user without the proper authorisation.

You already have your root account protected, so you can safely answer 'n'.

Switch to unix_socket authentication [Y/n] n
 ... skipping.

You already have your root account protected, so you can safely answer 'n'.

Change the root password? [Y/n] y
New password: 
Re-enter new password: 
Password updated successfully!
Reloading privilege tables..
 ... Success!


By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

Remove anonymous users? [Y/n] y
 ... Success!

Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

Disallow root login remotely? [Y/n] y
 ... Success!

By default, MariaDB comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.

Remove test database and access to it? [Y/n] y
 - Dropping test database...
 ... Success!
 - Removing privileges on test database...
 ... Success!

Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

Reload privilege tables now? [Y/n] y
 ... Success!

Cleaning up...

All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

Thanks for using MariaDB!

Editing MariaDB configuration

Removing existing Node.js (if any)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  nodejs
0 upgraded, 0 newly installed, 1 to remove and 5 not upgraded.
After this operation, 187 MB disk space will be freed.
(Reading database ... 111849 files and directories currently installed.)
Removing nodejs (18.20.3-1nodesource1) ...
dpkg: warning: while removing nodejs, directory '/usr/lib/node_modules' not empty so not removed
Processing triggers for man-db (2.10.2-1) ...

Installing Node.js and Yarn
2024-07-01 12:40:04 - Installing pre-requisites
Hit:1 http://ca.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://security.ubuntu.com/ubuntu jammy-security InRelease                                   
Hit:3 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease                       
Hit:4 https://deb.nodesource.com/node_18.x nodistro InRelease       
Hit:5 http://ca.archive.ubuntu.com/ubuntu jammy-updates InRelease   
Hit:6 http://ca.archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
ca-certificates is already the newest version (20230311ubuntu0.22.04.1).
curl is already the newest version (7.81.0-1ubuntu1.16).
gnupg is already the newest version (2.2.27-3ubuntu2.1).
apt-transport-https is already the newest version (2.4.12).
0 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.
Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:2 http://ca.archive.ubuntu.com/ubuntu jammy InRelease                                     
Hit:3 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease                  
Hit:4 https://deb.nodesource.com/node_18.x nodistro InRelease       
Hit:5 http://ca.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:6 http://ca.archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
2024-07-01 12:40:12 - Repository configured successfully. To install Node.js, run: apt-get install nodejs -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  nodejs
0 upgraded, 1 newly installed, 0 to remove and 5 not upgraded.
Need to get 0 B/29.6 MB of archives.
After this operation, 187 MB of additional disk space will be used.
Selecting previously unselected package nodejs.
(Reading database ... 106524 files and directories currently installed.)
Preparing to unpack .../nodejs_18.20.3-1nodesource1_amd64.deb ...
Unpacking nodejs (18.20.3-1nodesource1) ...
Setting up nodejs (18.20.3-1nodesource1) ...
Processing triggers for man-db (2.10.2-1) ...
Scanning processes...                                                                                                                                
Scanning candidates...                                                                                                                               
Scanning linux images...                                                                                                                             

Running kernel seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.

Installing wkhtmltopdf
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Note, selecting 'libfontconfig1' instead of 'libfontconfig'
libfontconfig1 is already the newest version (2.13.1-4.2ubuntu5).
wkhtmltopdf is already the newest version (0.12.6-2).
xvfb is already the newest version (2:21.1.4-2ubuntu1.7~22.04.10).
0 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.

Installing frappe-bench
Requirement already satisfied: frappe-bench in /usr/local/lib/python3.10/dist-packages (5.22.6)
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (from frappe-bench) (2.25.1)
Requirement already satisfied: honcho in /usr/local/lib/python3.10/dist-packages (from frappe-bench) (1.1.0)
Requirement already satisfied: click>=7.0 in /usr/lib/python3/dist-packages (from frappe-bench) (8.0.3)
Requirement already satisfied: jinja2~=3.1.3 in /usr/local/lib/python3.10/dist-packages (from frappe-bench) (3.1.4)
Requirement already satisfied: setuptools>40.9.0 in /usr/lib/python3/dist-packages (from frappe-bench) (59.6.0)
Requirement already satisfied: python-crontab~=2.6.0 in /usr/local/lib/python3.10/dist-packages (from frappe-bench) (2.6.0)
Requirement already satisfied: semantic-version~=2.8.2 in /usr/local/lib/python3.10/dist-packages (from frappe-bench) (2.8.5)
Requirement already satisfied: gitpython~=3.1.30 in /usr/local/lib/python3.10/dist-packages (from frappe-bench) (3.1.43)
Requirement already satisfied: tomli in /usr/local/lib/python3.10/dist-packages (from frappe-bench) (2.0.1)
Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython~=3.1.30->frappe-bench) (4.0.11)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/lib/python3/dist-packages (from jinja2~=3.1.3->frappe-bench) (2.0.1)
Requirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from python-crontab~=2.6.0->frappe-bench) (2.9.0.post0)
Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython~=3.1.30->frappe-bench) (5.0.1)
Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil->python-crontab~=2.6.0->frappe-bench) (1.16.0)
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

Initializing frappe bench
Setting Up Environment
$ python3.11 -m venv env
$ /home/elliot/frappe-bench/env/bin/python -m pip install --quiet --upgrade pip
$ /home/elliot/frappe-bench/env/bin/python -m pip install --quiet wheel
Getting frappe
$ git clone https://github.com/frappe/frappe.git --branch version-15 --depth 1 --origin upstream
Cloning into 'frappe'...
remote: Enumerating objects: 3308, done.
remote: Counting objects: 100% (3308/3308), done.
remote: Compressing objects: 100% (2976/2976), done.
remote: Total 3308 (delta 414), reused 1524 (delta 218), pack-reused 0
Receiving objects: 100% (3308/3308), 15.57 MiB | 7.73 MiB/s, done.
Resolving deltas: 100% (414/414), done.
Installing frappe
$ /home/elliot/frappe-bench/env/bin/python -m pip install --quiet --upgrade -e /home/elliot/frappe-bench/apps/frappe 
$ yarn install --check-files
yarn install v1.22.22
[1/5] Validating package.json...
[2/5] Resolving packages...
[3/5] Fetching packages...
[4/5] Linking dependencies...
warning " > @frappe/esbuild-plugin-postcss2@0.1.3" has unmet peer dependency "less@^4.x".
warning " > @frappe/esbuild-plugin-postcss2@0.1.3" has unmet peer dependency "stylus@^0.x".
warning " > @vue/component-compiler@4.2.4" has unmet peer dependency "vue-template-compiler@*".
[5/5] Building fresh packages...
Done in 44.95s.
Found existing apps updating states...
WARN: restart failed: Couldn't find supervisorctl in PATH
$ bench build
Assets for Release v15.32.0 don't exist
✔ Application Assets Linked                                                                                                                          


yarn run v1.22.22
$ node esbuild --production --run-build-command
Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
File                                                        Size

frappe/dist/js/
├─ bootstrap-4-web.bundle.FOZOVELL.js                       1.73 Kb
├─ controls.bundle.XSQTGDX4.js                              1234.55 Kb
├─ data_import_tools.bundle.GNL3BWOK.js                     126.56 Kb
├─ desk.bundle.5V6S656C.js                                  1345.72 Kb
├─ dialog.bundle.JUOABYOR.js                                57.42 Kb
├─ form.bundle.UL7I7KM2.js                                  167.77 Kb
├─ frappe-web.bundle.MTRV47AB.js                            829.37 Kb
├─ libs.bundle.TIV7ZGVY.js                                  556.25 Kb
├─ list.bundle.NZMQ2FRC.js                                  195.70 Kb
├─ logtypes.bundle.EKN7LWKW.js                              0.73 Kb
├─ onboarding_tours.bundle.RAUR6X4Z.js                      7.60 Kb
├─ report.bundle.3ULLPC5Z.js                                197.43 Kb
├─ sentry.bundle.IPS6PK2M.js                                69.50 Kb
├─ telemetry.bundle.LKEZCADB.js                             2.59 Kb
├─ user_profile_controller.bundle.ZJ6AYZ5P.js               11.96 Kb
├─ video_player.bundle.DUYYLSFO.js                          120.67 Kb
├─ web_form.bundle.LCRMGSTF.js                              1426.50 Kb
├─ form_builder.bundle.VYKGFDCA.js                          798.60 Kb
├─ form_builder.bundle.UEQAHLLT.css                         23.19 Kb
├─ print_format_builder.bundle.RPGO75WJ.js                  685.24 Kb
├─ print_format_builder.bundle.PLH6XRTA.css                 5.54 Kb
├─ workflow_builder.bundle.LX3Y753Z.js                      351.72 Kb
├─ workflow_builder.bundle.RVRKQCE6.css                     11.02 Kb
├─ build_events.bundle.M55W3UUG.js                          105.71 Kb
├─ build_events.bundle.QF22FNWB.css                         1.29 Kb
├─ file_uploader.bundle.FPCPQRTX.js                         201.83 Kb
├─ file_uploader.bundle.WGFSWD7S.css                        6.53 Kb
└─ kanban_board.bundle.AS3FI5GX.js                          578.14 Kb

frappe/dist/css/
├─ desk.bundle.R5N2TRGE.css                                 590.98 Kb
├─ email.bundle.TIWGDKWO.css                                5.97 Kb
├─ login.bundle.XJFTHEP2.css                                32.29 Kb
├─ print.bundle.UH3OFGMM.css                                203.33 Kb
├─ print_format.bundle.IFNFAM36.css                         186.11 Kb
├─ report.bundle.XIS6PUYI.css                               5.33 Kb
├─ web_form.bundle.YI2JDXDX.css                             14.69 Kb
└─ website.bundle.EHNFY2RX.css                              443.56 Kb

frappe/dist/css-rtl/
├─ desk.bundle.EPRZVTK5.css                                 591.49 Kb
├─ email.bundle.6LNUSB6I.css                                5.98 Kb
├─ login.bundle.WH7VMOZ6.css                                32.29 Kb
├─ print.bundle.YOU2HUR2.css                                203.49 Kb
├─ print_format.bundle.ILHRGMLA.css                         186.24 Kb
├─ report.bundle.3MZIYGGR.css                               5.33 Kb
├─ web_form.bundle.E5OOXY57.css                             14.68 Kb
└─ website.bundle.6Q6PEWG4.css                              443.72 Kb

 DONE  Total Build Time: 58.977s

 WARN  Cannot connect to redis_cache to update assets_json
 WARN  Cannot connect to redis_cache to update assets_json
 WARN  Cannot connect to redis_cache to update assets_json
Done in 62.52s.
Compiling translations for frappe
SUCCESS: Bench frappe-bench initialized

Creating a new site
Enter the site name (e.g., example.com): site.local 
MySQL root password: 

Installing frappe...
Updating DocTypes for frappe        : [========================================] 100%
Set Administrator password: 
Re-enter Administrator password: 
Updating Dashboard for frappe
site.local: SystemSettings.enable_scheduler is UNSET
*** Scheduler is disabled ***
[sudo] password for elliot: 
127.0.0.1 site.local

Installing ERPNext
Getting erpnext
$ git clone https://github.com/frappe/erpnext.git --branch version-15 --depth 1 --origin upstream
Cloning into 'erpnext'...
remote: Enumerating objects: 4731, done.
remote: Counting objects: 100% (4731/4731), done.
remote: Compressing objects: 100% (3988/3988), done.
remote: Total 4731 (delta 973), reused 2067 (delta 524), pack-reused 0
Receiving objects: 100% (4731/4731), 15.91 MiB | 5.91 MiB/s, done.
Resolving deltas: 100% (973/973), done.
Updating files: 100% (4431/4431), done.
Ignoring dependencies of erpnext. To install dependencies use --resolve-deps
Installing erpnext
$ /home/elliot/frappe-bench/env/bin/python -m pip install --quiet --upgrade -e /home/elliot/frappe-bench/apps/erpnext 
$ yarn install --check-files
yarn install v1.22.22
[1/4] Resolving packages...
[2/4] Fetching packages...
[3/4] Linking dependencies...
[4/4] Building fresh packages...
Done in 0.20s.
$ bench build --app erpnext
✔ Application Assets Linked                                                                                                                          


yarn run v1.22.22
$ node esbuild --production --apps erpnext --run-build-command
Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
File                                                        Size

erpnext/dist/js/
├─ bank-reconciliation-tool.bundle.ALGDCWUD.js              17.17 Kb
├─ erpnext-web.bundle.J4A2DQB4.js                           0.29 Kb
├─ erpnext.bundle.PX4LHVCU.js                               219.51 Kb
├─ item-dashboard.bundle.ERY5BPYC.js                        10.24 Kb
├─ point-of-sale.bundle.WJIIJGKH.js                         92.63 Kb
└─ bom_configurator.bundle.D2UVDA3I.js                      8.63 Kb

erpnext/dist/css/
├─ erpnext-web.bundle.XOZZFNTP.css                          2.86 Kb
├─ erpnext.bundle.WX3S5RTE.css                              44.14 Kb
└─ erpnext_email.bundle.JFOFQZVI.css                        0.56 Kb

erpnext/dist/css-rtl/
├─ erpnext-web.bundle.EJFG5KEE.css                          2.87 Kb
├─ erpnext.bundle.WVNS7L7O.css                              44.13 Kb
└─ erpnext_email.bundle.QCRMFBPJ.css                        0.56 Kb

 DONE  Total Build Time: 2.811s

 WARN  Cannot connect to redis_cache to update assets_json
 WARN  Cannot connect to redis_cache to update assets_json
 WARN  Cannot connect to redis_cache to update assets_json
Done in 5.65s.
Compiling translations for erpnext
WARN: restart failed: Couldn't find supervisorctl in PATH

Installing erpnext...
Updating DocTypes for erpnext       : [========================================] 100%
Updating customizations for Address
Updating customizations for Contact
Updating Dashboard for erpnext

Using the new site
Current Site set to site.local

Setting permissions

Installation complete! You can now run 'bench start' to start the server.
Please note: You may need to logout and log back in for all changes to take effect.
elliot@frappe:~$ cd frappe-bench 
elliot@frappe:~/frappe-bench$ bench start 
12:48:34 system        | redis_cache.1 started (pid=37169)
12:48:34 system        | web.1 started (pid=37173)
12:48:34 system        | watch.1 started (pid=37179)
12:48:34 system        | redis_queue.1 started (pid=37174)
12:48:34 redis_queue.1 | 37181:C 01 Jul 2024 12:48:34.771 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
12:48:34 redis_cache.1 | 37171:C 01 Jul 2024 12:48:34.771 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
12:48:34 redis_cache.1 | 37171:C 01 Jul 2024 12:48:34.771 # Redis version=6.0.16, bits=64, commit=00000000, modified=0, pid=37171, just started
12:48:34 redis_cache.1 | 37171:C 01 Jul 2024 12:48:34.771 # Configuration loaded
12:48:34 redis_queue.1 | 37181:C 01 Jul 2024 12:48:34.771 # Redis version=6.0.16, bits=64, commit=00000000, modified=0, pid=37181, just started
12:48:34 redis_queue.1 | 37181:C 01 Jul 2024 12:48:34.771 # Configuration loaded
12:48:34 redis_cache.1 | 37171:M 01 Jul 2024 12:48:34.773 * Increased maximum number of open files to 10032 (it was originally set to 1024).
12:48:34 redis_queue.1 | 37181:M 01 Jul 2024 12:48:34.773 * Increased maximum number of open files to 10032 (it was originally set to 1024).
12:48:34 system        | worker.1 started (pid=37180)
12:48:34 system        | schedule.1 started (pid=37188)
12:48:34 redis_cache.1 | 37171:M 01 Jul 2024 12:48:34.792 * Running mode=standalone, port=13000.
12:48:34 redis_queue.1 | 37181:M 01 Jul 2024 12:48:34.792 * Running mode=standalone, port=11000.
12:48:34 redis_cache.1 | 37171:M 01 Jul 2024 12:48:34.795 # Server initialized
12:48:34 redis_queue.1 | 37181:M 01 Jul 2024 12:48:34.796 # Server initialized
12:48:34 redis_cache.1 | 37171:M 01 Jul 2024 12:48:34.796 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
12:48:34 redis_queue.1 | 37181:M 01 Jul 2024 12:48:34.797 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
12:48:34 redis_queue.1 | 37181:M 01 Jul 2024 12:48:34.803 * Ready to accept connections
12:48:34 redis_cache.1 | 37171:M 01 Jul 2024 12:48:34.804 * Ready to accept connections
12:48:34 system        | socketio.1 started (pid=37187)
12:48:35 watch.1       | 
12:48:36 socketio.1    | Realtime service listening on:  9000
12:48:36 web.1         | /home/elliot/frappe-bench/env/lib/python3.11/site-packages/passlib/utils/__init__.py:854: DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13
12:48:36 web.1         |   from crypt import crypt as _crypt
12:48:36 web.1         | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
12:48:36 web.1         |  * Running on all addresses (0.0.0.0)
12:48:36 web.1         |  * Running on http://127.0.0.1:8000
12:48:36 web.1         |  * Running on http://10.10.60.29:8000
12:48:36 web.1         | Press CTRL+C to quit
12:48:36 web.1         |  * Restarting with stat
12:48:37 watch.1       | yarn run v1.22.22
12:48:37 watch.1       | $ node esbuild --watch --live-reload
12:48:38 web.1         | /home/elliot/frappe-bench/env/lib/python3.11/site-packages/passlib/utils/__init__.py:854: DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13
12:48:38 web.1         |   from crypt import crypt as _crypt
12:48:38 web.1         |  * Debugger is active!
12:48:38 web.1         |  * Debugger PIN: 137-861-188
12:48:47 watch.1       | Browserslist: caniuse-lite is outdated. Please run:
12:48:47 watch.1       |   npx update-browserslist-db@latest
12:48:47 watch.1       |   Why you should do it regularly: https://github.com/browserslist/update-db#readme
12:49:15 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:15] "GET / HTTP/1.1" 200 -
12:49:16 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:16] "GET /assets/erpnext/dist/css/erpnext-web.bundle.XOZZFNTP.css HTTP/1.1" 200 -
12:49:16 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:16] "GET /assets/frappe/dist/css/website.bundle.EHNFY2RX.css HTTP/1.1" 200 -
12:49:16 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:16] "GET /assets/frappe/dist/css/login.bundle.XJFTHEP2.css HTTP/1.1" 200 -
12:49:17 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:17] "GET /website_script.js HTTP/1.1" 200 -
12:49:18 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:18] "GET /assets/erpnext/images/erpnext-favicon.svg HTTP/1.1" 200 -
12:49:28 web.1         | /home/elliot/frappe-bench/env/lib/python3.11/site-packages/werkzeug/wrappers/request.py:190: DeprecationWarning: login: Sending `cmd` for RPC calls is deprecated, call REST API instead `/api/method/cmd`
12:49:28 web.1         |   resp = f(*args[:-2] + (request,))
12:49:28 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:28] "POST /login HTTP/1.1" 200 -
12:49:44 watch.1       | Watching for changes...
12:49:50 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:50] "GET /app HTTP/1.1" 200 -
12:49:50 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:50] "GET /assets/frappe/icons/timeless/icons.svg?v=1719838185.584056 HTTP/1.1" 200 -
12:49:50 web.1         | 10.10.60.10 - - [01/Jul/2024 12:49:50] "GET /assets/frappe/icons/espresso/icons.svg?v=1719838185.584056 HTTP/1.1" 200 -
12:50:01 web.1         | 10.10.60.10 - - [01/Jul/2024 12:50:01] "GET /assets/frappe/dist/css/report.bundle.XIS6PUYI.css HTTP/1.1" 404 -
12:50:02 web.1         | 10.10.60.10 - - [01/Jul/2024 12:50:02] "GET /assets/erpnext/dist/css/erpnext.bundle.WX3S5RTE.css HTTP/1.1" 404 -
12:50:02 web.1         | 10.10.60.10 - - [01/Jul/2024 12:50:02] "GET /assets/frappe/dist/css/desk.bundle.R5N2TRGE.css HTTP/1.1" 404 -
12:50:02 web.1         | 10.10.60.10 - - [01/Jul/2024 12:50:02] "GET /assets/frappe/dist/js/form.bundle.UL7I7KM2.js HTTP/1.1" 404 -
12:50:03 web.1         | 10.10.60.10 - - [01/Jul/2024 12:50:03] "GET /assets/erpnext/js/setup_wizard.js?v=1719838200665 HTTP/1.1" 200 -
12:50:03 web.1         | 10.10.60.10 - - [01/Jul/2024 12:50:03] "POST /api/method/frappe.desk.page.setup_wizard.setup_wizard.load_languages HTTP/1.1" 200 -
12:50:03 web.1         | 10.10.60.10 - - [01/Jul/2024 12:50:03] "POST /api/method/frappe.geo.country_info.get_country_timezone_info HTTP/1.1" 200 -
12:50:05 web.1         | 10.10.60.10 - - [01/Jul/2024 12:50:05] "GET /api/method/frappe.desk.form.load.getdoc?doctype=Currency&name=GHS&_=1719838199441 HTTP/1.1" 200 -
^C12:58:27 system        | SIGINT received
12:58:27 system        | sending SIGTERM to redis_cache.1 (pid 37169)
12:58:27 system        | sending SIGTERM to redis_queue.1 (pid 37174)
12:58:27 system        | sending SIGTERM to web.1 (pid 37173)
12:58:27 system        | sending SIGTERM to socketio.1 (pid 37187)
12:58:27 system        | sending SIGTERM to watch.1 (pid 37179)
12:58:27 system        | sending SIGTERM to schedule.1 (pid 37188)
12:58:27 system        | sending SIGTERM to worker.1 (pid 37180)
12:58:27 redis_queue.1 | 37181:signal-handler (1719838707) Received SIGTERM scheduling shutdown...
12:58:27 redis_cache.1 | 37171:signal-handler (1719838707) Received SIGTERM scheduling shutdown...
12:58:28 redis_cache.1 | 37171:M 01 Jul 2024 12:58:27.641 # User requested shutdown...
12:58:28 redis_cache.1 | 37171:M 01 Jul 2024 12:58:27.713 * Removing the pid file.
12:58:28 redis_cache.1 | 37171:M 01 Jul 2024 12:58:27.780 # Redis is now ready to exit, bye bye...
12:58:27 redis_queue.1 | 37181:M 01 Jul 2024 12:58:27.706 # User requested shutdown...
12:58:27 redis_queue.1 | 37181:M 01 Jul 2024 12:58:27.710 * Removing the pid file.
12:58:27 redis_queue.1 | 37181:M 01 Jul 2024 12:58:27.725 # Redis is now ready to exit, bye bye...
12:58:28 system        | redis_queue.1 stopped (rc=-15)
12:58:28 system        | redis_cache.1 stopped (rc=-15)
12:58:28 system        | worker.1 stopped (rc=-15)
12:58:28 system        | socketio.1 stopped (rc=-15)
12:58:28 system        | schedule.1 stopped (rc=-15)
12:58:29 system        | watch.1 stopped (rc=-15)
12:58:31 system        | web.1 stopped (rc=-15)
elliot@frappe:~/frappe-bench$ chmod o+rx /home/elliot/
elliot@frappe:~/frappe-bench$ bench start 
12:58:50 system        | redis_queue.1 started (pid=38172)
12:58:50 system        | redis_cache.1 started (pid=38176)
12:58:50 system        | web.1 started (pid=38178)
12:58:50 redis_queue.1 | 38174:C 01 Jul 2024 12:58:50.280 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
12:58:50 redis_queue.1 | 38174:C 01 Jul 2024 12:58:50.280 # Redis version=6.0.16, bits=64, commit=00000000, modified=0, pid=38174, just started
12:58:50 redis_queue.1 | 38174:C 01 Jul 2024 12:58:50.280 # Configuration loaded
12:58:50 system        | worker.1 started (pid=38186)
12:58:50 redis_cache.1 | 38179:C 01 Jul 2024 12:58:50.286 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
12:58:50 redis_cache.1 | 38179:C 01 Jul 2024 12:58:50.286 # Redis version=6.0.16, bits=64, commit=00000000, modified=0, pid=38179, just started
12:58:50 redis_cache.1 | 38179:C 01 Jul 2024 12:58:50.286 # Configuration loaded
12:58:50 system        | watch.1 started (pid=38185)
12:58:50 redis_cache.1 | 38179:M 01 Jul 2024 12:58:50.292 * Increased maximum number of open files to 10032 (it was originally set to 1024).
12:58:50 redis_queue.1 | 38174:M 01 Jul 2024 12:58:50.295 * Increased maximum number of open files to 10032 (it was originally set to 1024).
12:58:50 system        | schedule.1 started (pid=38192)
12:58:50 redis_cache.1 | 38179:M 01 Jul 2024 12:58:50.309 * Running mode=standalone, port=13000.
12:58:50 redis_cache.1 | 38179:M 01 Jul 2024 12:58:50.315 # Server initialized
12:58:50 redis_cache.1 | 38179:M 01 Jul 2024 12:58:50.315 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
12:58:50 redis_queue.1 | 38174:M 01 Jul 2024 12:58:50.321 * Running mode=standalone, port=11000.
12:58:50 redis_cache.1 | 38179:M 01 Jul 2024 12:58:50.320 * Ready to accept connections
12:58:50 redis_queue.1 | 38174:M 01 Jul 2024 12:58:50.321 # Server initialized
12:58:50 redis_queue.1 | 38174:M 01 Jul 2024 12:58:50.321 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
12:58:50 redis_queue.1 | 38174:M 01 Jul 2024 12:58:50.326 * Ready to accept connections
12:58:50 system        | socketio.1 started (pid=38191)
12:58:52 watch.1       | 
12:58:52 socketio.1    | Realtime service listening on:  9000
12:58:53 web.1         | /home/elliot/frappe-bench/env/lib/python3.11/site-packages/passlib/utils/__init__.py:854: DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13
12:58:53 web.1         |   from crypt import crypt as _crypt
12:58:54 web.1         | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
12:58:54 web.1         |  * Running on all addresses (0.0.0.0)
12:58:54 web.1         |  * Running on http://127.0.0.1:8000
12:58:54 web.1         |  * Running on http://10.10.60.29:8000
12:58:54 web.1         | Press CTRL+C to quit
12:58:54 web.1         |  * Restarting with stat
12:58:54 watch.1       | yarn run v1.22.22
12:58:54 watch.1       | $ node esbuild --watch --live-reload
12:58:58 web.1         | /home/elliot/frappe-bench/env/lib/python3.11/site-packages/passlib/utils/__init__.py:854: DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13
12:58:58 web.1         |   from crypt import crypt as _crypt
12:59:00 web.1         |  * Debugger is active!
12:59:00 web.1         |  * Debugger PIN: 137-861-188
12:59:08 watch.1       | Browserslist: caniuse-lite is outdated. Please run:
12:59:08 watch.1       |   npx update-browserslist-db@latest
12:59:08 watch.1       |   Why you should do it regularly: https://github.com/browserslist/update-db#readme
12:59:17 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:17] "GET /app/setup-wizard/0 HTTP/1.1" 200 -
12:59:17 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:17] "GET /assets/frappe/dist/js/telemetry.bundle.ZJBT5ETW.js HTTP/1.1" 200 -
12:59:17 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:17] "GET /assets/frappe/dist/css/desk.bundle.7MPVM6RL.css HTTP/1.1" 200 -
12:59:17 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:17] "GET /assets/frappe/icons/timeless/icons.svg?v=1719838185.584056 HTTP/1.1" 200 -
12:59:17 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:17] "GET /assets/frappe/dist/css/report.bundle.RFJR5B24.css HTTP/1.1" 200 -
12:59:18 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:17] "GET /assets/frappe/icons/espresso/icons.svg?v=1719838185.584056 HTTP/1.1" 200 -
12:59:18 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:18] "GET /assets/erpnext/dist/css/erpnext.bundle.GXDIPWEB.css HTTP/1.1" 200 -
12:59:19 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:19] "GET /assets/erpnext/js/setup_wizard.js?v=1719838756340 HTTP/1.1" 200 -
12:59:19 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:19] "POST /api/method/frappe.desk.page.setup_wizard.setup_wizard.load_languages HTTP/1.1" 200 -
12:59:19 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:19] "POST /api/method/frappe.geo.country_info.get_country_timezone_info HTTP/1.1" 200 -
12:59:21 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:21] "GET /api/method/frappe.desk.form.load.getdoc?doctype=Currency&name=GHS&_=1719838755501 HTTP/1.1" 200 -
12:59:34 web.1         | 10.10.60.10 - - [01/Jul/2024 12:59:34] "POST /api/method/frappe.desk.page.setup_wizard.setup_wizard.load_user_details HTTP/1.1" 200 -
13:00:06 web.1         | 10.10.60.10 - - [01/Jul/2024 13:00:06] "POST /api/method/erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts.get_charts_for_country HTTP/1.1" 200 -
13:00:36 watch.1       | Watching for changes...
13:01:43 web.1         | Updating Dashboard for frappe
13:01:43 web.1         | Updating Dashboard for erpnext
13:01:44 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:44] "POST /api/method/frappe.desk.page.setup_wizard.setup_wizard.setup_complete HTTP/1.1" 200 -
13:01:55 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:55] "GET /app HTTP/1.1" 200 -
13:01:55 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:55] "GET /assets/frappe/dist/css/desk.bundle.MNGUF3M4.css HTTP/1.1" 200 -
13:01:55 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:55] "GET /assets/erpnext/dist/css/erpnext.bundle.34JBCQFT.css HTTP/1.1" 200 -
13:01:55 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:55] "GET /assets/frappe/dist/css/report.bundle.6SN3KWLG.css HTTP/1.1" 200 -
13:01:55 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:55] "GET /assets/frappe/icons/timeless/icons.svg?v=1719838838.9390998 HTTP/1.1" 200 -
13:01:56 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:56] "GET /assets/frappe/icons/espresso/icons.svg?v=1719838838.9390998 HTTP/1.1" 200 -
13:01:57 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:57] "POST /api/method/erpnext.accounts.utils.get_fiscal_year HTTP/1.1" 200 -
13:01:57 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:57] "POST /api/method/erpnext.accounts.utils.get_fiscal_year HTTP/1.1" 200 -
13:01:57 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:57] "POST /api/method/erpnext.accounts.utils.get_fiscal_year HTTP/1.1" 200 -
13:01:57 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:57] "POST /api/method/erpnext.accounts.utils.get_fiscal_year HTTP/1.1" 200 -
13:01:57 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:57] "GET /assets/erpnext/sounds/incoming-call.mp3 HTTP/1.1" 200 -
13:01:57 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:57] "GET /assets/frappe/sounds/alert.mp3 HTTP/1.1" 200 -
13:01:57 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:57] "GET /assets/erpnext/sounds/call-disconnect.mp3 HTTP/1.1" 200 -
13:01:57 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:57] "POST /api/method/frappe.desk.doctype.event.event.get_events HTTP/1.1" 200 -
13:01:57 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:57] "POST /api/method/frappe.desk.doctype.notification_log.notification_log.get_notification_logs HTTP/1.1" 200 -
13:01:58 web.1         | 10.10.60.10 - - [01/Jul/2024 13:01:58] "POST /api/method/frappe.desk.desktop.get_workspace_sidebar_items HTTP/1.1" 200 -
13:02:01 web.1         | 10.10.60.10 - - [01/Jul/2024 13:02:01] "POST /api/method/frappe.desk.desktop.get_desktop_page HTTP/1.1" 200 -
13:02:08 web.1         | 10.10.60.10 - - [01/Jul/2024 13:02:08] "POST /api/method/frappe.desk.doctype.route_history.route_history.deferred_insert HTTP/1.1" 200 -
^C13:43:16 system        | SIGINT received
13:43:16 system        | sending SIGTERM to redis_cache.1 (pid 38176)
13:43:16 system        | sending SIGTERM to redis_queue.1 (pid 38172)
13:43:16 system        | sending SIGTERM to web.1 (pid 38178)
13:43:16 system        | sending SIGTERM to socketio.1 (pid 38191)
13:43:16 system        | sending SIGTERM to watch.1 (pid 38185)
13:43:16 system        | sending SIGTERM to schedule.1 (pid 38192)
13:43:16 system        | sending SIGTERM to worker.1 (pid 38186)
13:43:16 redis_cache.1 | 38179:signal-handler (1719841396) Received SIGTERM scheduling shutdown...
13:43:16 redis_cache.1 | 38179:M 01 Jul 2024 13:43:16.585 # User requested shutdown...
13:43:16 redis_cache.1 | 38179:M 01 Jul 2024 13:43:16.590 * Removing the pid file.
13:43:16 redis_cache.1 | 38179:M 01 Jul 2024 13:43:16.721 # Redis is now ready to exit, bye bye...
13:43:16 redis_queue.1 | 38174:signal-handler (1719841396) Received SIGTERM scheduling shutdown...
13:43:17 redis_queue.1 | 38174:M 01 Jul 2024 13:43:16.641 # User requested shutdown...
13:43:17 redis_queue.1 | 38174:M 01 Jul 2024 13:43:16.643 * Removing the pid file.
13:43:17 redis_queue.1 | 38174:M 01 Jul 2024 13:43:16.697 # Redis is now ready to exit, bye bye...
13:43:17 system        | worker.1 stopped (rc=-15)
13:43:17 system        | redis_cache.1 stopped (rc=-15)
13:43:17 system        | redis_queue.1 stopped (rc=-15)
13:43:17 system        | socketio.1 stopped (rc=-15)
13:43:17 system        | schedule.1 stopped (rc=-15)
13:43:18 system        | watch.1 stopped (rc=-15)
13:43:19 system        | web.1 stopped (rc=-15)
elliot@frappe:~/frappe-bench$ cd ..
elliot@frappe:~$ sudo mkdir 
[sudo] password for elliot: 
mkdir: missing operand
Try 'mkdir --help' for more information.
elliot@frappe:~$ sudo mkdir frappe-erpnext installation script up-to bench start 
elliot@frappe:~$ ls
bench  frappe-bench  frappe-erpnext  install_erpnext.py  installation  script  start  up-to
elliot@frappe:~$ rm -rf installation 
elliot@frappe:~$ rm -rf script 
elliot@frappe:~$ rm -rf up-to 
elliot@frappe:~$ rm -rf frappe-erpenxt 
elliot@frappe:~$ sudo mkdir frappe-erpnext-installation-script 
elliot@frappe:~$ ls
bench  frappe-bench  frappe-erpnext  frappe-erpnext-installation-script  install_erpnext.py  start
elliot@frappe:~$ mv install_erpnext.py frappe-erpnext-installation-script/
mv: cannot move 'install_erpnext.py' to 'frappe-erpnext-installation-script/install_erpnext.py': Permission denied
elliot@frappe:~$ sudo mv install_erpnext.py frappe-erpnext-installation-script/
elliot@frappe:~$ ls
bench  frappe-bench  frappe-erpnext  frappe-erpnext-installation-script  start
elliot@frappe:~$ cd frappe-erpnext-installation-script
elliot@frappe:~/frappe-erpnext-installation-script$ ls
install_erpnext.py
elliot@frappe:~/frappe-erpnext-installation-script$ cd ..
elliot@frappe:~$ ls
bench  frappe-bench  frappe-erpnext  frappe-erpnext-installation-script  start
elliot@frappe:~$ cd /frappe-erpnext-installation-script
-bash: cd: /frappe-erpnext-installation-script: No such file or directory
elliot@frappe:~$ cd ./frappe-erpnext-installation-script
elliot@frappe:~/frappe-erpnext-installation-script$ ls
install_erpnext.py
elliot@frappe:~/frappe-erpnext-installation-script$ nano install_erpnext.py

  GNU nano 6.2                                                      install_erpnext.py                                                               
#!/usr/bin/env python3

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
    print_colored("Elliot Brenya ERPNext Installation Script", Fore.GREEN)
    print_colored("========================================", Fore.GREEN)

    # Ensure script is run with sudo
    if os.geteuid() != 0:
                                                          [ Directory '.' is not writable ]
^G Help         ^O Write Out    ^W Where Is     ^K Cut          ^T Execute      ^C Location     M-U Undo        M-A Set Mark    M-] To Bracket
^X Exit         ^R Read File    ^\ Replace      ^U Paste        ^J Justify      ^/ Go To Line   M-E Redo        M-6 Copy        ^Q Where Was
