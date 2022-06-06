from commands.commands import exec_command
from commands.checker import namespace_check


def instiate_CNF(commands,NAMESPACE,NAME_HELM_DEP,CHART_NAME_URL, CHART_VALUES_URL):
    #command on instiate CNF
    instiate_CNF_command=commands[1]
    instiate_CNF_command = instiate_CNF_command.replace('{NAMESPACE}', NAMESPACE)
    instiate_CNF_command = instiate_CNF_command.replace('{NAME_HELM_DEP}', NAME_HELM_DEP)
    instiate_CNF_command = instiate_CNF_command.replace('{CHART_NAME_URL}', CHART_NAME_URL)
    instiate_CNF_command = instiate_CNF_command.replace('{CHART_VALUES_URL}', CHART_VALUES_URL)
    #print(instiate_CNF_command)

    #Extract namespace and check if is namespace created , if no create, if not active stop script
    instiate_CNF_namespace=NAMESPACE
    namespace_check(instiate_CNF_namespace)

    deployment_check = exec_command(instiate_CNF_command)
    print("-------- Iniciate CNF")
    print(f'Implementation of command: {instiate_CNF_command}')
    print("\n".join(deployment_check))






