# Module for signing the ballots.
# Pseudo-code Stage 0

# @author: jethroFloyd // Ritobroto Maitra

# Input Format: ASCII-encoded ballot file, Name, Roll Number
# Step 0: Concatenate the three inputs
# Step 1: Call SHA256 from PyCrypto on the Concatenatation
# Step 2: Output the digest to HashBallot
# Step 3:  Encrypt the HashBallot with Private Key
# Step 4: Generate Hash of Encrypted HashBallot.
# Step 5: Concatenate RandomHash with Encrypted Hash Ballot and the Roll Number.
# Step 6: Send over to transmission module.