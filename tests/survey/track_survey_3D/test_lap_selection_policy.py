"""
test_lap_selection_policy.py
"""

from __future__ import annotations

from kartsimdt.survey.track_survey_3d.full_lap import FullLap
from kartsimdt.survey.track_survey_3d.lap_selection_policy import (
    LapSelectionPolicy,
)


def test_select_nine_laps_after_warmup() -> None:
    laps = [
        FullLap(
            session_index=0,
            lap_number=number,
            start_time=float(number * 10),
            end_time=float(number * 10 + 5),
        )
        for number in range(2, 14)
    ]

    policy = LapSelectionPolicy()

    selected = policy.select(laps)

    print()
    print("========== LAP SELECTION ==========")
    print("Input laps :")
    print([lap.lap_number for lap in laps])

    print("Selected :")
    print([lap.lap_number for lap in selected])
    print("===================================")

    assert len(selected) == 9

    assert [lap.lap_number for lap in selected] == [
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
    ]
