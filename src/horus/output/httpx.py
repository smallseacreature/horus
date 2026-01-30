from horus.file_manager import target_run_dir

def httpx_social_output(diff) -> str:
    httpx_output = []
    
    if diff:
        httpx_output.append(f"Changes found with httpx: {len(diff)}")
    else:
        httpx_output.append("No httpx results (No changes or first run)")

    return "\n".join(httpx_output)

def output_httpx_data(diff: dict, target) -> None:

    output_location = target_run_dir(target) / "output" / "httpx.txt"

    if output_location.is_file():
        return
    
    output_location.parent.mkdir(parents=True, exist_ok=True)
    with open(output_location, "w") as f:
        for item in diff.items():
            f.write(f"{item}\n")