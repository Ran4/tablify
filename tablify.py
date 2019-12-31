from typing import List, Dict, Iterable, Any
from collections import Counter

ColumnIdx = int

def find_column_sizes(lines: List, padding=0) -> Dict[ColumnIdx, int]:
    column_sizes: Counter = Counter()
    
    # Find the largest column width for every column
    for line in lines:
        for column_idx, item in enumerate(line):
            if len(item) > column_sizes[column_idx]:
                column_sizes[column_idx] = len(item)
                
    # Add padding if needed
    if padding:
        for key in column_sizes:
            column_sizes[key] += padding
    
    return dict(sorted(column_sizes.items(), key=lambda key: key))


def tablify(data: Iterable[Iterable[Any]]) -> str:
    """
    Formats data into a string that looks like a table.
    
    
    Example output:
    
    | Name     | Hitrate | Hitrate'  | Rolls
    |----------|---------|-----------|---------
    | Meh      | 43%     | 1 in 1.02 | Shield 4
    """
    all_lines: List[List[str]] = [[str(x) for x in row] for row in data if row]
    
    header: List[str]
    lines: List[List[str]]
    header, *lines = all_lines
    
    column_sizes: Dict[ColumnIdx, int] = \
        find_column_sizes(all_lines, padding=1)
        
    header_string: str = "".join(
        ("| " + item).ljust(column_sizes[col_idx] + len("| "))
        for col_idx, item in enumerate(header))
    
    divider_string: str = "".join(
        "|" + "-" * (column_sizes[col_idx] + 1)
        for col_idx in range(len(header)))
    
    body_strings: List[str] = ["".join(
        ("| " + item).ljust(column_sizes[col_idx] + len("| "))
        for col_idx, item in enumerate(line))
        for line in lines]

    return "\n".join([
        header_string,
        divider_string,
        *body_strings,
    ])



if __name__ == "__main__":
    table_string = tablify(
        [
            ["Name", "Hitrate", "Hitrate'", "Rolls"],
            ["Meh", "43%", "1 in 1.02", "Shield 4"],
        ]
    )
    print(table_string)
