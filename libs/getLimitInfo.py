from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

cl = client.CoreV1Api()
limits = cl.list_limit_range_for_all_namespaces()

def getlimitinfo() :
    limitsinfo = []
    for limit in limits.items:
        limitsinfo.append([limit.metadata.name, limit.metadata.namespace, limit.spec.limits[0].default])
    return limitsinfo