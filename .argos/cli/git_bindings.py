import re
from enum import Enum
from os import path

from utils.cmd_executor import CmdExecutor


class MergeFileResultKind(Enum):
    SUCCESS = 0
    CONFLICTS = 1
    ERROR = 2


class GitBindings:
    def __init__(self):
        pass

    def clone(self, repo_url: str, destination_path: str) -> None:
        """
        Clones a git repository from the given URL to the specified destination path.
        """
        if path.exists(destination_path):
            raise FileExistsError(
                f"Destination path '{destination_path}' already exists."
            )

        res = CmdExecutor(["git", "clone", repo_url, destination_path]).execute()
        if res.returncode != 0:
            raise RuntimeError(
                f"Failed to clone repository from '{repo_url}' to '{destination_path}'. Error: {res.stderr}"
            )

    def pull(self, repo_path: str) -> None:
        """
        Pulls the latest changes from the remote repository for the given local repository path.
        """
        if not path.exists(repo_path):
            raise FileNotFoundError(f"Repository path '{repo_path}' does not exist.")

        res = CmdExecutor(["git", "-C", repo_path, "pull"]).execute()
        if res.returncode != 0:
            raise RuntimeError(
                f"Failed to pull latest changes for repository at '{repo_path}'. Error: {res.stderr}"
            )

    def is_repository_clean(self, repo_path: str) -> bool:
        """
        Checks if the ARGOS repository at the given path has no uncommitted changes.
        Returns True if the repository is clean, False otherwise.
        To tell that a repository is clean, we check dirty files in .argos/exercises and Exercises directory.
        """
        if not path.exists(repo_path):
            raise FileNotFoundError(f"Repository path '{repo_path}' does not exist.")

        res = CmdExecutor(
            ["git", "ls-files", "--others", "--modified", "--exclude-standard"]
        ).execute()
        if res.returncode != 0:
            raise RuntimeError(
                f"Failed to check repository status at '{repo_path}'. Error: {res.stderr}"
            )

        files = res.stdout.splitlines() if res.stdout else []

        if any(
            f.startswith(".argos/exercises/") or f.startswith("Exercises/")
            for f in files
        ):
            return False

        return True

    def merge_file(
        self, file_to_change: str, original_file: str, new_file: str
    ) -> MergeFileResultKind:
        """
        Merges the content of the new file into the file to change, using the original file as a base.
        Returns True if the merge was successful, False if there were conflicts that need to be resolved manually.
        """
        if (
            not path.exists(file_to_change)
            or not path.exists(original_file)
            or not path.exists(new_file)
        ):
            raise FileNotFoundError("One or more files do not exist for merging.")

        res = CmdExecutor(
            [
                "git",
                "merge-file",
                file_to_change,
                original_file,
                new_file,
            ]
        ).execute(
            output_on_error=True,
            output_on_error_predicate=lambda code: code < 0 or code > 127,
        )

        if res.returncode < 0 or res.returncode > 127:
            return MergeFileResultKind.ERROR

        if res.returncode == 0:
            return MergeFileResultKind.SUCCESS

        return MergeFileResultKind.CONFLICTS

    def set_hooks_dir(self, hooks_dir: str) -> bool:
        """
        Sets the hooks directory for the repository.
        Returns True if the operation was successful, False otherwise.
        """
        res = CmdExecutor(
            [
                "git",
                "config",
                "core.hooksPath",
                hooks_dir,
            ]
        ).execute(output_on_error=False)

        return res.returncode == 0

    def get_user_name(self) -> str | None:
        res = CmdExecutor(["git", "config", "user.name"]).execute(output_on_error=False)
        if res.returncode != 0:
            return None
        return res.stdout.strip() if res.stdout is not None else None

    def get_github_username(self) -> str | None:
        res = CmdExecutor(["git", "remote", "get-url", "origin"]).execute(
            output_on_error=False
        )
        if res.returncode != 0:
            return None
        match = re.search(
            r"github\.com[:/]([^/]+)/",
            res.stdout.strip() if res.stdout is not None else "",
        )
        return match.group(1) if match else None

    def get_hooks_dir(self) -> str | None:
        """
        Returns the hooks directory for the repository, or None if not set.
        """
        res = CmdExecutor(
            [
                "git",
                "config",
                "core.hooksPath",
            ]
        ).execute(output_on_error=False)

        if res.returncode != 0:
            return None

        return res.stdout.strip() if res.stdout else None

    def check_repository_exists(self, repo_url: str) -> bool:
        """
        Checks if a repository exists and/or is reachable
        """
        res = CmdExecutor(["git", "ls-remote", repo_url]).execute(output_on_error=False)

        return res.returncode == 0
