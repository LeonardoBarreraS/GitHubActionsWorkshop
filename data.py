from azure.ai.ml import MLClient
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