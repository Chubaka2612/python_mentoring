def file_size(bytes): 
    mod = 1024

    kilo_bytes = mod
    mega_bytes = mod ** 2
    giga_bytes = mod ** 3
    if bytes < kilo_bytes:
       return "{:.1f}B".format(bytes)
    elif bytes < mega_bytes:
       return "{:.1f}Kb".format(bytes / kilo_bytes)
    elif bytes < giga_bytes:
       return "{:.1f}Mb".format(bytes / mega_bytes)
    else:
       return "{:.1f}Gb".format(bytes / giga_bytes)