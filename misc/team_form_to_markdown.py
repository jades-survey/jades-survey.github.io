import csv
from collections import OrderedDict


PROFILE_IMAGE_HTML_TEMPLATE = "<img src=\"/assets/images/team/{lastname}_{firstname}.jpg\" onerror=\"this.src='/assets/images/team/fallback.jpg'\">"
PROFILE_NAME_HTML_TEMPLATE = "<a href=\"{url}\">{name}</a>"


def row_to_html(row: OrderedDict) -> str:
    html = "<tr>\n"

    # image
    html += "<td>" + PROFILE_IMAGE_HTML_TEMPLATE.format(
        firstname=row["Name"].split(" ")[0],
        lastname=row["Name"].split(" ")[1],
    ) + "</td>\n"

    # name
    if row["URL or Website to cross link"] == "":
        html += "<td>" + row["Name"] + "</td>\n"
    else:
        html += "<td>" + PROFILE_NAME_HTML_TEMPLATE.format(
            name=row["Name"],
            url=row["URL or Website to cross link"],
        ) + "</td>\n"

    # position
    # html += "<td>" + row["Title"] + "</td>\n"

    # institution
    html += "<td>" + row["Institution"] + "</td>\n"

    # biography
    html += "<td>" + row["1-2 sentence biographical info (JADES related please)"] + "</td>\n"

    html += "</tr>\n"

    return html




def main():
    with open(r"JADES Team Site Info.csv", "r") as f:
        reader = csv.DictReader(f)
        markdown_rows = list(map(row_to_html, reader))

    page_str = "\n".join(
        [
            "---",
            "layout: single",
            "title: Team",
            "permalink: /team/",
            "---",
            "",
            "",
            "<div id=\"main\">",
            "<table>",
            "<tbody>",
            *markdown_rows,
            "</tbody>",
            "</table>",
            "</div>",
        ]
    )


    with open("team.markdown", "w") as f:
        f.write(page_str)

if __name__ == '__main__':
    main()