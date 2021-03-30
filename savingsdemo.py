import sys
import argparse

def calculate_savings(amount, annual_rate, total_years):
    """
    Calculates savings after total_years givven annual  
    saving amout and annual rate
    """
    total = 0
    history = []
    for year in range(total_years):
        total = total + amount
        total = total * (1 + annual_rate)
        total = round(total, 2)
        history.append(total)
        print(f"Total value after {year + 1}: {total}")

    return history


if __name__ == "__main__":

    try:
        amount = int(sys.argv[1])
        rate = float(sys.argv[2])
        year = int(sys.argv[3])
    except IndexError:
        print("Usage: savingsdemo.py amout rate year")
        exit()

    print("Final value", calculate_savings(amount, rate, year)[-1])