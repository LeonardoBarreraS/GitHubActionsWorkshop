import azure.ai.ml
from azure.ai.ml import MLClient, Input, Output
from azure.ai.ml.entities import Workspace, AmlCompute
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential, AzureCliCredential
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import load_component
from azure.ai.ml.constants import AssetTypes

from azure.ai.ml.sweep import (
    Choice,
    Uniform
)

# NOTE:  set your workspace name here!
workspace_name="Leogithubactions"
# NOTE:  if you do not have a cpu-cluster already, we will create one
# Alternatively, change the name to a CPU-based compute cluster
cluster_name="cpu-cluster-leo86"

# NOTE:  for local runs, I'm using the Azure CLI credential
# For production runs as part of an MLOps configuration using
# Azure DevOps or GitHub Actions, I recommend using the DefaultAzureCredential
#ml_client=MLClient.from_config(DefaultAzureCredential())
ml_client=MLClient.from_config(AzureCliCredential())
ws=ml_client.workspaces.get(workspace_name)

cpt_asset=ml_client.data.get(name="ChicagoParkingTicketsFolder4", version="initial")

