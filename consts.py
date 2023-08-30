import os


def load_dotenv(file_path=".env"):
    """
    Load environment variables from a file and set them in the os.environ dictionary.

    This function reads environment variable assignments in the format 'key=value' from
    the specified file and sets the corresponding environment variables in the
    os.environ dictionary. Each line in the file is expected to contain a single
    environment variable assignment.

    :param file_path: Path to the file containing environment variable assignments.
                     The default is '.env' in the current directory.
    :type file_path: str
    """
    # Open the specified file for reading
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            # Split the line into key and value using '=' as the delimiter
            key, value = line.strip().split("=")
            # Set the environment variable 'key' with the corresponding 'value'
            os.environ[key] = value


# Load variables from .env
load_dotenv()

SENDER = os.getenv("GMAIL_USERNAME")
PASSWORD = os.getenv("GMAIL_PASSWORD")
RECEIVER = "alexsychev27@gmail.com"
list_of_receivers = ["alexsychev27@gmail.com", "YehudaShani88@gmail.com"]