from argparse import ArgumentParser

def get_args():
    prase = ArgumentParser(description="Statistical Analysis.")
    prase.add_argument("--input", required=True, help="This is required to take the input data csv.")
    prase.add_argument("--output", default="data/sample_output.json", help="This is required to save the analysied data in destination place.")
    prase.add_argument("--format" ,default='console', choices=['console','json'], help="This helps to save in json or display in console.")
    
    args = prase.parse_args()
    return args