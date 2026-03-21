
import json

def report(result, col_names, format_type, output_folder):
    if format_type== "json":
        with open(output_folder,'w') as file:
            json.dump(result,file,indent=2)
        print(f"Report succesfully saved to {output_folder}")

    if format_type == "console":
        width = 20
        correlation = "".ljust(width) + "".join(name.ljust(width) for name in col_names) + "\n"
        for i, feature in enumerate(col_names):
            print(f"\n----------{i+1}) Statistical Data of {feature}----------\n")
            print(f"Mean: {result[feature]['mean']}")
            print(f"Median: {result[feature]['median']}")
            print(f"Standard Deviation: {result[feature]['std']}\n")
            row_header = feature.ljust(width)
            row_values = "".join(str(val).ljust(width) for val in result['correlation_matrix'][i])
            correlation += f"{row_header}{row_values}\n"
        print("Correlation Matrix:")
        print(correlation)