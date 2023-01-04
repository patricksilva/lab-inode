import sys
import shutil

def main():
    print('Testing inodes')
    n_files = int(sys.argv[1])
    print(f'Generating {n_files} copies of files')
    src = sys.argv[2]
    for i in range(0, n_files):
        dst = f'{src}-{i:05d}'
        print(f'Copying file number {i} and storing it into {dst}...')
        shutil.copyfile(src, dst)

if __name__ == '__main__':
    main()
