"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""


def valid_parentheses(s: str) -> bool:
    """
    :param s: A string containing just the characters '(', ')', '{', '}', '[' and ']'
    :return:bool
    """
    # 使用栈结构，一个列表只使用append和pop可以当成栈
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            # 取栈顶
            top = stack.pop() if stack else "#"
            # 栈顶：(.{,[
            if mapping[char] != top:
                return False

        else:
            # 添加(,[,{
            stack.append(char)

    return not stack


if __name__ == "__main__":
    print(valid_parentheses('({)}'))
