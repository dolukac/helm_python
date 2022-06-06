from commands.commands import exec_command

from datetime import datetime
from kubernetes import client, config
from kubernetes import client, config
import time

def cluster_health_check(health_command):
#command on check health of kubernetes cluster
    cluster_check=exec_command(health_command)
    #load good check of kubernetes cluster
    with open('C:/Users/1994d/PycharmProjects/helm_python/help_files/health_good.txt') as file:
        good_health = []
        for line in file:
            good_health.append(line.rstrip())

    if cluster_check != good_health:
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

def list_pods_namespace(pod_name):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pod_list=v1.list_namespaced_pod(pod_name)
    for pod in pod_list.items:
        print("%s \t%s " % (pod.status.phase,pod.metadata.name))

#get list of all namespaces
def get_namespaces(v1):
    namespaces_list=[]
    nameSpaceList = v1.list_namespace()

    for nameSpace in nameSpaceList.items:
        namespaces_list.append(nameSpace.metadata.name)
    return namespaces_list


#check if namespace exists
# check if is namespace active
def namespace_check(instiate_CNF_namespace):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("-------- Check if namespace exists, if no exist then create ")
    print("-------- If namespace isn't active then exits ")


    if instiate_CNF_namespace in get_namespaces(v1):
        exist_namespace = v1.read_namespace(instiate_CNF_namespace)
        if exist_namespace.status.phase == 'Active':
            print("Namespace is active")
        else:
            print("Namespace isn't active")

            return exit()
    else:

        v1.create_namespace(client.V1Namespace(metadata=client.V1ObjectMeta(name=instiate_CNF_namespace)))
        time.sleep(3)

        if instiate_CNF_namespace in get_namespaces(v1):

            exist_namespace = v1.read_namespace(instiate_CNF_namespace)
            if exist_namespace.status.phase == 'Active':
                print("Namespace is active")
            else:
                print("Namespace isn't active")

                return exit()


