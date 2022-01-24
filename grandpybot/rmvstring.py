def remove_nested_parens(input_str):
    """Returns a copy of 'input_str' with any parenthesized text removed. Nested parentheses are handled."""
    result = ''
    paren_level = 0
    for ch in input_str:
        if ch == '(':
            paren_level += 1
        elif (ch == ')') and paren_level:
            paren_level -= 1
        elif not paren_level:
            result += ch
    return result
