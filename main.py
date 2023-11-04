import platform
import os


def block_website(website):
    system = platform.system()

    if system == "Windows":
        # Windows
        host_path = r'C:\Windows\System32\drivers\etc\hosts'
    elif system == "Linux":
        # Linux
        host_path = '/etc/hosts'
    else:
        print("Unsupported operating system")
        return

    with open(host_path, 'r+') as host_file:
        hosts = host_file.read()
        if website in hosts:
            print(f"{website} is already blocked.")
        else:
            host_file.write('127.0.0.1 ' + website)
            print(f"{website} is now blocked.")


def unblock_website(website):
    system = platform.system()

    if system == "Windows":
        host_path = r'C:\Windows\System32\drivers\etc\hosts'
    elif system == "Linux":
        host_path = '/etc/hosts'
    else:
        print("Unsupported operating system")
        return

    with open(host_path, 'r+') as host_file:
        hosts = host_file.readlines()
        host_file.seek(0)
        for line in hosts:
            if not any(website in line for website in [website, f"www.{website}"]):
                host_file.write(line)
        host_file.truncate()
        print(f"{website} is unblocked.")


if __name__ == "__main__":
    while True:
        action = input(
            "Enter 'block' or 'unblock' and the website you want to (un)block (e.g., 'block example.com', 'unblock example.com'): ").split()

        if len(action) != 2:
            print("Invalid input. Please use the format 'block/unblock website'.")
            continue

        command, website = action
        if command == 'block':
            block_website(website)
        elif command == 'unblock':
            unblock_website(website)
        else:
            print("Invalid command. Please use 'block' or 'unblock'.")
