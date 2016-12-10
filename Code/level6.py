import re, zipfile

zip_file_name = '../Resource/channel.zip'
zip_file = zipfile.ZipFile(zip_file_name)

file_format = '.txt'
next_file_name = '90052'

comment = []

while int(next_file_name):
    content = zip_file.read(next_file_name + file_format)
    print content
    finding = re.search('\d+', content)
    if finding:
        next_file_name = finding.group(0)
        info = zip_file.getinfo(next_file_name + file_format)
        c = info.comment
        comment.append(c)
    else:
        break

print ''.join(comment)

