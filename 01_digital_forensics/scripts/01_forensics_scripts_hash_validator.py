# Automation of MD5 and SHA1 verification

# Import Libraries
import hashlib
import sys

def calculate_hashes(file_path):
    """Calculates MD5 and SHA1 hashes for a given file to ensure forensic integrity."""
    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()

    try:
        with open(file_path, "rb") as f:
            # Read file in chunks to handle large forensic images
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha1_hash.update(byte_block)
        
        print(f"File: {file_path}")
        print(f"MD5:  {md5_hash.hexdigest()}")
        print(f"SHA1: {sha1_hash.hexdigest()}")
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        calculate_hashes(sys.argv[1])
    else:
        print("Usage: python hash_validator.py <file_path>")