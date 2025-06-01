import multiprocessing


# Function to calculate the square of a number
def square(num):
    print(f"Process {multiprocessing.current_process().name}: Square of {num} is {num * num}")


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Creating a process pool to execute the function in parallel
    processes = []

    for num in numbers:
        process = multiprocessing.Process(target=square, args=(num,))
        processes.append(process)
        process.start()  # Start each process

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("Multiprocessing Task Completed!")


# Define a function (square) that computes the square of a number.
# Create multiple processes using multiprocessing.Process(), each running square(num).
# Start each process using process.start().
# Ensure all processes complete using process.join().
# Each process runs independently in parallel, using separate memory spaces.