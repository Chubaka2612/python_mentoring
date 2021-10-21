def file_size(test_bytes):
    mod = 1024

    kilo_bytes = mod
    mega_bytes = mod ** 2
    giga_bytes = mod ** 3
    if test_bytes < kilo_bytes:
        return "{:.1f}B".format(test_bytes)
    elif test_bytes < mega_bytes:
        return "{:.1f}Kb".format(test_bytes / kilo_bytes)
    elif test_bytes < giga_bytes:
        return "{:.1f}Mb".format(test_bytes / mega_bytes)
    else:
        return "{:.1f}Gb".format(test_bytes / giga_bytes)
