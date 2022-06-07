import yaml
from kubernetes import client, config

import logging

from commands.commands import exec_command

def update_upgrade_history_check(commands,NAMESPACE,NAME_HELM_DEP):
    #command on show history of revisions
    update_upgrade_history= commands[4]
    update_upgrade_history = update_upgrade_history.replace('{NAMESPACE}', NAMESPACE)
    update_upgrade_history = update_upgrade_history.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)

    update_upgrade_history_S = exec_command(update_upgrade_history)
    print("-------- HELM HISTORY UPDATE/UPGRADE ")
    print(f"Implementation of command: {update_upgrade_history}")
    print("\n".join(update_upgrade_history_S))

def update_via_cli(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL,SETS):
    # command on update deployment via CLI
    update_via_cli_command = commands[3]
    update_via_cli_command  = update_via_cli_command.replace('{NAMESPACE}', NAMESPACE)
    update_via_cli_command  = update_via_cli_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    update_via_cli_command  = update_via_cli_command.replace('{CHART_NAME_URL}', CHART_NAME_URL)
    update_via_cli_command  = update_via_cli_command.replace('{SETS}', SETS)

    update_via_cli_command_check = exec_command(update_via_cli_command )
    print("-------- CNF CLI update ")
    print(f"Implementation of command: {update_via_cli_command}")
    print("\n".join(update_via_cli_command_check))

    #check history of revisions
    update_upgrade_history_check(commands,NAMESPACE,NAME_HELM_DEP)

def update_via_yaml(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL, CHART_VALUES_URL):
    #command on update deployment via yaml
    update_via_yaml_command=commands[5]
    update_via_yaml_command = update_via_yaml_command.replace('{NAMESPACE}', NAMESPACE)
    update_via_yaml_command = update_via_yaml_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    update_via_yaml_command = update_via_yaml_command.replace('{CHART_NAME_URL}', CHART_NAME_URL)
    update_via_yaml_command = update_via_yaml_command.replace('{CHART_VALUES_URL}', CHART_VALUES_URL)

    update_via_yaml_command_check = exec_command(update_via_yaml_command)
    print("-------- UPDATE CNF via YAML")
    print(f"Implementation of command: {update_via_yaml_command}")
    print("\n".join(update_via_yaml_command_check))

    # check history of revisions
    update_upgrade_history_check(commands,NAMESPACE,NAME_HELM_DEP)

def upgrade_chart_version(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL, CHART_VALUES_URL):
    # command on upgrade deployment
    upgrade_CNF_command = commands[6]
    upgrade_CNF_command = upgrade_CNF_command.replace('{NAMESPACE}', NAMESPACE)
    upgrade_CNF_command = upgrade_CNF_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    upgrade_CNF_command = upgrade_CNF_command.replace('{CHART_NAME_URL}', CHART_NAME_URL)
    upgrade_CNF_command = upgrade_CNF_command.replace('{CHART_VALUES_URL}', CHART_VALUES_URL)


    upgrade_chart = exec_command(upgrade_CNF_command)
    print("-------- Upgrade CNF")
    print(f"Implementation of command: {upgrade_CNF_command}")
    print("\n".join(upgrade_chart))

    # check history of revisions
    update_upgrade_history_check(commands, NAMESPACE, NAME_HELM_DEP)

def rollback_revision_CNF(commands,NAMESPACE,NAME_HELM_DEP, OLD_HELM_REVISION):
    #rollback of revision
    rollback_revision_CNF_command = commands[7]
    rollback_revision_CNF_command = rollback_revision_CNF_command.replace('{NAMESPACE}', NAMESPACE)
    rollback_revision_CNF_command = rollback_revision_CNF_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    rollback_revision_CNF_command = rollback_revision_CNF_command.replace('{OLD_HELM_REVISION}', OLD_HELM_REVISION)


    revision = exec_command(rollback_revision_CNF_command)
    print("-------- Rollback revision CNF")
    print(f"Implementation of command: {rollback_revision_CNF_command}")
    print("\n".join(revision))

    # check history of revisions
    update_upgrade_history_check(commands, NAMESPACE, NAME_HELM_DEP)

