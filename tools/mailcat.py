import subprocess

def run_mailcat(domain):
    try:
        result = subprocess.run(["mailcat", "--domain", domain], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error running mailcat: {result.stderr.strip()}"
    except FileNotFoundError:
        return "Mailcat is not installed or not in PATH."
