def chunk_string(input_string, chunk_size=1000):
    return [input_string[0+i:chunk_size+i] for i in range(0, len(input_string), chunk_size)]
