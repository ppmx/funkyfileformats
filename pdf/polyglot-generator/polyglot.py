#!/usr/bin/env python3

""" PDF polyglot generator. """

import argparse
import io
import os
import shutil
import sys
import zipfile

def pdf_find_offset(stream):
    """ Returns the offset to the beginning of the PDF """

    data = stream.getvalue()
    print(data)
    return data.find(b"%PDF-")

def adjust_xref(stream, offset):
    """ Adjust the xref table by adding the given offset to
    each field. This function is a bit hacked, but it works for
    pdflatex pdf files (after applying `mutool clean -du bla.pdf` on it.
    """

    i = 0
    output_stream = io.BytesIO(b"xref\n")

    # read first line:
    line = stream.readline()
    assert line == b"xref\n"
    output_stream.write(line)

    # read second line:
    line = stream.readline()
    output_stream.write(line)
    number_entries = int(line.strip().decode().split(" ")[1])
    print(f"[+] expecting {number_entries} xref entries")

    while True:
        line = stream.readline().strip().decode()

        if not line or i == number_entries:
            break

        i += 1
        print(i, line)

        entry_offset, kp, used_flag = line.split(" ")
        #print(f"[#{i:04d}] offset = {entry_offset}, flag = {used_flag}")
        new_offset = int(entry_offset) + offset
        output_stream.write(f"{new_offset:010d} {kp} {used_flag}\n".encode())

    assert number_entries == i
    output_stream.write(b"\n")


    while True:
        line = stream.readline()

        if not line:
            break

        output_stream.write(line)

        if line == b"startxref\n":
            startxref = int(stream.readline().strip().decode())
            print("[+] startxref found:", startxref)
            output_stream.write(str(startxref + offset).encode() + b"\n")

    return output_stream

def read_pdf(filename):
    """ Reads the content of a given PDF file and returns its head (header and objects)
    and its tail (xref table and footer). Both will be returnes as io.BytesIO() streams.
    """

    with open(filename, "rb") as f:
        pdf_data = f.read()

    # read pdf version
    #print(pdf_data.find("%PDF-"))

    # scan for xref table
    xref_start = pdf_data.find(b"xref")
    print(f"[+] found xref at position #{xref_start}")

    pdf_head = pdf_data[:xref_start]
    pdf_tail = pdf_data[xref_start:]

    assert pdf_tail.split(b"\n")[0] == b"xref"
    return io.BytesIO(pdf_head), io.BytesIO(pdf_tail)

def main():
    """
    0. Add header
    1. Extract head and tail from given PDF
    2. ZIP
    3. Adjust xref table and startxref entry
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--header")
    parser.add_argument("--output", required=True)
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--files", nargs='*')
    args = parser.parse_args()

    # remove output file if it exists:
    if os.path.exists(args.output):
        print(f"[!] file ({args.output}) already exist. Will be overwritten")
        os.remove(args.output)

    pdf_offset = 0

    # prepare memory and zip archive:
    archive_memory = io.BytesIO()
    archive = zipfile.ZipFile(archive_memory, "w", zipfile.ZIP_STORED, allowZip64=True)

    if args.header:
        print("[+] Write header to memory:", args.header)

        with open(args.header, "rb") as f:
            header_data = f.read()

        # this is actually not a hard limit. But the PDF header must be in the first 1024 bytes.
        assert len(header_data) < 800
        with open(args.output, "ab") as f:
            f.write(header_data)

        pdf_offset += len(header_data)
        print("[+] move PDF offset to:", pdf_offset)

    # read initial pdf and split into header and trailer:
    pdf_head, pdf_tail = read_pdf(args.pdf)

    # write pdf's head to archive and store the tail as comment at the end of zip:
    #archive.writestr(args.pdf, pdf_head.getvalue())
    archive.write(args.pdf)

    print("[+] Add additional files...")
    for additional_filename in args.files:
        print(f"    > {additional_filename}")
        archive.write(additional_filename)

    # adjust xref entries:
    print("[+] Adjust PDF's references (xref)")
    pdf_offset += pdf_find_offset(archive_memory)
    print("    pdf offset:", pdf_offset)

    # Add PDF's tail to archive as comment:
    print("[+] Add PDF tail to archive")
    pdf_tail = adjust_xref(pdf_tail, pdf_offset)
    archive.comment = pdf_tail.getvalue()
    archive.close()

    # Write memory to file:
    print("[+] write polyglot to", args.output)
    with open(args.output, "ab") as f:
        f.write(archive_memory.getvalue())

if __name__ == "__main__":
    main()
