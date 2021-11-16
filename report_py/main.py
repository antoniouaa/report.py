import re
import shlex
import pathlib
import subprocess
from collections import defaultdict

from rich.tree import Tree
from rich.table import Table

from report_py.console import console
from report_py.argument_parser import assemble_parser


def parse_log(log: list[str]) -> dict[str, list[str]]:
    topics = defaultdict(list)
    pattern = r"(.*) \[(.*)\] (.*)"
    for commit in log:
        matches = re.match(pattern, commit)
        if matches:
            tags = matches.groups()[1].split(", ")
        else:
            continue
        for tag in tags:
            commit_hash = matches.groups()[0].strip()
            commit_message = matches.groups()[-1].strip()
            topics[tag].append((commit_hash, commit_message))
    return topics


def get_git_log(args) -> list[str]:
    commits = subprocess.run(
        shlex.split('git log --oneline --since "1 week ago"'),
        shell=True,
        capture_output=True,
    ).stdout
    commits = commits.decode("utf-8").splitlines()
    return commits


def attach_to_tree(tree: Tree, mapping: dict[str, list[tuple[str, str]]]) -> None:
    for topic, messages in mapping.items():
        table = Table(title=topic)
        table.add_column("Commit Hash", justify="left")
        table.add_column("Message", justify="left")
        for hash_, message in messages:
            table.add_row(hash_, message)
        tree.add(table, style=topic.lower())


def get_repo_name():
    name = subprocess.run(
        [
            "git",
            "remote",
            "get-url",
            "origin",
        ],
        capture_output=True,
    ).stdout
    return pathlib.Path(name.decode("utf-8")).name[:-5]


def run() -> None:
    cliparser = assemble_parser()
    args = cliparser.parse_args()

    repo_name = get_repo_name()

    tree = Tree(f":seedling: {repo_name}", highlight=True)
    commits = get_git_log(args)
    topics = parse_log(commits)
    attach_to_tree(tree, topics)
    console.print(tree)
