from horus.file_manager import target_run_dir

def subfinder_social_output(diff) -> str:
    subfinder_output = []

    if diff:
        subfinder_output.append(f"Changes found with Subfinder: {len(diff)}")        
    else:
        subfinder_output.append("No subfinder results (No changes or first run)")

    return "\n".join(subfinder_output)

def output_subfinder_data(diff: dict, target) -> None:

    output_location = target_run_dir(target) / "output" / "subfinder.txt"
    if output_location.is_file():
        return
    
    output_location.parent.mkdir(parents=True, exist_ok=True)
    with open(output_location, "w") as f:
        for item in diff.items():
            f.write(f"{item}\n")