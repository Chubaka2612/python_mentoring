import argparse
import module_finder
import log_configurator

parser = argparse.ArgumentParser(description='Logging and parsing demo')
parser.add_argument('package_name', type=str, help='Package name for analysis')
parser.add_argument('file_level', type=str, help='Logging level for file')
parser.add_argument('console_level', type=str, help='Logging level for console')
args = parser.parse_args()


# run command from module_3 python demo.py setuptools DEBUG INFO
def main():
    print("==========task#1")

    log = log_configurator.get_logger('module_finder', args.file_level, args.console_level)
    module_finder.get_package_path(args.package_name, log)


main()
