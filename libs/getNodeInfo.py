from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
nodes = v1.list_node(watch=False)

def getnodeinfo() :
    nodeinfo = []
    for node in nodes.items:  
        nodeinfo.append([node.metadata.cluster_name, node.metadata.name, node.status.node_info.os_image, node.status.addresses[0].address])
    return nodeinfo