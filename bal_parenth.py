def brackets_balanced(s):
   stack = []
   for ch in s:
       if ch in ('(','{','['):
           stack.append(ch)
       else:
           if stack and(stack[-1]=='(' or ch==')' or stack[-1]=='{' or ch=='}' or stack[-1] =='[' or chr ==']'):
                 stack.pop()
           else:
               return False
   return not stack

expr = "{()}[]"
print(brackets_balanced(expr))