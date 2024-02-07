def _check_and_accumulate_row_values(row: list[str], checks: list[str], 
                                     cols_names: list[str]) -> int:
    sign_sc = {
            "<": lambda cell, value: int(cell)<int(value),
            ">": lambda cell, value: int(cell)>int(value)
            }
    for check in checks:
        col_name, sign, value = check.split(' ')
        cell = row[cols_names.index(col_name)]
        if not sign_sc[sign](cell, value):
            return 0
    else:
        return sum([int(cell) for cell in row])


def main(input: str) -> str:
    amounts, cols_names, data_and_checks = input.split('\n', maxsplit=2)
    cols_names = cols_names.split(' ')
    rows, _ = amounts.split(' ', maxsplit=1)
    data_and_checks = data_and_checks.split('\n')
    data = data_and_checks[:int(rows)]
    data = [elem.split(' ') for elem in data]
    checks = data_and_checks[int(rows):]
    filtered_rows_sums = list(map(
        lambda row: _check_and_accumulate_row_values(row, checks, cols_names), data))
    results_sum = sum(filtered_rows_sums)
    return str(results_sum)
