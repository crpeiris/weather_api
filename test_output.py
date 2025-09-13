import os

print("### Test 1: Hello, World! ###")

api_key = os.environ.get("GOOGLE_MAPS_API_KEY", "NOT SET")
print(f"### Test 2: The API Key is: {api_key} ###")

if api_key == "NOT SET":
    print("### The environment variable is NOT set. ###")
else:
    print("### The environment variable IS set. ###")
