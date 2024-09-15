from azure.ai.ml import MLClient
from azure.ai.ml.constants import BatchDeploymentOutputAction
from azure.identity import DefaultAzureCredential

# Inicializar el cliente de ML
credential = DefaultAzureCredential()
ml_client = MLClient.from_config(credential)

# Nombre del endpoint y deployment que deseas eliminar
endpoint_name = "chicago-parking-tickets-batch"
deployment_name = "cpt-batch-deployment"

# Obtener el endpoint
endpoint = ml_client.batch_endpoints.get(endpoint_name)

# Eliminar el deployment existente
ml_client.batch_deployments.begin_delete(
    name=deployment_name,
    endpoint_name=endpoint_name
).result()


"""from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# authenticate
credential = DefaultAzureCredential()

# Get a handle to the workspace
ml_client = MLClient(
    credential=credential,
    subscription_id="1d100390-d502-435b-9d18-5d2002a57d9d",
    resource_group_name="leonardobarrera.s-rg",
    workspace_name="Leogithubactions",
)

ws=ml_client.workspaces.get("Leogithubactions")
print(f"workspace:{ws.name}")

endpoint = ml_client.batch_endpoints.get("chicago-parking-tickets-batch")
print(f"Endpoint '{endpoint.name}' exists.")



from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# update the 'my_path' variable to match the location of where you downloaded the data on your
# local filesystem

my_path = "./data"
# set the version number of the data asset
v1 = "initial"

my_data = Data(
    name="ChicagoParkingTicketsFolder4",
    version=v1,
    description="Chicago Parking Ticket",
    path=my_path,
    type=AssetTypes.URI_FOLDER,
)

## create data asset if it doesn't already exist:
try:
    data_asset = ml_client.data.get(name="ChicagoParkingTicketsFolder4", version=v1)
    print(
        f"Data asset already exists. Name: {my_data.name}, version: {my_data.version}"
    )
except:
    ml_client.data.create_or_update(my_data)
    print(f"Data asset created. Name: {my_data.name}, version: {my_data.version}")
"""




    