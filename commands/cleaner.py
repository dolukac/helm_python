from kubernetes import client, config
import time

from commands.commands import exec_command


def clean_namespace(NAMESPACE):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    v1.delete_namespace(NAMESPACE)
    print(f"-------- Delete namespace")
    print(f"Implementation of command: kubectl delete namespace {NAMESPACE}")

def clean_CNF(commands, NAMESPACE, NAME_HELM_DEP):
    terminate_CNF_command = commands[8]
    terminate_CNF_command = terminate_CNF_command.replace('{NAMESPACE}', NAMESPACE)
    terminate_CNF_command = terminate_CNF_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    print("-------- Terminate CNF")
    print(f"Implementation of command: {terminate_CNF_command}")
    terminate = exec_command(terminate_CNF_command)
    print("\n".join(terminate))
