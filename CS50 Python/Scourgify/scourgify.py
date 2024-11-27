import csv
import sys


def main():
    # Check if the number of command-line arguments is correct
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists and can be read
    try:
        with open(input_file, "r") as infile:
            reader = csv.DictReader(infile)
            # Ensure the input file has the correct columns
            if "name" not in reader.fieldnames or "house" not in reader.fieldnames:
                sys.exit(f"Could not read {input_file}")

            # Prepare the output file
            with open(output_file, "w", newline="") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
                writer.writeheader()

                # Write reformatted data to the output file
                for row in reader:
                    try:
                        last, first = row["name"].split(", ")
                        writer.writerow({"first": first, "last": last, "house": row["house"]})
                    except ValueError:
                        sys.exit(f"Could not process row: {row}")
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == "__main__":
    main()
