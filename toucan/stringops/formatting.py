

def chunk_list(lst: list, chunk_size: int, invert_chunks: bool=False) -> list:
    """
    Chunk a list
    """
    n_items = len(lst)
    if invert_chunks:
        chunk_size = n_items // chunk_size
    indices = list(range(0, n_items+1, chunk_size))
    if n_items % chunk_size:
        indices.append(n_items)
    
    chunked = [lst[i:j] for i, j in zip(indices[:-1], indices[1:])]

    if invert_chunks:
        last = chunked[-1]
        chunked = list(zip(*chunked[:-1]))
        for i, x in enumerate(last):
            chunked[i] = [*chunked[i], x]

    return chunked
    

def columns_of_strings(lst: list, direction: str='col', spaces: int=4, 
                        output_width: int=100, align: str='left') -> str:
    """
    Return a list of strings formatted into columns.

    Parameters
    ----------
    direction:
        list items down ('col') or across ('row')
    spaces:
        Number of spaces to leave between columns
    output_width:
        Number of characters per row
    """
    
    if direction == 'col':
        invert = True
    elif direction == 'row':
        invert = False
    else:
        raise NotImplementedError("Only supports direction='row' or direction='col'")
    
    if align == 'left':
        align_fmt = ''
    elif align == 'right':
        align_fmt='>'
    else:
        raise NotImplementedError("Only supports align='left' or align='right'")
    
    str_list = list(map(str, lst))
    longest = max(map(len, str_list))
    ncol = output_width // (longest + spaces)
    formatted = ['{:{align}{width}}'.format(x, align=align_fmt, width=longest) for x in str_list]
    
    chunks = chunk_list(formatted, ncol, invert_chunks=invert)
    
    buffer = ' '*spaces
    rows = [buffer.join(x) for x in chunks]
    output = "\n".join(rows)
    return output

def print_columns(*args, **kwargs):
    """
    Print a list in columns.

    See also
    --------
    columns_of_strings
    """
    output = columns_of_strings(*args, **kwargs)
    print(output)