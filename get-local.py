from clearml import Dataset

# Define dataset_metadata (or get it from Task, config, etc.)
dataset_metadata = {
    'test1': '30514d27993b4c9cbe9e9e6ed6eced6a'  # Replace with actual dataset ID
}

# Assuming you already have the dataset_id
train_dataset_id = dataset_metadata.get('test1', '')

if not train_dataset_id:
    raise ValueError("Dataset ID not found in dataset_metadata")

# Get the dataset object using the dataset_id
train_dataset = Dataset.get(dataset_id=train_dataset_id)

# Get the name of the dataset
dataset_name = train_dataset.name
print(f"Dataset Name: {dataset_name}")

# Download the dataset locally
local_path = train_dataset.get_local_copy()
print(f"Dataset downloaded to: {local_path}")

#list 
files = train_dataset.list_files()
print(f"Files in dataset: {files}")