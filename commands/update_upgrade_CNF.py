from commands.checker import pod_health_check
from commands.commands import exec_command, exec_command_need


#show history of revisions
def update_upgrade_history_check(commands,NAMESPACE,NAME_HELM_DEP):
    #replace relevant {values} in template command_lists
    update_upgrade_history= commands[4]
    update_upgrade_history = update_upgrade_history.replace('{NAMESPACE}', NAMESPACE)
    update_upgrade_history = update_upgrade_history.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    #execution of command
    update_upgrade_history_S = exec_command_need(update_upgrade_history)
    print("-------- HELM HISTORY UPDATE/UPGRADE ")
    #print(f"Implementation of command: {update_upgrade_history}")
    print(update_upgrade_history_S)

#update CNF via CLI
def update_via_cli(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL,SETS,wait_health):
    #replace relevant {values} in template command_lists
    update_via_cli_command = commands[3]
    update_via_cli_command  = update_via_cli_command.replace('{NAMESPACE}', NAMESPACE)
    update_via_cli_command  = update_via_cli_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    update_via_cli_command  = update_via_cli_command.replace('{CHART_NAME_URL}', CHART_NAME_URL)
    update_via_cli_command  = update_via_cli_command.replace('{SETS}', SETS)

    #check of CNF before update
    before_check=pod_health_check(NAMESPACE, NAME_HELM_DEP, wait_health)
    print("-------- CNF CLI update ")
    if before_check == 'Health check good':
        print(f'Before operation {before_check}')
        # execution of command
        update_via_cli_command_check = exec_command(update_via_cli_command )
        if update_via_cli_command_check == True:
            print(f"Implementation of command: {update_via_cli_command}")
            # check of CNF after update
            after_health_check=pod_health_check(NAMESPACE, NAME_HELM_DEP,wait_health)
            print(f'After operation {after_health_check}')
            # check history of revisions
            update_upgrade_history_check(commands, NAMESPACE, NAME_HELM_DEP)

        else:
            print(update_via_cli_command_check)
    else:
        print('Before health check not good')


#update CNF deployment via yaml
#please consider change of yaml in repo
def update_via_yaml(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL, CHART_VALUES_URL,wait_health):
    # replace relevant {values} in template command_lists
    update_via_yaml_command=commands[5]
    update_via_yaml_command = update_via_yaml_command.replace('{NAMESPACE}', NAMESPACE)
    update_via_yaml_command = update_via_yaml_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    update_via_yaml_command = update_via_yaml_command.replace('{CHART_NAME_URL}', CHART_NAME_URL)
    update_via_yaml_command = update_via_yaml_command.replace('{CHART_VALUES_URL}', CHART_VALUES_URL)

    #check of CNF before update
    before_check = pod_health_check(NAMESPACE, NAME_HELM_DEP, wait_health)
    print("-------- CNF YAML update ")
    if before_check == 'Health check good':
        print(f'Before operation {before_check}')
        # execution of command
        update_via_yaml_command_check = exec_command(update_via_yaml_command)

        if update_via_yaml_command_check == True:
            print(f"Implementation of command: {update_via_yaml_command}")
            # check of CNF after update
            after_health_check = pod_health_check(NAMESPACE, NAME_HELM_DEP, wait_health)
            print(f'After operation {after_health_check}')
            # check history of revisions
            update_upgrade_history_check(commands, NAMESPACE, NAME_HELM_DEP)
        else:
            print(update_via_yaml_command_check)
    else:
        print('Before health check not good')


#upgrade CNF via change in yaml
def upgrade_chart_version(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL, CHART_VALUES_URL,wait_health):
    # replace relevant {values} in template command_lists
    upgrade_CNF_command = commands[6]
    upgrade_CNF_command = upgrade_CNF_command.replace('{NAMESPACE}', NAMESPACE)
    upgrade_CNF_command = upgrade_CNF_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    upgrade_CNF_command = upgrade_CNF_command.replace('{CHART_NAME_URL}', CHART_NAME_URL)
    upgrade_CNF_command = upgrade_CNF_command.replace('{CHART_VALUES_URL}', CHART_VALUES_URL)

    #check of CNF before update
    before_check = pod_health_check(NAMESPACE, NAME_HELM_DEP, wait_health)
    print("-------- CNF Upgrade update ")
    if before_check == 'Health check good':
        print(f'Before operation {before_check}')
        # execution of command
        upgrade_chart_check = exec_command(upgrade_CNF_command)
        if upgrade_chart_check == True:
            print(f"Implementation of command: {upgrade_CNF_command}")
            # check of CNF after update
            after_health_check = pod_health_check(NAMESPACE, NAME_HELM_DEP, wait_health)
            print(f'After operation {after_health_check}')
            # check history of revisions
            update_upgrade_history_check(commands, NAMESPACE, NAME_HELM_DEP)

        else:
            print(upgrade_chart_check)
    else:
        print('Before health check not good')

#rolback CNF
def rollback_revision_CNF(commands,NAMESPACE,NAME_HELM_DEP, OLD_HELM_REVISION,wait_health):
    # replace relevant {values} in template command_lists
    rollback_revision_CNF_command = commands[7]
    rollback_revision_CNF_command = rollback_revision_CNF_command.replace('{NAMESPACE}', NAMESPACE)
    rollback_revision_CNF_command = rollback_revision_CNF_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    rollback_revision_CNF_command = rollback_revision_CNF_command.replace('{OLD_HELM_REVISION}', OLD_HELM_REVISION)

    #check of CNF before rollback
    before_check = pod_health_check(NAMESPACE, NAME_HELM_DEP, wait_health)
    print("-------- CNF rollback  ")
    if before_check == 'Health check good':
        print(f'Before operation {before_check}')
        # execution of command
        rollbac_check = exec_command(rollback_revision_CNF_command)
        if rollbac_check == True:
            print(f"Implementation of command: {rollback_revision_CNF_command}")
            after_health_check = pod_health_check(NAMESPACE, NAME_HELM_DEP, wait_health)
            # check of CNF after rollback
            print(f'After operation {after_health_check}')
            # check history of revisions
            update_upgrade_history_check(commands, NAMESPACE, NAME_HELM_DEP)
        else:
            print(rollbac_check)
    else:
        print('Before health check not good')

