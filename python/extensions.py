# Define a dictionary to map file extensions to media types
extension_to_media = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Prompt the user for a file name
file_name = input("File name: ").strip()

# Extract the file extension (case-insensitively)
# Use rpartition to split at the last period
base, sep, ext = file_name.rpartition(".")

# Check if there was an extension
if sep == ".":  # This means there was a period before the extension
    ext = f".{ext.lower()}"  # Ensure the extension is lower case
    # Output the corresponding media type if it exists, else default
    print(extension_to_media.get(ext, "application/octet-stream"))
else:
    # No extension found
    print("application/octet-stream")
