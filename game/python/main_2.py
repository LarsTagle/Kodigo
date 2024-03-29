import subprocess

notes = "Operating System Concepts covers the functions of operating systems, computer-system architecture, structure, operations, and storage management. An Operating System is a program that serves as an intermediary between a computer user and its hardware, with the primary goals of executing user programs, making problem-solving easier, making the computer system more convenient, and efficiently using the computer hardware. The computer system consists of four components: hardware, which provides basic computing resources like CPU, memory, and I/O devices; the operating system, which controls and coordinates hardware use among applications and users; application programs, which define how system resources are used to solve user computing problems; and users, including people, machines, and other computers. The Operating System (OS) is a resource allocator that manages all resources, decides between conflicting requests for efficient and fair use, and controls program execution to prevent errors and improve computer usage."
python_path = r"D:\renpy-8.1.3-sdk\Python311\python.exe"
py_path = r"D:\renpy-8.1.3-sdk\Kodigo\game\python\fill_in_blanks.py"
quiz_title = "Quiz 1"
n = "3"

process = subprocess.Popen([python_path, py_path, quiz_title])#, creationflags=subprocess.CREATE_NO_WINDOW)

