from Rational import Rational


def evaluate_rational_expression(expression):
    for op in ['+', '-', '*', '/']:
        expression = expression.replace(op, f' {op} ')

    parts = expression.split()
    processed_parts = []

    for part in parts:
        if part in ['+', '-', '*', '/']:
            processed_parts.append(part)
        else:
            processed_parts.append(f'Rational("{part}")')
    final_expr = " ".join(processed_parts)
    return eval(final_expr)

