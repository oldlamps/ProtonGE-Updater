import requests
import subprocess

# Get the latest release information from the GitHub API
url = "https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases/latest"
response = requests.get(url)
release_info = response.json()

# Find the first asset with the '.tar.gz' file extension
asset = None
for a in release_info["assets"]:
    if a["name"].endswith(".tar.gz"):
        asset = a
        break

if asset:
    # Extract the version number and download URL from the asset
    version = release_info["tag_name"]
    download_url = asset["browser_download_url"]

    print("The latest version is:", version)
    print("Download URL:", download_url)

    # Prompt the user to download the file
    answer = input("Do you want to download the file (y/n)? ")
    if answer.lower() == "y":
        subprocess.run(["curl", "-LJO", download_url])
        print("Download complete.")
else:
    print("No tar.gz file found in the latest release.")
