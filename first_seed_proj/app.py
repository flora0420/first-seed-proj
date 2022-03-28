"""first_seed_proj.app: Skeleton of a function."""


def main(str_torepeat: str, n_rep: int) -> str:
    """return a string that repeat the given str n times

    Args:
        str_torepeat (str): [description]
        n_rep (int): [description]

    Returns:
        str: [description]
    >>> from first_seed_proj.app import main
    >>> assert main('a', 3) == 'aaa'
    """
    return str_torepeat * n_rep
