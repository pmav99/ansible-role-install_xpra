[![Build Status](https://travis-ci.com/pmav99/ansible-role-install_xpra.svg?branch=master)](https://travis-ci.com/pmav99/ansible-role-install_xpra)

install_xpra
=============

An ansible role for installing GRASS GIS on Ubuntu 16.04 & 18.04 and Fedora 28 & 29

The role also installs the latest Python 2 version and R

Quickstart
----------

    ansible-galaxy install pmav99.install_xpra
    wget https://git.io/fh87W -O install_xpra.yml
    ansible-playbook install_xpra.yml --ask-become

Install the role
----------------

You can install the role by using:

    ansible-galaxy install pmav99.install_xpra

Example Playbook
----------------

If you want to install xpra locally you can use the following playbook:

    - hosts: 127.0.0.1
      connection: local
      roles:
         - role: pmav99.install_xpra

You can also download it with:

    wget https://raw.githubusercontent.com/pmav99/ansible-role-install_xpra/master/install_xpra.yml -O install_xpra.yml

License
-------

MIT
