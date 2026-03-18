from endee_store import add_documents

# Read your notes file
with open("notes.txt", "r") as f:
    notes = f.readlines()

# Add to Endee
add_documents(notes)

print("✅ Notes successfully added to Endee")