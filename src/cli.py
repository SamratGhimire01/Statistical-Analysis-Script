from argparse import ArgumentParser

def get_args():
    parse = ArgumentParser(description= "statistical-analysis")
    parse.add_argument("--input",required=True, help="Getting the input of CSV file.")
    parse.add_argument("--output",default="data/sample_output.json", help="Giving the output of CSV file after the processing.")
    parse.add_argument("--format",choices=['console','json'],default="console", help="Showing the result.")
    args = parse.parse_args()
    return args
