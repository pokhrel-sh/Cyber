# Define file paths
shadow_file = "shadow.txt"
decrypted_file = "answers.txt"
output_file = "output.txt"

# Read shadow file and create a dictionary mapping hash to username
hash_to_user = {}
all_users = {}  # Stores all usernames and their hashes for later use
with open(shadow_file, "r") as sf:
    for line in sf:
        parts = line.strip().split(":")
        if len(parts) == 2:
            username, hash_value = parts
            hash_suffix = "$".join(hash_value.split("$")[1:])  # Extract hash without prefix
            hash_to_user[hash_suffix] = username
            all_users[username] = hash_value  # Store full hash for unmatched users

# Read decrypted file and match hashes to extract passwords
matched_users = set()
output_lines = []
with open(decrypted_file, "r") as df:
    for line in df:
        parts = line.strip().split(":")
        if len(parts) == 2:
            hash_value, password = parts
            hash_suffix = "$".join(hash_value.split("$")[1:])  # Extract hash without prefix
            if hash_suffix in hash_to_user:
                username = hash_to_user[hash_suffix]
                output_lines.append(f"{username}:{password}")
                matched_users.add(username)  # Mark this user as matched

# Add unmatched users at the bottom with their original hash
for username, hash_value in all_users.items():
    if username not in matched_users:
        output_lines.append(f"{username}:{hash_value}")

# Write to output file
with open(output_file, "w") as of:
    of.write("\n".join(output_lines) + "\n")

print(f"Processed {len(output_lines)} entries. Output saved to {output_file}.")
