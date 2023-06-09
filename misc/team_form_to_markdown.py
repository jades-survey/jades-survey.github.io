import csv
import numpy as np
from unidecode import unidecode
from collections import OrderedDict


PROFILE_IMAGE_HTML_TEMPLATE = "<img src=\"/assets/images/team_resized/{lastname}_{firstname}.jpg\" onerror=\"this.src='/assets/images/team_resized/fallback.jpg'\">"
PROFILE_NAME_HTML_TEMPLATE = "<a href=\"{url}\">{name}</a>"


def row_to_html(row: OrderedDict) -> str:
    html = "<tr>\n"

    # image
    html += "<td>" + PROFILE_IMAGE_HTML_TEMPLATE.format(
        firstname=row["Name"].split(" ")[0],
        lastname=row["Name"].split(" ")[-1],
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
    names = []
    html_rows = []
    # with open(r"JADES Team Site Info.csv", "r") as f:
    #     reader = csv.DictReader(f)
    #     for r in reader:
    #         name = r["Name"]
    #         html = row_to_html(r)
    #         names.append(name)
    #         html_rows.append(html)

    with open("jades_team_members_short.csv", "r") as f:
        reader = csv.DictReader(f)
        for r in reader:
            names.append(r["Name"])
            html_rows.append(row_to_html(r))

    last = [unidecode(n.split(" ")[-1]) for n in names]
    #markdown_rows = [row[0] for row in sorted(zip(html_rows, last), key=lambda x: x[1])]
    order = np.argsort(last)
    markdown_rows = [html_rows[i] for i in order]

    page_str = "\n".join(
        [
            "---",
            "layout: splash",
            "title: Team",
            "permalink: /team/",
            "---",
            "",
            "",
            '<img src="/assets/images/jades_team_arizona_oct_22.png"',
            '          alt="JADES Team Members"',
            '          style="float: left; margin-right: 10px;" />',
            "",
            "",
            "<div id=\"main\">",
            "<table>",
            "<colgroup>",
            "  <col span=\"1\" class=\"col-img\">",
            "  <col span=\"1\" class=\"col-name\">",
            "  <col span=\"1\" class=\"col-inst\">",
            "  <col span=\"1\" class=\"col-bio\">",
            "</colgroup>",
            "<tbody>",
            *markdown_rows,
            "</tbody>",
            "</table>",
            "</div>",
        ]
    )


    with open("../team.markdown", "w") as f:
        f.write(page_str)
    return html_rows, last

if __name__ == '__main__':
    html, names = main()