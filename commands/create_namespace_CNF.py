import time
from commands.commands import exec_command
from commands.checker import pod_health_check, get_namespaces, check_state_namespace
from kubernetes import client, config


#crate nemespace if doesn't exist
def create_namespace(NAMESPACE):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("-------- Check if namespace exists, if no exist then create ")
    if NAMESPACE not in get_namespaces(v1):
        v1.create_namespace(client.V1Namespace(metadata=client.V1ObjectMeta(name=NAMESPACE)))
        time.sleep(3)
        print(f'Namespace {NAMESPACE} created')
    else:
        print(f'Namespace {NAMESPACE} exist')

#instiate CNF
def instanciate_CNF(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL, CHART_VALUES_URL,wait_health):
    # replace relevant {values} in template command_lists
    instiate_CNF_command=commands[1]
    instiate_CNF_command = instiate_CNF_command.replace('{NAMESPACE}', NAMESPACE)
    instiate_CNF_command = instiate_CNF_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    instiate_CNF_command = instiate_CNF_command.replace('{CHART_NAME_URL}', CHART_NAME_URL)
    instiate_CNF_command = instiate_CNF_command.replace('{CHART_VALUES_URL}', CHART_VALUES_URL)

    print("-------- Instanciate CNF")
    #check if namespace exists and is active
    name_space_check=check_state_namespace(NAMESPACE)
    if name_space_check == True:
        print(f'Namespace {NAMESPACE} is active')
        deployment_check = exec_command(instiate_CNF_command)
        if deployment_check == True:
            print(f'Implementation of command: {instiate_CNF_command}')
            #check if was instanciation correct
            print(pod_health_check(NAMESPACE, NAME_HELM_DEP,wait_health))
        else:
            print(deployment_check)
    else:
        print(f'Namespace {NAMESPACE} is not active')










