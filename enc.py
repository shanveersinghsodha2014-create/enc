import sys
import os
import zipfile

def encode(files, output):
    with zipfile.ZipFile(output, 'w') as zf:
        for f in files:
            if os.path.isfile(f):
                zf.write(f, arcname=os.path.basename(f))
            else:
                print(f"Warning: {f} is not a file, skipping.")

def decode(enc_file, output_dir):
    with zipfile.ZipFile(enc_file, 'r') as zf:
        zf.extractall(output_dir)

def print_usage():
    print("Usage:")
    print("  enc.py -encode file1 file2 ... -o output.enc")
    print("  enc.py -decode input.enc -o output_folder")

def main():
    args = sys.argv[1:]
    if not args:
        print_usage()
        return

    if args[0] == '-encode':
        if '-o' not in args:
            print("Error: Missing output file (-o).")
            print_usage()
            return
        o_index = args.index('-o')
        files = args[1:o_index]
        output = args[o_index + 1]
        encode(files, output)
        print(f"Encoded {len(files)} files into {output}")

    elif args[0] == '-decode':
        if '-o' not in args:
            print("Error: Missing output directory (-o).")
            print_usage()
            return
        input_file = args[1]
        o_index = args.index('-o')
        output_dir = args[o_index + 1]
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        decode(input_file, output_dir)
        print(f"Decoded {input_file} to {output_dir}")

    else:
        print_usage()

if __name__ == "__main__":
    main()