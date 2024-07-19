# Git Bash encryption steps


# Create ENCRYPTION_KEY with python

ENCRYPTION_KEY=$(python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")

# Print key for sharing

echo "Generated encryption key: $ENCRYPTION_KEY"

# save key to a file 

echo $ENCRYPTION_KEY > ekey.txt

# Export key as enviorment variable

export ENCRYPTION_KEY=$ENCRYPTION_KEY

# Print message telling  key is set

echo "Encryption key set as environment variable ENCRYPTION_KEY"

# make script executable and run it 
