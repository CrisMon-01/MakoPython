from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
pods = v1.list_pod_for_all_namespaces(watch=False)

def getpodinfo() :
    podinfo = []
    for pod in pods.items:
        podinfo.append([pod.metadata.name,pod.spec.node_name])
    return podinfo