import os
import logging
import argparse
import json

"""
Collects all BLEU scores from a directory into a single CSV file.
"""

LOGGING_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


OUTPUT_MODES = {
    "APPEND": 'a',
    "WRITE": 'w',
}


def get_argument_parser():
    parser = argparse.ArgumentParser(description="Transform a set of BLEU Score Files into a single CSV file")
    parser.add_argument("--path",
                        type=str,
                        help="Path to a directory (or single file).")
    parser.add_argument("--out",
                        type=str,
                        help="Path to the output csv file. May include a filename or only a directory name.")
    parser.add_argument("--logging",
                        help="logging level in stderr",
                        choices=LOGGING_LEVELS.keys(),
                        default="INFO")
    parser.add_argument("--out-mode",
                        help="How the output file is written to the file",
                        choices=OUTPUT_MODES.keys(),
                        default="APPEND")
    return parser


def get_logger(args):
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(LOGGING_LEVELS[args.logging])
    return logger


def get_metrics_from_filename(filename):
    metrics = {}

    parts = filename.split("_")
    parts = [item.split(".") for item in parts]
    parts = [item for sublist in parts for item in sublist]

    for i in range(len(parts)):
        if parts[i] == "beam":
            metrics["beam"] = parts[i+1]
        if parts[i] == "pads":
            metrics["start_pads"] = parts[i+1]
        if parts[i] == "limit":
            metrics["epsilon_limit"] = parts[i+1]
        if parts[i] == "spi":
            metrics["spi"] = parts[i+1]

    return metrics


def get_header_line():
    return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (
        "Beam Size",
        "Start Pads",
        "Epsilon Limit",
        "SPI",
        "BLEU",
        "Length Ratio",
        "Sys Len",
        "Ref Len",
        "Brevity Penalty",
        "CLASS",
    )


def construct_line_from_metrics(bleu_metrics, file_metrics):
    return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (
        file_metrics["beam"],
        file_metrics["start_pads"],
        file_metrics["epsilon_limit"],
        file_metrics["spi"],
        round(float(bleu_metrics["score"]), 2),
        round(float(bleu_metrics["ratio"]), 2),
        bleu_metrics["sys_len"],
        bleu_metrics["ref_len"],
        round(float(bleu_metrics["bp"]), 2),
        "default",
    )


def write_bleu_to_csv(path_to_input_directory, path_to_output_file, mode=OUTPUT_MODES["APPEND"]):
    with open(path_to_output_file, mode) as output_file:
        if mode == OUTPUT_MODES["WRITE"]:
            output_file.write(get_header_line())

        for file in os.listdir(path_to_input_directory):
            if file.endswith(".bleu") or file.endswith(".BLEU"):
                file_path = os.path.join(path_to_input_directory, file)
                file_handler = open(file_path, "r")
                file_metrics = get_metrics_from_filename(file_path)
                bleu_metrics = json.loads(file_handler.read())
                output_file.write(construct_line_from_metrics(bleu_metrics, file_metrics))


def main():
    parser = get_argument_parser()
    args = parser.parse_args()
    logger = get_logger(args)
    logger.debug(args)

    write_bleu_to_csv(args.path, args.out, mode=OUTPUT_MODES[args.out_mode])


if __name__ == '__main__':
    main()
