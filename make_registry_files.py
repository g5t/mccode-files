
def register(directory):
    from pathlib import Path
    from pooch import make_registry
    if not isinstance(directory, Path):
        directory = Path(directory)

    if not directory.exists() or not directory.is_dir():
        raise RuntimeError(f'{directory} can not be registered because it does not exist as a directory')

    file = directory.parent.joinpath(f'{directory.stem}-registry.txt')

    make_registry(directory, file)


if __name__ == '__main__':
    for directory in ('mcstas', 'mcxtrace', 'runtime/libc'):
        register(directory)
