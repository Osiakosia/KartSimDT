from pathlib import Path

from kartsimdt.io.aim.reader import AimCsvReader


def test_reader_reads_sample_file() -> None:
    reader = AimCsvReader()

    raw = reader.read(Path("tests/data/aim/rotena_sample.csv"))

    assert raw.metadata["Session"] == "Rotena"
    assert len(raw.channel_names) == 18
    assert len(raw.channel_units) == 18
    assert raw.samples.shape == (8400, 18)
