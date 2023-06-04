import os
import sys

def create_tree_diagram(start_path=None, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = []

    if start_path is None:
        start_path = os.getcwd()

    def _create_tree_diagram(path, prefix=''):
        entries = sorted(os.listdir(path))
        for i, entry in enumerate(entries):
            if entry in exclude_dirs:
                continue

            is_last = i == len(entries) - 1
            new_prefix = prefix + ('└── ' if is_last else '├── ')

            if os.path.isdir(os.path.join(path, entry)):
                _create_tree_diagram(os.path.join(path, entry), prefix + ('    ' if is_last else '│   '))

    _create_tree_diagram(start_path)


if __name__ == '__main__':
    if not os.path.exists('directory_structure'):
        sys.stdout = open('directory_structure', 'w')
    create_tree_diagram(exclude_dirs=['.git', 'dist', 'build', 'node_modules', '__pycache__', '*.egg-info', 'venv'])
    sys.stdout.close()
