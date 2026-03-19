from src import loader,log,reporter,stats

from src.cli import get_args
def main():
    args = get_args()
    print("Starting Statistical Analysis...")
    log.setup_logging()
    log.log_info("Statistical analysis started.")
    data,col_names,format=loader.analysis(args.input, args.output, args.format)
    
    
    if data is not None:
        result = stats.basic_operation(data,col_names,format)
        log.log_info("Basic statistical operations completed.")
        reporter.report(result, col_names, format,args.output)
        log.log_info("Report generation completed.")
        print("Statistical Analysis Completed.")
    
if __name__ == "__main__":
    main()