import requests
import os

base_url = "https://cdn.converteai.net/95571f87-0880-4710-aa13-bcbffe9545e6/6682239208bf60000baeebfd/original_720p"
data_dir = "data"
list_path = "list.txt"

if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

i = 1
response = requests.get(f"{base_url}/segment__{i:05}.ts")
while response.status_code == 200:
    with open(list_path, "a") as f:
        f.write(f"file './{data_dir}/segment__{i:05}.ts'\n")
    with open(f"{data_dir}/segment__{i:05}.ts", "wb") as f:
        f.write(response.content)
    i += 1
    response = requests.get(f"{base_url}/segment__{i:05}.ts")
