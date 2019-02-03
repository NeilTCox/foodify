#!/usr/bin/env python3
"""
A simple blockchain
"""
__author__ = "Neil Schultz-Cox"

import hashlib
import datetime
from collections import defaultdict

class Blockchain:
    def __init__(self, genesis_block_data):
        self.chain = {}
        self.genesis_block = Block(0, datetime.datetime.now(), genesis_block_data, hashlib.sha256("-1".encode('utf-8')).hexdigest())
        self.chain[self.genesis_block.hash] = self.genesis_block
        self.last_block = self.genesis_block

    def export_chain(self):
        return (self.genesis_block.hash, self.last_block.hash, self.chain)

    def import_chain(self, genesis_block_hash, last_block_hash, chain):
        self.chain = chain
        self.genesis_block = self.explore_block(genesis_block_hash)
        self.last_block = self.explore_block(last_block_hash)

    def add_block(self, data):
        this_index = self.last_block.index + 1
        this_timestamp = datetime.datetime.now()
        this_data = data
        last_hash = self.last_block.hash
        new_block = Block(this_index, this_timestamp, this_data, last_hash)
        self.chain[new_block.hash] = new_block
        self.last_block = new_block
        return new_block

    def explore_chain(self):
        block = self.last_block
        if block.index == 0:
            return [block]
        chain = []
        while block.index > 0:
            chain.append(block)
            block = self.chain[block.previous_hash]
        chain.append(block)
        return chain

    def explore_block(self, hash):
        return self.chain[hash]

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        return hashlib.sha256( (\
        str(self.index) + \
        str(self.timestamp) + \
        str(self.data) + \
        str(self.previous_hash)).encode('utf-8')).hexdigest()
    
    def __str__(self):
        return "================================" \
        + "\nIndex: " + str(self.index) \
        + "\nTimestamp: " + str(self.timestamp) \
        + "\nData: " + self.data \
        + "\nPrevious Hash: " + str(self.previous_hash) \
        + "\nHash: " + str(self.hash) \
        + "\n================================"