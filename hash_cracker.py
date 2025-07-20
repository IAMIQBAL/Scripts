import hashlib
import sys

def crack(hash, algo, wordlist_path):
    with open(wordlist_path, "r") as f:
        for word in f:
            gen_hash = hashlib.new(algo, word.strip().encode()).hexdigest()
            if gen_hash == hash:
                print(f"Password Found: {word.strip()}")
                f.close()
                exit(0)
            
 
crack(sys.argv[1], sys.argv[2], sys.argv[3])