import matplotlib.pyplot as plt
import numpy as np

def conjecture_sequence(n_value, y_list, x_list):
    y_list.append(n_value)
    while n_value > 1:
        if n_value % 2 == 0:
            n_value = n_value // 2
            y_list.append(n_value)
        else:
            n_value = 3 * n_value + 1
            y_list.append(n_value)
        x_list.append(x_list[-1] + 1)

def main():
    initial_value = str(input("Enter a natural number (1-1,000,000): "))
    n_value = int(initial_value)

    if n_value <= 1000000 and n_value > 1:
        x = [1]             # x-axis
        y = []              # y-axis
        plt.figure(figsize=(15, 15), dpi=300)
        #y.append(n_value)

        # While input value (n) is more than one the value will get:
        #   divided by 2 if n is even.
        #   If n is odd, n will get multiplied by 3 and added to 1.
        # while n_value > 1:
        #     if n_value % 2 == 0:
        #         n_value = n_value // 2
        #         y.append(n_value)
        #     else:
        #         n_value = 3 * n_value + 1
        #         y.append(n_value)
        #     x.append(x[-1] + 1)
        conjecture_sequence(int(initial_value),y,x)
        
        # Set the x-axis tick interval
        if x[-1] >=50:
            if x[-1] >= 500:
                graph_x_interval = np.arange(10, max(x), 10)
            elif x[-1] >= 100:
                graph_x_interval = np.arange(5, max(x), 5)
            else:
                graph_x_interval = np.arange(2, max(x), 2)
            x_tick = np.insert(graph_x_interval, 0, 1)
            plt.xticks(x_tick)
        else:
            plt.xticks(np.arange(1, max(x)))

        # Set the y-axis tick interval
        if max(y) >= 1000:
            if max(y) >= 100000:
                interval_y = round(max(y) // 20, -3)
            elif max(y) >= 5000:
                interval_y = round(max(y) // 20, -2)
            else:
                interval_y = round(max(y) // 10, -2)
            y_tick = np.arange(interval_y, max(y), interval_y)
            plt.yticks(y_tick)  
        
        # Display Figure
        plt.plot(x, y, marker='o')
        plt.title("3n+1 Conjecture", fontsize=20)
        plt.xlabel("Step / Iteration", fontsize=16)
        plt.ylabel("Number (n)", fontsize=16)
        plt.show()

        # Print sequence
        print("Sequence:")
        print(*y, sep= ", ")
        print("\nIt takes", x[-2], "steps to get to 1.")
        print("Max Y value (n):", max(y))
        
        # Save Figure
        fig = plt.gcf()
        fig.savefig(initial_value + '_graph.png')
    else:
        print("You have entered an invalid value.")


if __name__ == '__main__':
    main()
