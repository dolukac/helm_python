from kubernetes import client, config
import time

from commands.checker import print_namespaces
from commands.commands import exec_command

config.load_kube_config()
v1 = client.CoreV1Api()

#delete namespace
#1. check if namespace exist
#3. delete namespace
#4. Check, if is namespaced deleted  3 times, for each loop sleep=wait_health
#5. If no return 'check message'
def clean_namespace(NAMESPACE,wait_health):
    print(f"-------- Delete namespace")
    print(f"Implementation of command: kubectl delete namespace {NAMESPACE}")
    namespaces_alive=print_namespaces()
    if NAMESPACE not in namespaces_alive:
        return 'Namespace does not exist'
    else:
        v1.delete_namespace(NAMESPACE)
        for _ in range(3):
            namespaces_alive=print_namespaces()
            if NAMESPACE not in namespaces_alive:
                return 'Namespace deleted'
            else:
                time.sleep(wait_health)

    return 'Check namespace'


#terminate CNF
#1. check if CNF exist
#2. check if is CNF running
#3. delete running CNF
#4. Check, if is CNF terminated 3 times, for each loop sleep=wait_health
#5. If no return 'check message'

def clean_CNF(commands, NAMESPACE, NAME_HELM_DEP,wait_health):
    terminate_CNF_command = commands[8]
    terminate_CNF_command = terminate_CNF_command.replace('{NAMESPACE}', NAMESPACE)
    terminate_CNF_command = terminate_CNF_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)

    print("-------- Terminate CNF")
    print(f"Implementation of command: {terminate_CNF_command}")

    pod_namespace_list = v1.list_namespaced_pod(NAMESPACE)
    if pod_namespace_list.items == []:
        return f"CNF {NAME_HELM_DEP} exists"
    else:
        for podNamespace in pod_namespace_list.items:
            if podNamespace.metadata.name.startswith(NAME_HELM_DEP):
                if podNamespace.status.phase == 'Running':
                    exec_command(terminate_CNF_command)
                    time.sleep(wait_health)
                    for _ in range(3):
                        pod_namespace_list2 = v1.list_namespaced_pod(NAMESPACE)
                        if pod_namespace_list2.items == []:
                            return "CNF terminated"
                        else:
                            for podNamespace in pod_namespace_list2.items:
                                if not podNamespace.metadata.name.startswith(NAME_HELM_DEP):
                                    return "CNF terminated"
                                else:
                                    time.sleep(wait_health)
                    return f"Check CNF"
                else:
                    return f"CNF with {NAME_HELM_DEP} not exists"
            else:
                return f"CNF with {NAME_HELM_DEP} not exists"
