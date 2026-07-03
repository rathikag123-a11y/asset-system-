# Remote Asset Tracking and Management

print("===== Remote Asset Tracking and Management =====")

asset_id = input("Enter Asset ID: ")
asset_name = input("Enter Asset Name: ")
location = input("Enter Asset Location: ")
status = input("Enter Asset Status (Active/Inactive): ")

print("\n----- Asset Details -----")
print("Asset ID      :", asset_id)
print("Asset Name    :", asset_name)
print("Location      :", location)
print("Status        :", status)

if status.lower() == "active":
    print("Tracking Status: Asset is Active and Tracked Successfully.")
else:
    print("Tracking Status: Asset is Inactive.")