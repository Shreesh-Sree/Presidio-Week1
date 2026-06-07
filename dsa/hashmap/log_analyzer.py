"""Analyze developer activity logs using a HashMap-style dictionary.

Sample execution:
    $ python dsa/hashmap/log_analyzer.py
    Event frequency:
      COMMIT: 3
      PR_CREATED: 2
      REVIEW: 1
    Most common event: COMMIT (3)
    Least common event: REVIEW (1)

Complexity:
    Time: O(n), where n is the number of activity events.
    Space: O(k), where k is the number of unique event types.
"""

from __future__ import annotations


DEFAULT_ACTIVITY_LOGS: list[str] = [
    "COMMIT",
    "COMMIT",
    "PR_CREATED",
    "REVIEW",
    "COMMIT",
    "PR_CREATED",
]

# TODO: Read events from a text file so this can analyze real exported logs.


def count_events(events: list[str]) -> dict[str, int]:
    """Return a frequency map for developer activity events."""
    frequency: dict[str, int] = {}
    for event in events:
        # Current implementation keeps the event names exactly as received.
        # A future version could normalize case and trim whitespace.
        frequency[event] = frequency.get(event, 0) + 1
    return frequency


def find_most_common(frequency: dict[str, int]) -> tuple[str, int]:
    """Return the event with the highest frequency."""
    if not frequency:
        raise ValueError("frequency map cannot be empty")
    return max(frequency.items(), key=lambda item: item[1])


def find_least_common(frequency: dict[str, int]) -> tuple[str, int]:
    """Return the event with the lowest frequency."""
    if not frequency:
        raise ValueError("frequency map cannot be empty")
    return min(frequency.items(), key=lambda item: item[1])


def render_report(events: list[str]) -> str:
    """Create a readable analytics report for activity logs."""
    frequency = count_events(events)
    most_common_event, most_common_count = find_most_common(frequency)
    least_common_event, least_common_count = find_least_common(frequency)

    lines = ["Event frequency:"]
    for event, count in frequency.items():
        lines.append(f"  {event}: {count}")
    lines.append(f"Most common event: {most_common_event} ({most_common_count})")
    lines.append(f"Least common event: {least_common_event} ({least_common_count})")
    return "\n".join(lines)


def main() -> None:
    """Run the sample developer activity analysis."""
    print(render_report(DEFAULT_ACTIVITY_LOGS))


if __name__ == "__main__":
    main()
