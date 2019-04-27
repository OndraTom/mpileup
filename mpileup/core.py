import os
import subprocess
from mpileup.logger import Logger
from mpileup.config import Config


class Mpileup:

    input_file_extension = ".BAM"
    output_file_extension = ".mpileup.samtools"

    def __init__(self, config: Config, output_dir_path: str, logger: Logger = None):
        self.config = config
        self.output_dir_path = output_dir_path
        self.logger = logger

    def run(self):
        reference_path = self.config.get_reference_path()
        bam_files_dir_path = self.config.get_bam_files_dir_path()
        for filename in os.listdir(bam_files_dir_path):
            if filename.endswith(self.input_file_extension):
                output_file_name = filename[:-len(self.input_file_extension)]
                output_file_path = self.output_dir_path + "/" + output_file_name
                input_file_path = bam_files_dir_path + "/" + filename
                command = " ".join(
                    ["/app/samtools-1.9/samtools", "mpileup", "-f", reference_path, input_file_path]
                ) + " > " + output_file_path + self.output_file_extension
                self._log_info("Executing command: " + command)
                return_code = subprocess.call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                if return_code != 0:
                    raise MpileupException("Execution of the last command ended with error")

    def _log_info(self, message: str):
        if self.logger:
            self.logger.log_info(message)

    def _log_error(self, message: str):
        if self.logger:
            self.logger.log_error(message)


class MpileupException(Exception):
    pass
