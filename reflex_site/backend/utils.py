from datetime import datetime, timezone


def convert_str_to_datetime(created_at: str) -> datetime:
    if not created_at:
        return datetime.now(timezone.utc)
    else:
        date_str, time_str = created_at.split("T")
        date_int = [int(d) for d in date_str.split("-")]
        time_int = [int(t) for t in time_str.split(":")]
        return datetime(
            *date_int,
            *time_int,
            tzinfo=timezone.utc,
        )


def proccess_form_data(form_data: dict) -> dict:
    data = {}
    for k, v in form_data.items():
        if k == "created_at":
            v = convert_str_to_datetime(form_data["created_at"])
        if k == "content":
            continue
        data[k] = v
    return data


def get_time() -> datetime:
    return datetime.now(timezone.utc)
