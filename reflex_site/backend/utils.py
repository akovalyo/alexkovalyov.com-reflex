from datetime import datetime, timezone


def convert_str_to_datetime(created_at: str) -> datetime:
    if not created_at:
        return datetime.now(timezone.utc)
    else:
        return datetime(
            *[
                int(num)
                for num in created_at.split(
                    "-",
                )
            ],
            tzinfo=timezone.utc,
        )
