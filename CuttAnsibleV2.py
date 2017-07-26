#!/usr/bin/env python
# coding:utf-8

__author__ = "dewly_tg"

"""
Ansible module for python of version 2.+
"""

import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import importlib

class ResultCallback(CallbackBase):
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
        self.data = json.dumps({host.name: result._result}, indent=4)

def getPath(module):
    mresult = importlib.import_module(module)
    mpath = mresult.__file__
    return  mpath

def exec_ansible(module,args,host):
    # initialize needed objects
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check'])
    variable_manager = VariableManager()
    loader = DataLoader()

    # module_path参数指定本地ansible模块包的路径
    mpath = getPath("ansible") + "/" + "modules"
    options = Options(connection='smart', module_path=mpath, forks=100, become=None, become_method=None, become_user='root', check=False)
    passwords = dict(vault_pass='secret')

    # Instantiate our ResultCallback for handling results as they come in
    results_callback = ResultCallback()

    # create inventory and pass to var manager
    #host_list指定本地ansible的hosts文件
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='/etc/ansible/hosts')
    variable_manager.set_inventory(inventory)

    # create play with tasks
    play_source =  dict(
        name = "Ansible Play",
        # hosts可以指定inventory中的一组主机，也可指定单台主机
        hosts = host,
        gather_facts = 'no',
        #task执行列表，如果想一次执行多个任务，可以在列表中添加任务
        tasks = [
            dict(action=dict(module=module, args=args), register='shell_out'),
        ]
        )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # actually run it
    tqm = None
    try:
        tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            options=options,
            passwords=passwords,
            stdout_callback=results_callback,
        )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup
        return json.loads(results_callback.data)