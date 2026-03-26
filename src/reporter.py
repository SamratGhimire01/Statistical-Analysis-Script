import numpy as np
import json
def showing(basic_data,correaltions,header,output,format):
    if format == "console":
        
        w = 12  # Set one width for everything
        
        # 1. Basic Stats Table
        result = " " * w
        for h in header:
            result += f"{h:>{w}}"
        print(f"\nBasic Stats:")
        d1 = ['Mean', 'Median', 'STD']
        for i, row in enumerate(basic_data):
            
            row_vals = "".join(f"{v:>{w}}" for v in row) 
            result += f"\n{d1[i]:<{w}}{row_vals}"
            
        print(f"\n{result}\n\nCorrelation:\n")
        
        result = " "*w
        for h in header:
            result += f"{h:>{w}}"
        
        for i,data in enumerate(correaltions):
            row_vals = "".join(f"{v:>{w}}" for v in data) 
            result += f"\n{header[i]:<{w}}{row_vals}"
        print(result)
    else:
        # Convert basic_data rows (skipping the label at index 0) into a dictionary {Header: Value}
        output_data = {
            "Basic Operation": {
                "Mean": dict(zip(header, basic_data[0].tolist())),
                "Median": dict(zip(header, basic_data[1].tolist())),
                "STD": dict(zip(header, basic_data[2].tolist()))
            },
            "Correlation Matrix": {
                # This creates a nested dictionary {RowHeader: {ColHeader: Value}}
                "Correlation": {
                    h_row: dict(zip(header, row.tolist())) 
                    for h_row, row in zip(header, correaltions)
                }
            }
        }

        
        with open(output,'w') as file:
            json.dump(output_data,file,indent=2)
        