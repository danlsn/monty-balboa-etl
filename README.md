# Monty Balboa ETL Project (Montague Street Bridge)

__Made possible by the data from the [TeeWallz/monty_balboa](https://github.com/TeeWallz/monty_balboa/tree/main) 
project__

## Project Description

This is an example ETL project in its simplest form. It is designed to demonstrate a common task that a Data 
Engineer might be required to perform.

It accomplishes the following using Python:
1. Download the data as JSON from the website [How Many Days Since Montague Street Bridge Has Been Hit?](https://howmanydayssincemontaguestreetbridgehasbeenhit.com/)
2. Load the data into a Pandas DataFrame
3. Normalize the semi-structured data into rows and columns
4. Export the data as a CSV file

## How to Run

If you're unfamiliar with Python, some of these steps might make no sense. If you're on a Windows machine, you'll 
have to use PowerShell to enter these commands. 

You'll need to have both `git` and `python` installed on your machine. If you don't have them, you can download them
here:
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/) (make sure to check the box that says "Add Python to PATH")

### Follow these steps to run the script:
1. Clone the repository
2. Install the dependencies
3. Run the script

```bash
# Clone the repository and cd into it
git clone https://www.github.com/danlsn/monty-balboa-etl.git
cd monty-balboa-etl
# Install the dependencies
pip install -r requirements.txt
# Run the script
python pipeline.py
```

## Packages Used

- Pandas: the gold standard for data manipulation in Python
- Requests: for making HTTP requests
- JSON: for parsing JSON data
- Datetime: for converting the date string into a datetime object
- pathlib: for working with file paths
- tqdm: totally unnecessary, but it makes the process look cool

## Takeaways

Data Engineering is fundamentally about moving data from one place to another. This project is simple but it 
captures the basic steps in the approach to solving a data engineering problem. Other datasets you'll encounter in 
the wild will be more complex, your source data might be different, and you might output to a different place, but
the core steps will be the same.

Go out there and build something cool!
