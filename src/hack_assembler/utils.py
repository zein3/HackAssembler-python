# This file contains helper functions for the Hack Assembler.

def allocate_memory(memory: dict, var: str):
    """
    Find a free place in memory and allocate var to it
    If there is no available memory raise an exception
    """
    for i in range(16, 16384):
        # if i is free in memory
        allocated_memory = memory.values()
        if i not in allocated_memory:
            # then allocate var to it and return
            memory[var] = i
            return

    # raise an exception if there is no free memory
    raise Exception("Run out of memory.")
