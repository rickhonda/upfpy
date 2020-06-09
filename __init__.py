from upfpy.upf import *

import os.path
if os.path.exists('upfpy/vectors.txt') == False:
    with open('upfpy/vectors.txt', 'w') as csv_file:
        writer = (csv.writer(csv_file, delimiter=','))
        writer.writerow('2')
        writer.writerow([])
        writer.writerow('0')
        writer.writerow('1')


if __name__ == "__main__":
    import upf.__main__
    __main__.main()
