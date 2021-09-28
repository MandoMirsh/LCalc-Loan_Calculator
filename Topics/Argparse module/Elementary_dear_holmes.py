def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


#  filename = args.file
#  opened_file = open(filename)
encoded_text = "Qrn!Mfur!y,pxIMvsMF,BH!rM!rnqv'tMAuv IMAur'JJJMVHzMCr!FIMCr!FMqv n..,v'ArqJMQvqMF,BM!rnyyFMAuv'xMVMD,ByqMB rMAurMPrn r!Mpv.ur!MA,Mr'p,qrMzFMrCvyM.yn'KMc,,!MAuv'tLMjur'MqvqMF,BM A,.MB v'tMF,B!Mo!nv'KMOr AMDv ur IMZ,!vn!AF"  # opened_file.read()  # read the file into a string
#  opened_file.close()  # always close the files you've opened
print(decode_Caesar_cipher(encoded_text, 13))
