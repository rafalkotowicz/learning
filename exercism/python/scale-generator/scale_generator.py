"""Scale Generator exercise solution."""

from typing import ClassVar


class Scale:
    """Generate chromatic and interval-based musical scales from a tonic note."""

    _SHARP_NOTES: ClassVar[tuple[str, ...]] = (
        "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"
    )
    _FLAT_NOTES: ClassVar[tuple[str, ...]] = (
        "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"
    )
    _FLAT_TONICS: ClassVar[frozenset[str]] = frozenset(
        {"F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"}
    )
    _INTERVAL_STEPS: ClassVar[dict[str, int]] = {"m": 1, "M": 2, "A": 3}

    def __init__(self, tonic: str) -> None:
        self._source_tonic = self._normalize_source_tonic(tonic)
        self._tonic = self._format_note(self._source_tonic)
        self._base_scale = (
            self._FLAT_NOTES
            if self._source_tonic in self._FLAT_TONICS
            else self._SHARP_NOTES
        )

    @staticmethod
    def _normalize_source_tonic(tonic: str) -> str:
        tonic_text = tonic.strip()
        return tonic_text[0] + tonic_text[1:].lower()

    @staticmethod
    def _format_note(tonic: str) -> str:
        return tonic[0].upper() + tonic[1:]

    def chromatic(self) -> list[str]:
        """Return the 12-note chromatic scale starting from the tonic."""
        start_position = self._base_scale.index(self._tonic)
        return list(self._base_scale[start_position:] + self._base_scale[:start_position])

    def interval(self, intervals: str) -> list[str]:
        """Return notes defined by the provided interval pattern."""
        chromatic_notes = self.chromatic()
        note_positions = [0]

        for interval_code in intervals:
            next_position = note_positions[-1] + self._INTERVAL_STEPS[interval_code]
            note_positions.append(next_position % len(chromatic_notes))

        return [chromatic_notes[position] for position in note_positions]
