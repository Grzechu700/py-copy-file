def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format")
        return

    src_file_name = parts[1]
    dest_file_name = parts[2]

    if src_file_name == dest_file_name:
        return

    try:
        with (open(src_file_name, "r") as file_in,
              open(dest_file_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File {src_file_name} not found.")
    except Exception as e:
        print(f"An error occured: {e}")
