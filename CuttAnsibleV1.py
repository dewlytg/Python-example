#!/usr/bin/env python
# coding:utf-8
__author__ = "dewly_tg"

"""
Ansible module for python of version 1.+
"""

import ansible.runner


##python中ansible模块调用
def ansible(host, inventory, module, moduleargs):
    """


    :param host: please input a host or hostgroup which you want to remote host
    :param inventory: this hostlist is hosts of ansible,example:/etc/ansible/hosts,or put a hostlist must be list
    :param module: you might choose a module for ansible, ping cory file user rpm yum shell command script
    :return:result of programm
    """
    runner = ansible.runner.Runner(
        module_name=module,
        module_args=moduleargs,
        host_list=inventory,
        pattern=host
    )
    ret = runner.run()
    return ret
