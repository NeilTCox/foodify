from tinychain import Blockchain

def main():
    blockchain = Blockchain("GENESIS BLOCK")

    print("\nExploring blockchain:")
    chain = blockchain.explore_chain()

    for block in chain:
        print(block)
    
    print("\nAdding blocks...")
    for i in range(0, 5):
        blockchain.add_block("I'M BLOCK #" + str(i))
    
    print("\nExploring blockchain:")
    chain = blockchain.explore_chain()

    for block in chain:
        print(block)

if __name__ == "__main__":
    main()