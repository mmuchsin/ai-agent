import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_dir: str = os.path.abspath(working_directory)
        abs_file_path: str = os.path.normpath(os.path.join(abs_working_dir, directory))
        valid_abs_file_path = (
            os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir
        )
        if not valid_abs_file_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_file_path):
            return f'Error: "{directory}" is not a directory'
        return describe_directory(abs_file_path)
    except Exception as e:
        return f"Error: {e}"


def describe_directory(dir_path):
    entries = os.listdir(dir_path)
    lines = []
    for entry_name in entries:
        full_path = os.path.join(dir_path, entry_name)
        # figure out size here
        file_size = os.path.getsize(full_path)
        # figure out is_dir here
        is_dir = os.path.isdir(full_path)
        # build a formatted line and add it to lines
        line = f"- {entry_name}: file_size={file_size} bytes, is_dir={is_dir}"
        lines.append(line)

    # join lines together and return
    return "\n".join(lines)


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
