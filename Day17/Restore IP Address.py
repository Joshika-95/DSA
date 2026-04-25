def restore_ip(s):
    result = []
    def backtrack(index, parts, current):
        # If 4 parts formed AND all digits used
        if parts == 4 and index == len(s):
            result.append(current[:-1])  # remove last dot
            return
        # If more than 4 parts → stop
        if parts > 4:
            return
        # Try 1 to 3 digits
        for i in range(1, 4):
            # If index exceeds length → stop
            if index + i > len(s):
                break
            # Take substring
            part = s[index:index+i]
            # Check invalid cases
            if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                continue
            # Choose and move forward
            backtrack(index + i, parts + 1, current + part + ".")
    backtrack(0, 0, "")
    return result
print(restore_ip("25525511135"))