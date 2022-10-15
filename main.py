list_group_items = []
paragraph_title_list = []
list_paragraphs = []

section_titles = []

section_titles_two = []

split_list_keys = [['1', '  Definitions  '], ['2', '  General interpretation of Act  '], ['3', '  Objective of Act  '], ['4', '  Principles  '], ['5', '  Insurance business and limitations on other business  '], ['6', '  Conducting of insurance business by branches of foreign reinsurers and  Lloyd ’s underwriters  '], ['7', '  Claims against branches of foreign reinsurers or Lloyd ’s underwriters  '], ['8', '  Application of Part  '], ['9', '  Notification by insurer on becoming part of group of companies  '], ['10', '  Designation of insurance group and licensing of controlling company  '], ['11', '  Responsibility of board of directors of controlling company  '], ['12', '  Transparent insurance group structure  '], ['13', '  Fit and proper requirements for key persons and significant owners  '], ['14', '  Approval of appointment of certain key persons  '], ['15', '  Notification of appointment and change of circumstances of certain key  persons  '], ['16', '  Termination of appointment of key persons  '], ['17', '  Changes in control of insurer or controlling compa ny '], ['18', '  Registration of shares in name of nominee  '], ['19', '  Key person or significant owner not fit and proper or no longer fit and proper  '], ['20', '  Assessing if key person or significant owner is fit and  proper  '], ['21', '  Application of Chapter  '], ['22', '  Requirements for licence  '], ['23', '  Licensing  '], ['24', '  Lloyd ’s underwriters and Lloyd ’s licensed  '], ['25', '  Licence conditions  '], ['26', '  Variation of licence conditions  '], ['27', '  Suspension of licence  '], ['28', '  Consequences of suspension of licence  '], ['29', '  Withdrawal of licence  '], ['30', '  Governance framework  '], ['31', '  Failure to maintain governance framework  '], ['32', '  Auditor  '], ['33', '  Audit committee  '], ['34', '  Representative office  '], ['35', '  Application of Part  Page 4 of 148  '], ['36', '  Maintenance  of financially sound condition  '], ['37', '  Capital add -on '], ['38', '  Capital and securities  '], ['39', '  Failure to maintain financially sound condition  '], ['40', '  Security to be held in trust  '], ['41', '  Trust and trustees  '], ['42', '  Failure to provide or maintain security  '], ['43', '  Information concerning beneficial interests  '], ['44', '  Information for supervisory purposes  '], ['45', '  Annual disclosures  '], ['46', '  Annual financial statements and accounting requirements  '], ['47', '  Auditing requirements  '], ['48', '  Additional information relating to foreign reinsurers, Lloyd ’s underwriters or  Lloyd ’s '], ['49', '  Additional matters relating to Chapter  '], ['50', '  Transfer, fundamental transaction or change of institutional form  '], ['51', '  Acquisitions or disposals  '], ['52', '  Application of Chapter  '], ['53', '  Appointment of statutory manager  '], ['54', '  Appointment  of curator  Page 5 of 148  '], ['55', '  Application of Companies Act to business rescue of insurers and controlling  companies  '], ['56', '  Business rescue applications and resolutions  '], ['57', '  Application of Companies Act to winding -up of insurer s and controlling  companies  '], ['58', '  Winding -up applications and resolutions  '], ['59', '  Winding -up of trusts referred to in section 41  '], ['60', '  Applications  '], ['61', '  Notifications  '], ['62', '  General powers, duties and functions of Prudential Authority  '], ['63', '  Prudential Standards  '], ['64', '  Publication by Prudential Authority  '], ['65', '  Determination of another jurisdiction as equivalent  '], ['66', '  Exemptions  '], ['67', '  Unlicensed insurance business  '], ['68', '  Penalties for non -submission or late submission  '], ['69', '  Offences  '], ['70', '  Regulations relating to certain classes of insurance business set out in  Schedule 2  '], ['71', '  Special exemption of certain insurers  '], ['72', '  Consequential amendments and transitional arrangements  '], ['73', '  Short title and commencement  Page 6 of 148  ']]


sub_heading_list = [['CHAPTER 1'],
                    ['ADMINISTRATION OF ACT'], ['CHAPTER 2'], ['AUTHORISATION OF FINANCIAL SERVICES PROVIDERS'],
                    ['CHAPTER 3'],
                    ['REPRESENTATIVES OF AUTHORISED FINANCIAL SERVICES  PROVIDERS'], ['CHAPTER 4'],
                    ['CODES OF CONDUCT'], ['CHAPTER 5'],
                    ['ENFORCEMENT'],
                    ['PART I']]

dropdowns = f'<div class="dropdown pb-4">\n<button type="button" class="btn btn-outline-secondary ' \
            f'dropdown-toggle"\ndata-bs-toggle="dropdown" aria-expanded="false" ' \
            f'data-bs-auto-close="outside">\nPlain Language Summary\n</button>\n<div class="dropdown-menu p-4 ' \
            f'text-muted" style="max-width: 1400px;">\n<p class="summaries"></p>\n</div>\n</div>\n '
final_paragraphs = []
for title in split_list_keys:
    section_number = title[0]
    full_section = '.'.join(title)
# print(title)
# full_section = title[1]
# print(section_number)
# print(full_section)
    item = f'<a class="list-group-item list-group-item-action section-titles" href="#Insurance_act-item-{section_number}">{full_section}</a> '
    paragraph = f'<h4 id="Insurance_act-item-{section_number}">{full_section}<a class="btn btn-link-secondary" ' \
            f'href="#Insurance_act-item-1" role="button">Back to Top</a></h4>\n' \
            f'<p class="paragraphs">...</p>\n {dropdowns} '
    list_group_items.append(item)
    final_paragraphs.append(paragraph)

# for keys in section_titles:
#     key = keys.split(".", 1)
#     split_list_keys.append(key)
#
# print(split_list_keys)

# for title in section_titles:
#     for key in title:
# print(key)
# print(title[key])
# item = f'<a class="list-group-item list-group-item-action" href="#list-item-{key}">{title[key]}</a>'
# paragraph = f'<h4 id="list-item-{key}">{title[key]}</h4>\n<p class="paragraphs">...</p>'
# list_group_items.append(item)
# list_paragraphs.append(paragraph)

# Adding index
# for i in range(46, 46):
#     item = f'<a class="list-group-item list-group-item-action" href="#list-item-{i}"></a>'
#     paragraph = f'<h4 id="list-item-{i}">Item </h4>\n<p class="paragraphs">...</p>'
#     list_group_items.append(item)
#     list_paragraphs.append(paragraph)

# Adding Titles
# for title in section_titles:


for item in list_group_items:
    print(item)

for paragraph in final_paragraphs:
    print(paragraph)

# print(len(list_paragraphs))
