server-upgrade (version: 1.0.0)
=========

[Ansible][ansible] role for management of Huawei Server driver version.

With this role, you could:

- list server upgrade list
- upgrade driver & firmware
- Restart OS

Requirements
------------

- ansible >= 2.4
- Target Huawei Server with iBMC


Role Variables
--------------

- **command**: what command of the role expected to run.
  - upgrade-list: list target server upgrade list
  - auto-upgrade: auto upgrade server
  - restart: restart target OS
- **drivers**: a list of name/version for the drivers to be upgraded (used when command is `auto-upgrade`).
- **inbandFW**: a list of name/version for the inband firmware to be upgraded (used when command is `auto-upgrade`).
- **outbandFW**: a list of name/version for the outband firmware to be upgraded (used when command is `auto-upgrade`).
- **driver_repo_baseurl**: driver yum repo baseurl (used when command is `upgrade-list` or `auto-upgrade`).
- **driver_repo_gpgcheck**: driver yum repo gpgcheck [yes|no] (used when command is `upgrade-list` or `auto-upgrade`).
- **firmware_repo_baseurl**: firmware yum repo baseurl (used when command is `upgrade-list` or `auto-upgrade`).
- **firmware_repo_gpgcheck**: firmware yum repo gpgcheck [yes|no] (used when command is `upgrade-list` or `auto-upgrade`).


Dependencies
------------

None.

Example Playbook
----------------

- list upgrade list:

```
---

- hosts: servers
  roles:
    - { role: 'Huawei.server-upgrade', command: 'upgrade-list' }
```


- auto upgrade server (include all drivers and firmwares):

```
---
  
- hosts: servers
  remote_user: root
  roles:
    - role: 'Huawei.server-upgrade'
      command: 'auto-upgrade'
      
```


- Restart OS:

```
---
  
- hosts: servers
  remote_user: root
  roles:
    - role: 'Huawei.server-upgrade'
      command: 'restart'
      
```


License
-------

Apache 2.0


[ansible]:  https://ansible.com/    "Ansible"