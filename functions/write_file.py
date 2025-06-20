import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = abs_working_dir
    if file_path:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        try:
            f = open(abs_file_path, "x")
        except Exception as e:
            return f'Error: creating file "{file_path}": {e}'
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Succesfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: writing contents to file {file_path}: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write contents to a specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path within the working directory to find the necessary file to write to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the specified file.",
            ),
        },
    ),
)