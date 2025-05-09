import hashlib
import time

class Block:
    def __init__(self, data, prev_hash=''):
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        info = str(self.timestamp) + self.data + self.prev_hash
        return hashlib.sha256(info.encode()).hexdigest()

block1 = Block("First block data")
block2 = Block("Second block data", block1.hash)

print("Block 1 Hash:", block1.hash)
print("Block 2 Hash:", block2.hash)

print("Block 1 Previous Hash:", block1.prev_hash)
print("Block 2 Previous Hash:", block2.prev_hash)

print("Block 1 Data:", block1.data) 
print("Block 2 Data:", block2.data)

print("Block 1 Timestamp:", block1.timestamp)
print("Block 2 Timestamp:", block2.timestamp)



# Simulating a DLT with two nodes

blockchain = []
blockchain.append(block1)
blockchain.append(block2)

node2_chain = blockchain.copy()

print("Node 1 Blockchain:", blockchain)
print("Node 2 Blockchain:", node2_chain)
