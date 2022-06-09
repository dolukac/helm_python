from time import sleep

from commands.cleaner import clean_namespace, clean_CNF
from commands.checker import cluster_health_check, pod_list, get_namespaces, pod_health_check
from commands.commands import exec_command
from commands.create_namespace_CNF import create_namespace, instanciate_CNF
from commands.update_upgrade_CNF import update_via_cli, update_via_yaml, upgrade_chart_version, rollback_revision_CNF
from kubernetes import client, config

#load template for commands
with open("C:/Users/1994d/PycharmProjects/helm_python/commands/command_lists.txt") as file:
    lines = file.readlines()
    commands = [line.rstrip() for line in lines]

config.load_kube_config()
v1 = client.CoreV1Api()

'''
define basic variables for performs operations like:
    - cluster health check
    - create namespace
    - instantiate CNF
    - update CNF
    - update CNF via yaml (change in gitlab is needed)
    - upgrade chart version of CNF
    - rollback of update/upgrade (please consider that in HELM3, you can return back just 10 reviosion (default value, can be different))
    - terminate CNF
    - delete namespace
'''

#namespace for perform operation
NAMESPACE='free5gc'
#namespace of CNF/deployment name
NAME_HELM_DEP='free5gc-v1'
#URL for chart
CHART_NAME_URL='https://raw.githubusercontent.com/dolukac/towards5gs-helm/main/repo/free5gc-nrf-0.1.1.tgz'
#URL with valus.yaml
CHART_VALUES_URL='https://raw.githubusercontent.com/dolukac/towards5gs-helm/main/charts/free5gc/charts/free5gc-nrf/values.yaml'
#Parameter for deployment
SETS= '--set global.sbi.scheme=http'
#URL for chart with diffrent package
CHART_NAME_URL_NEW_CHART='https://raw.githubusercontent.com/dolukac/towards5gs-helm/main/repo/free5gc-nrf-0.2.1.tgz'
#Number of revision
OLD_HELM_REVISION = '8'

if __name__ == "__main__":

    cluster_health_check(commands[0])
    create_namespace(NAMESPACE)

    instanciate_CNF(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL,CHART_VALUES_URL,10)
    update_via_cli(commands, NAMESPACE, NAME_HELM_DEP, CHART_NAME_URL, SETS,10)
    update_via_yaml(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL,CHART_VALUES_URL,10)
    upgrade_chart_version(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL_NEW_CHART,CHART_VALUES_URL,10)
    #please consider that in HELM3, you can return back just 10 reviosion (default value, can be different)
    rollback_revision_CNF(commands,NAMESPACE,NAME_HELM_DEP, OLD_HELM_REVISION,10)
    print(clean_CNF(commands, NAMESPACE, NAME_HELM_DEP,15))
    print(clean_namespace(NAMESPACE,5))


















