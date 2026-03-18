import stats
import numpy as np
import json
output_folder ='data/sample_output.json'
if stats.format == "json":
    result=stats.basic_operation()
    with open(output_folder,'w') as file:
        json.dump(result,file,indent=2)
    print(f"Report succesfully saved to {output_folder}")

if stats.format == "console":
    basic_stats=stats.basic_operation()
    for i, feature in enumerate(basic_stats.keys()):
        if feature == 'correlation_matrix':
            break
        print(f"\n----------{i+1}) Statistical Data of {feature}----------\n")
        print(f"Mean: {basic_stats[feature]['mean']}")
        print(f"Median: {basic_stats[feature]['median']}")
        print(f"Standard Deviation: {basic_stats[feature]['std']}\n")
        
        
        print(f"Correlation of {feature} to others: {basic_stats['correlation_matrix'][i]}\n")