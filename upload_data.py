import wandb

# Initialize W&B run
run = wandb.init(
    project="nyc_airbnb", 
    job_type="upload-dataset"
)

# Create artifact with the exact name the test suite is looking for
artifact = wandb.Artifact(
    name="nyc_airbnb", 
    type="dataset"
)

# Add local file from  root directory
artifact.add_file("clean_sample.csv") 

# Log and tag with the 'latest' alias
run.log_artifact(artifact, aliases=["latest"])
run.finish()

print("Dataset successfully uploaded to W&B as 'nyc_airbnb:latest'!")