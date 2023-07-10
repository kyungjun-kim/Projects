from emoji import core
def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Position,Company,Location,URL,Source\n")

    for job in jobs:
        loca = core.replace_emoji(job['location'],replace="").strip()
        file.write(
            f"{job['position']},{job['company']},{loca},{job['link']},{job['source']}\n"
        )
    file.close()
