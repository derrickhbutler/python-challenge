import csv


with open("Output.txt", "w") as text_file:
    with open('budget_data.csv','r') as budget_csv:
        csv_reader = csv.DictReader(budget_csv)

    # for line in csv_reader:
        # print(count((line['Date']))
        print("Financial Analysis")
        print("------------------------------")
        #The total amount of months in the dataset
        #
        reader = [line for line in csv_reader]

        print ("\nTotal Months:  ", len(([line['Date'] for line in reader])))
        profit_values =[line['Profit/Losses'] for line in reader]
        month_values = [line['Date'] for line in reader]
        print(f"Total: ${sum([int(x) for x in profit_values])}")
        text_file.write(f"Total: ${sum([int(x) for x in profit_values])}")

        diff_list = [(int(profit_values[n]) - int(profit_values[n-1])) for n in range(1, len(profit_values))]

        print(f"Average  Change:  ${ round(sum(diff_list)/ (len([line['Profit/Losses'] for line in reader]) -1 ), 2)}")
        text_file.write(f"\nAverage  Change:  ${ round(sum(diff_list)/ (len([line['Profit/Losses'] for line in reader]) -1 ), 2)}")

        # Question: The greatest increase in profits (date and amount) over the entire period
        max_value = max([int(profit_values[n]) - int(profit_values[n-1]) for n in range(1, len(profit_values))])
        index_value = [int(profit_values[n]) - int(profit_values[n-1]) for n in range(1, len(profit_values))].index(max_value)

        print(f"Greatest Increase in Profits: {month_values[index_value + 1]} ${max([int(profit_values[n]) - int(profit_values[n-1]) for n in range(1, len(profit_values))])}")
        text_file.write(f"\nGreatest Increase in Profits: {month_values[index_value + 1]} ${max([int(profit_values[n]) - int(profit_values[n-1]) for n in range(1, len(profit_values))])}")

        # Question: The minimun increase in profits (date and amount) over the entire period
        min_value = min([int(profit_values[n]) - int(profit_values[n-1]) for n in range(1, len(profit_values))])
        min_index_value = [int(profit_values[n]) - int(profit_values[n-1]) for n in range(1, len(profit_values))].index(min_value)

        print(f"Minimum Increase in Profits: {month_values[min_index_value + 1]} ${min([int(profit_values[n]) - int(profit_values[n-1]) for n in range(1, len(profit_values))])}")
        text_file.write(f"\nMinimum Increase in Profits: {month_values[min_index_value + 1]} ${min([int(profit_values[n]) - int(profit_values[n-1]) for n in range(1, len(profit_values))])}")
    # print("Month is: ", month_values[24 + 1])
    # diff = []

    # for  n in range(1, len(profit_values)):
    #     diff = int(profit_values[n] - int(profit_values[n-1]))

