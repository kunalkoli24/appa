# Write a program to implement Huffman Encoding using a greedy strateg

import heapq
from collections import Counter

# Define the Node structure for the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(frequencies):
    # Create a priority queue with initial nodes for each character
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    # Combine nodes until only one node (the root) remains
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # Create a new node with combined frequency
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
        
    return heap[0] if heap else None

# Function to generate codes from Huffman Tree
def generate_codes(node, prefix="", code_map={}):
    if node is None:
        return
    if node.char is not None:
        code_map[node.char] = prefix  # Leaf node, save the code
    generate_codes(node.left, prefix + "0", code_map)
    generate_codes(node.right, prefix + "1", code_map)
    return code_map

# Main Huffman Encoding function
def huffman_encoding(text):
    if not text:
        return "", {}

    # Calculate character frequencies
    frequencies = Counter(text)
    
    # Build Huffman Tree
    root = build_huffman_tree(frequencies)

    # Generate codes
    huffman_codes = generate_codes(root)
    
    # Encode the text using the generated codes
    encoded_text = "".join(huffman_codes[char] for char in text)

    return encoded_text, huffman_codes

# Take input from user
text = input("Enter the text to encode: ")

# Perform Huffman Encoding
encoded_text, huffman_codes = huffman_encoding(text)

# Display results
print("\nCharacter codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
print("\nEncoded text:", encoded_text)
