import argparse


def create_parser(app=None, desc=None, subparser=None):
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--one', action='store_true', default=False, help='Stop after the first file written.')
    parser.add_argument('--dry', action='store_true', default=False, help='Dry run, do not write any data file.')
    parser.add_argument('--this', type=int, default=-1, help='Fetch this specific ID')

    parser.add_argument('--min-words', type=int, default=3, help='Minimum number of words to accept a sentence')
    parser.add_argument('--max-words', type=int, default=15, help='Maximum number of words to accept a sentence')

    parser.add_argument('output', type=str, help='Output directory')

    subparsers = parser.add_subparsers(help='App-specific')

    args = parser.parse_args()

    check_output_dir(args.output)

    return args
