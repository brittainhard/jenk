from unittest.mock import Mock, MagicMock
import boto
from boto import ec2
from boto.ec2 import cloudwatch


ids = ["i-011ea983a6f869c75"]
sid="AKIAIQE36FLD6ZCKDPAQ"
key="gmFu8dzYiDuWkvJXJCtJPLGlzLSiCS6u9BJ5F9dP"

conn = ec2.connect_to_region("us-west-2", aws_access_key_id=sid, aws_secret_access_key=key)
cloud = cloudwatch.connect_to_region("us-west-2", aws_access_key_id=sid, aws_secret_access_key=key)
stat = conn.get_all_instance_status()[0]
metrics = cloud.list_metrics()
mon = conn.monitor_instances(instance_ids=ids)[0]

def get_metrics(metrics, ids):
    metrics_list = []
    for metric in metrics:
        if metric.dimensions and metric.dimensions.get("InstanceId", None) == ids:
            metrics_list.append(metric)
    return metrics_list