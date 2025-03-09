#!/usr/bin/python3

import os
from wrapper import wrap_file
from datetime import datetime as dt

index = []
posting_html = []
comment = str()

fh = open('helper/skel_header.html', 'r')
for line_head in fh:
    index.append(line_head)
fh.close()

index.append('<h4>Hallo & willkommen</h4>')

fh = open('helper/about.md', 'r')
for about_item in fh:
    index.append(about_item)
fh.close()

index.append('<br><br>')

for root_1, dirs_1, files_1 in os.walk("content/"):
    for vz in sorted(dirs_1):
        category = vz[4:]
        category = category.replace('-', ' ')
        index.append('<h4>' + category + '</h4>')
        for root_2, dirs_2, files_2 in os.walk('content/' + vz + '/'):
            index.append('<ul>')
            for file in sorted(files_2):
                posting = os.path.join(root_2, file)
                base = file[4:len(file)-4]
                desc = base.replace('-', ' ')
                mdate = os.path.getmtime(posting)
                post_date = dt.fromtimestamp(mdate).strftime("%Y-%m-%d")
                temp_comment = wrap_file(posting, base, desc)
                link = ('<a href="' + base + '.html">' + desc + '</a>')
                index.append('<li>' + link + '&nbsp;&nbsp;(Stand: ' + post_date + ')</li>')
            index.append('</ul><br>')
        posting_html = []

index.append('</ul>')

fh = open('helper/skel_footer.html', 'r')
for line_foot in fh:
    index.append(line_foot)
fh.close()

index_fh = open('upload/index.html', 'w')
for index_line in index:
    index_fh.write(index_line)
index_fh.close()
