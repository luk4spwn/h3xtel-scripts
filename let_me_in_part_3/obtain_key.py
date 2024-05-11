flag_in_bytes = bytes.fromhex("db5cb1b5563cf5015a9c94703be8c3a0a7c0615caec4978d948944d9c79dad95743bd9f59b69828e")

print(bytes([(flag_in_bytes[0] - ord("H")) % 256]))
print(bytes([(flag_in_bytes[1] - ord("3")) % 256]))
print(bytes([(flag_in_bytes[2] - ord("x")) % 256]))
print(bytes([(flag_in_bytes[3] - ord("T")) % 256]))
print(bytes([(flag_in_bytes[4] - ord("E")) % 256]))
print(bytes([(flag_in_bytes[5] - ord("L")) % 256]))
print(bytes([(flag_in_bytes[6] - ord("{")) % 256]))
