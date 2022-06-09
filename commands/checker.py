from commands.commands import exec_command_need

from datetime import datetime

import time
from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()

#check health of kubernetes cluster
#if cluster isn't in good health than exit() script
def cluster_health_check(health_command):
    #create actual health of kubernetes cluster
    cluster_check=exec_command_need(health_command)

    #load good check of kubernetes cluster
    with open('C:/Users/1994d/PycharmProjects/helm_python/help_files/health_good.txt') as file:
        good_health = file.readlines()
    def listToString(s):
        # initialize an empty string
        str1 = ""
        # traverse in the string
        for ele in s:
            str1 += ele
            # return string
        return str1
    #compare actual state of kubernetes cluster with good state
    #if they're not the same redirect actual state to output_files/health_check
    if cluster_check != listToString(good_health):
        with open('C:/Users/1994d/PycharmProjects/helm_python/output_files/health_check.txt', 'a') as f:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string)
            f.write('\n')
            for item in cluster_check:
                # write each item on a new line
                f.write("%s\n" % item)
        print("Cluster IS NOT in good health")
        return exit()


#get list of all namespaces
def get_namespaces(v1):
    namespaces_list=[]
    nameSpaceList = v1.list_namespace()

    for nameSpace in nameSpaceList.items:
        namespaces_list.append(nameSpace.metadata.name)
    return namespaces_list

#print all namespaces
def print_namespaces():
    namespaces=get_namespaces(v1)
    k=[]
    for i in namespaces:
        k.append(i)

    return k

#check state of namespace
def check_state_namespace(NAMESPACE):
    if NAMESPACE in get_namespaces(v1):
        exist_namespace = v1.read_namespace(NAMESPACE)

        if exist_namespace.status.phase == 'Active':
            a=exist_namespace.status.phase
            return True
        else:
            a=exist_namespace.status.phase
            return False

#check running pods, function return Running and based on this are then some conditions written
def pod_health_check(NAMESPACE,NAME_HELM_DEP,wait_health):
    time.sleep(2)
    for _ in range(3):
        time.sleep(wait_health)
        pod_namespace_list = v1.list_namespaced_pod(NAMESPACE)
        for podNamespace in pod_namespace_list.items:
            if podNamespace.metadata.name.startswith(NAME_HELM_DEP):
                pod_health = v1.read_namespaced_pod(podNamespace.metadata.name,NAMESPACE)
                if pod_health.status.phase == 'Running':
                    return 'Health check good'
                else:
                    result_health = False
    if result_health == False :
        return 'Health check not good'

#show all pods for namespace
def pod_list(NAMESPACE):
    pod_namespace_list = v1.list_namespaced_pod(NAMESPACE)
    print("-------- Healthcheck CNF")
    print(f"Implementation of command: kubectl get pods -n {NAMESPACE}")
    for podNamespace in pod_namespace_list.items:
        print(podNamespace.status.phase,podNamespace.metadata.name)