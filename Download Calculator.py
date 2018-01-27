# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def download_time(fileSize, fileSizeUnit, bandwitdh, bandwitdhUnit):
    
    kilo = 2 ** 10
    
    mega = kilo ** 2
    
    giga = kilo ** 3
    
    tera = kilo ** 4
    
    dict = {"kb":kilo, "kB": kilo * 8, "Mb": mega, "MB": mega * 8, "Gb": giga, "GB": giga * 8, "Tb": tera, "TB": tera * 8}
    
    return convert_seconds( (1.0 * fileSize * dict[fileSizeUnit]) / (bandwitdh * dict[bandwitdhUnit]) )



def convert_seconds(seconds):
    
    hour = int(seconds / 3600)
    minute = int(seconds % 3600 / 60)
    second = seconds % 60

    hourS = " hours, " if hour != 1 else " hour, "
    minuteS = " minutes, " if minute != 1 else " minute, "
    secondS = " seconds" if second != 1 else " second"

    return str(hour) + hourS + str(minute) + minuteS + str(second) + secondS

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print (download_time(13,'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print (download_time(13,'GB', 5.6, 'Mb'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print (download_time(10,'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print (download_time(10,'MB', 2, 'kb'))
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


