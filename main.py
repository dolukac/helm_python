from time import sleep

from commands.cleaner import clean_namespace, clean_CNF
from commands.checker import cluster_health_check, list_pods_namespace, pod_check, pod_list, get_namespaces
from commands.commands import exec_command
from commands.instantiate_CNF import instiate_CNF
from commands.update_upgrade_CNF import update_via_cli, update_via_yaml, upgrade_chart_version, rollback_revision_CNF
from kubernetes import client, config

with open("C:/Users/1994d/PycharmProjects/helm_python/commands/command_lists.txt") as file:
    lines = file.readlines()
    commands = [line.rstrip() for line in lines]

config.load_kube_config()
v1 = client.CoreV1Api()

NAMESPACE='free5gc'
NAME_HELM_DEP='free5gc-v1'
CHART_NAME_URL='https://raw.githubusercontent.com/dolukac/towards5gs-helm/main/repo/free5gc-nrf-0.1.1.tgz'
CHART_VALUES_URL='https://raw.githubusercontent.com/dolukac/towards5gs-helm/main/charts/free5gc/charts/free5gc-nrf/values.yaml'
SETS= '--set global.sbi.scheme=https'
CHART_NAME_URL_NEW_CHART='https://raw.githubusercontent.com/dolukac/towards5gs-helm/main/repo/free5gc-nrf-0.2.1.tgz'
OLD_HELM_REVISION = '1'

def print_namespaces():
    print("-------- Get Namespaces")
    print('Implementation of command: kubectl get namespace')
    namespaces=get_namespaces(v1)
    for i in namespaces:
        print(i)

if __name__ == "__main__":

    cluster_health_check(commands[0])

    #instantiate cnf
    # namespace
    # -n free5gc(namespace)
    # free5gc-v1(name of the helm deployment)
    # towards5gs/free5gc(chart name)
    # value.yaml
    print_namespaces()
    #instiate_CNF(commands,'free5gc','free5gc-v1','https://raw.githubusercontent.com/Orange-OpenSource/towards5gs-helm/main/repo/free5gc-0.1.0.tgz','https://raw.githubusercontent.com/Orange-OpenSource/towards5gs-helm/main/charts/free5gc/values.yaml')
    instiate_CNF(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL,CHART_VALUES_URL)

    pod_list(NAMESPACE)

    verify_health = pod_check(NAMESPACE, NAME_HELM_DEP)
    if verify_health != 'Running':
        print("----CNF is NOT HEALTHY----")

    sleep(60)

    verify_health=pod_check(NAMESPACE,NAME_HELM_DEP)
    pod_list(NAMESPACE)

    if verify_health == 'Running':
        #update_CNF
        update_via_cli(commands, NAMESPACE, NAME_HELM_DEP, CHART_NAME_URL, SETS)

    sleep(20)

    # update_CNF
    verify_health = pod_check(NAMESPACE, NAME_HELM_DEP)
    pod_list(NAMESPACE)
    if verify_health == 'Running':
        update_via_yaml(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL,CHART_VALUES_URL)

    sleep(20)
    #upgrade CNF
    verify_health = pod_check(NAMESPACE, NAME_HELM_DEP)
    pod_list(NAMESPACE)
    if verify_health == 'Running':
            upgrade_chart_version(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL_NEW_CHART,CHART_VALUES_URL)

    sleep(20)
    #rollback of  CNF
    verify_health = pod_check(NAMESPACE, NAME_HELM_DEP)
    pod_list(NAMESPACE)
    if verify_health == 'Running':
        rollback_revision_CNF(commands,NAMESPACE,NAME_HELM_DEP, OLD_HELM_REVISION)

    sleep(20)
    #terminate CNF
    verify_health = pod_check(NAMESPACE, NAME_HELM_DEP)
    pod_list(NAMESPACE)
    if verify_health == 'Running':
        clean_CNF(commands, NAMESPACE, NAME_HELM_DEP)

    sleep(60)

    clean_namespace(NAMESPACE)
    sleep(30)
    print_namespaces()

















