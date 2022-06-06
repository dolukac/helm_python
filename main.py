from time import sleep

from commands.cleaner import clean_namespace, clean_CNF
from commands.checker import cluster_health_check, list_pods_namespace
from commands.commands import exec_command
from commands.instantiate_CNF import instiate_CNF
from commands.update_upgrade_CNF import update_via_cli, update_via_yaml, upgrade_chart_version, rollback_revision_CNF

with open("C:/Users/1994d/PycharmProjects/helm_python/commands/command_lists.txt") as file:
    lines = file.readlines()
    commands = [line.rstrip() for line in lines]

NAMESPACE='free5gc'
NAME_HELM_DEP='free5gc-v1'
CHART_NAME_URL='https://raw.githubusercontent.com/dolukac/towards5gs-helm/main/repo/free5gc-0.1.1.tgz'
CHART_VALUES_URL='https://raw.githubusercontent.com/dolukac/towards5gs-helm/main/charts/free5gc/values.yaml'
SETS= '--set global.sbi.scheme=https'
CHART_NAME_URL_NEW_CHART='https://raw.githubusercontent.com/dolukac/towards5gs-helm/main/repo/free5gc-0.1.2.tgz'
OLD_HELM_REVISION = '1'

if __name__ == "__main__":

    cluster_health_check(commands[0])

    #instantiate cnf
    # namespace
    # -n free5gc(namespace)
    # free5gc-v1(name of the helm deployment)
    # towards5gs/free5gc(chart name)
    # value.yaml

    #instiate_CNF(commands,'free5gc','free5gc-v1','https://raw.githubusercontent.com/Orange-OpenSource/towards5gs-helm/main/repo/free5gc-0.1.0.tgz','https://raw.githubusercontent.com/Orange-OpenSource/towards5gs-helm/main/charts/free5gc/values.yaml')
    instiate_CNF(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL,CHART_VALUES_URL)
#
    #update_CNF
    #update_via_cli(commands, NAMESPACE, NAME_HELM_DEP, CHART_NAME_URL, SETS)

    #update cnf via yaml
    #update_via_yaml(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL,CHART_VALUES_URL)

    #upgrade CNF
    #upgrade_chart_version(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL_NEW_CHART,CHART_VALUES_URL)

    #rollback of  CNF
    #rollback_revision_CNF(commands,NAMESPACE,NAME_HELM_DEP, OLD_HELM_REVISION)

    #terminate CNF
    #clean_CNF(commands, NAMESPACE, NAME_HELM_DEP)

    #list_pods_namespace("free5gc")
    #clean_namespace(NAMESPACE)

    #delete namespace
    #list_pods_namespace(NAMESPACE)
















