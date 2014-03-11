import ftplib
import sys

# File usage: download_genomes.py [directory] [filematch]
# Example: download_genomes.py /refseq/release/microbial/ fna.gz
# Currently only does one folder at a time

# directory should be the ABSOLUTE path name for the download location
# if you want to download from the "/refseq/release/microbial/" folder, input exactly that (without the quotations)
# MAKE SURE YOU START IT WITH A SLASH / and END WITH A SLASH / 
directory = sys.argv[1]

# filematch should be something like "rna.fna.gz", "faa.gz" or "fna.gz", depending on what files you want
filematch = "*." + sys.argv[2]
 
# connection information
server = 'ftp.ncbi.nlm.nih.gov'
username = 'anonymous'
password = 'password'
 
# connect to the server
ftp = ftplib.FTP(server)
ftp.login(username, password)
print "Connected to " + server
 
# change to the directory we are downloading from
ftp.cwd(directory)
 
print "Attempting to download files!"
# loop through all files that match the given filematch and download them
# this will download to the directory you run the script from, so watch out!
for filename in ftp.nlst(filematch):
    fhandle = open(filename, 'wb')
    print 'Downloading ' + filename
    ftp.retrbinary('RETR ' + filename, fhandle.write)
    fhandle.close()