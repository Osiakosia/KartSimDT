"""
reader.py

KartSimDT AIM Import Module

Reads AIM CSV telemetry files.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd

from .constants import SUPPORTED_DELIMITERS, SUPPORTED_ENCODINGS
from .exceptions import InvalidAimFileError
from .raw import AimRawData


class AimCsvReader:
    """
    Reads AIM CSV telemetry files.
    """

    def _detect_encoding(
        self,
        file_path: Path,
    ) -> str:
        """
        Detect the encoding of an AIM CSV file.
        """

        for encoding in SUPPORTED_ENCODINGS:
            try:
                with file_path.open(
                    mode="r",
                    encoding=encoding,
                ) as file:
                    file.read(4096)

                return encoding

            except UnicodeDecodeError:
                continue

        raise InvalidAimFileError(f"Unsupported file encoding: {file_path}")

    def _detect_delimiter(
        self,
        file_path: Path,
        encoding: str,
    ) -> str:
        """
        Detect the delimiter used in an AIM CSV file.
        """

        with file_path.open(
            mode="r",
            encoding=encoding,
        ) as file:
            sample = "".join(file.readline() for _ in range(20))

        delimiter = max(
            SUPPORTED_DELIMITERS,
            key=sample.count,
        )

        if sample.count(delimiter) == 0:
            raise InvalidAimFileError("Unable to detect CSV delimiter.")

        return delimiter

    def _read_metadata_block(
        self,
        file_path: Path,
        encoding: str,
        delimiter: str,
    ) -> dict[str, str]:
        """
        Read the AIM CSV metadata block.
        """

        metadata: dict[str, str] = {}

        with file_path.open(
            mode="r",
            encoding=encoding,
            newline="",
        ) as file:

            reader = csv.reader(
                file,
                delimiter=delimiter,
            )

            for row in reader:

                if not row:
                    break

                if len(row) < 2:
                    continue

                key = row[0].strip()
                value = row[1].strip()

                metadata[key] = value

        return metadata

    def _read_channel_names(
        self,
        file_path: Path,
        encoding: str,
        delimiter: str,
    ) -> list[str]:

        with file_path.open(
            mode="r",
            encoding=encoding,
            newline="",
        ) as file:

            reader = csv.reader(
                file,
                delimiter=delimiter,
            )

            metadata_finished = False

            for row in reader:

                if not metadata_finished:
                    if not row:
                        metadata_finished = True
                    continue

                return [name.strip() for name in row]

        return []

    def _read_channel_units(
        self,
        file_path: Path,
        encoding: str,
        delimiter: str,
    ) -> list[str]:
        """
        Read channel units from an AIM CSV file.
        """

        with file_path.open(
            mode="r",
            encoding=encoding,
            newline="",
        ) as file:

            reader = csv.reader(
                file,
                delimiter=delimiter,
            )

            metadata_finished = False
            names_read = False

            for row in reader:

                if not metadata_finished:
                    if not row:
                        metadata_finished = True
                    continue

                if not names_read:
                    # This is the channel names row.
                    names_read = True
                    continue

                # This is the channel units row.
                return [unit.strip() for unit in row]

        return []

    def _read_samples(
        self,
        file_path: Path,
        encoding: str,
        delimiter: str,
    ) -> pd.DataFrame:
        """
        Read telemetry samples from an AIM CSV file.
        """

        samples_start = self._find_samples_start(
            file_path,
            encoding,
            delimiter,
        )

        dataframe = pd.read_csv(
            file_path,
            encoding=encoding,
            delimiter=delimiter,
            skiprows=samples_start,
            header=None,
        )

        return dataframe

    def _find_samples_start(
        self,
        file_path: Path,
        encoding: str,
        delimiter: str,
    ) -> int:
        """
        Find the first telemetry sample row.
        """

        with file_path.open(
            mode="r",
            encoding=encoding,
            newline="",
        ) as file:

            reader = csv.reader(
                file,
                delimiter=delimiter,
            )

            blank_lines = 0

            for line_number, row in enumerate(reader):

                if not row:
                    blank_lines += 1

                    if blank_lines == 2:
                        return line_number + 1

            raise InvalidAimFileError("Unable to locate telemetry samples.")

    def read(
        self,
        file_path: Path,
    ) -> AimRawData:
        """
        Read an AIM CSV telemetry file.
        """

        encoding = self._detect_encoding(
            file_path,
        )

        delimiter = self._detect_delimiter(
            file_path,
            encoding,
        )

        metadata = self._read_metadata_block(
            file_path,
            encoding,
            delimiter,
        )

        channel_names = self._read_channel_names(
            file_path,
            encoding,
            delimiter,
        )

        channel_units = self._read_channel_units(
            file_path,
            encoding,
            delimiter,
        )

        samples = self._read_samples(
            file_path,
            encoding,
            delimiter,
        )

        return AimRawData(
            metadata=metadata,
            channel_names=channel_names,
            channel_units=channel_units,
            samples=samples,
        )
