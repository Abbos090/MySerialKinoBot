def format_duration(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    if hours > 0:
        return f"{hours} soat, {minutes} daqiqa, {sec} soniya"
    return f"{minutes} daqiqa, {sec} soniya"

def generate_caption(seria: tuple) -> str:
    serial_name = seria[1]
    serial_language = seria[2]
    serial_janr = seria[3]
    serial_fasl = seria[4]
    serial_year = seria[5]
    serial_qism = seria[7]
    second = seria[9]

    duration = format_duration(second if second else 0)

    caption = (
        f"🎬 Nomi: {serial_name}\n"
        f"🌐 Til: {serial_language}\n"
        f"🎭 Janr: {serial_janr}\n"
        f"📆 Yili: {serial_year}\n"
        f"🎞 Fasl: {serial_fasl} | Qism: {serial_qism}\n"
        f"⏱ Davomiyligi: {duration}"
    )
    return caption
