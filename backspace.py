def backSpaceCompare(s,t):
    def proccessString(s):
        stack = []
        for char in s:
            if char != '#':
                stack += [char]
            elif stack:
                stack.pop()
        return ''.join(stack)
    return proccessString(s) == proccessString(t)

# Problem 5: Backspace String Compare
print(backSpaceCompare("ab#c", "ad#c"))  # Output: True
print(backSpaceCompare("ab##", "c#d#"))  # Output: True
print(backSpaceCompare("a#c#", "b#"))  # Output: False