from src import cli,log,loader,stats,reporter

def main():
    args = cli.get_args()
    log.setup_log()
    log.log_info("Started for Running....")
    header,data = loader.data_loader(args.input)
    basic_data,correaltions = stats.basic_operation(data,header)
    log.log_info("Data Accessing and Operation on data is done.")
    reporter.showing(basic_data,correaltions,header,args.output,args.format)
    log.log_info("Program Execuated Succesfully.")
    
if __name__ == "__main__":
    main()